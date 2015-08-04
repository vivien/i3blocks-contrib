#!/usr/bin/env python3
#
# Copyright (C) 2015 James Murphy                                                  
# Licensed under the terms of the GNU GPL v2 only.                                 
#                                                                                  
# i3blocks blocklet script to output connected usb storage device info. 

###############################################################################
# BEGIN CONFIG
# You may edit any of the following entries.  DO NOT delete any of them, else 
# the main script will have unpredictable behavior.
###############################################################################

# Color options, can be a color name or #RRGGBB
INFO_TEXT_COLOR = "white"
MOUNTED_COLOR = "green"
PLUGGED_COLOR = "gray"
LOCKED_COLOR = "gray"
UNLOCKED_NOT_MOUNTED_COLOR = "yellow"
PARTITIONLESS_COLOR = "red"

# Default texts
PARTITIONLESS_TEXT = "no partitions"
SEPARATOR = "<span color='gray'> | </span>"

# FontAwesome unicode lock/unlock
FA_LOCK = "\uf023"
FA_UNLOCK = "\uf09c"

# Maximum length of a filesystem label to display. Use None to disable
# truncation, a positive integer to right truncate to that many characters, or
# a negative integer to left truncate to that many characters. Setting this
# option to 0 will disable the displaying of filesystem labels.
TRUNCATE_FS_LABELS = None

# Edit this function to ignore certain devices (e.g. those that are always
# plugged in).
# The dictionary udev_attributes_dict contains all the attributes given by
# udevadm info --query=propery --name=$path
def ignore(path, udev_attributes_dict):
    # E.g. how to ignore devices whose device name begins with /dev/sda
    #if udev_attributes_dict["DEVNAME"].startswith("/dev/sda"):
    #    return True
    return False

# Edit this function to ignore devices before the udev attributes are
# computed in order to save time and memory.
def fastIgnore(path):
    # E.g. how to to ignore devices whose path begins with /dev/sda
    #if path.startswith("/dev/sda"):
    #    return True

    # E.g. how to ignore a fixed set of paths
    #if path in [ "/dev/path1", "/dev/path2", "/dev/path3" ]:
    #    return True
    return False

###############################################################################
# END CONFIG
# DO NOT EDIT ANYTHING AFTER THIS POINT UNLESS YOU KNOW WHAT YOU ARE DOING
###############################################################################

from subprocess import check_output

def pangoEscape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def getLeafDevicePaths():
    lines = check_output(['lsblk', '-spndo', 'NAME'], universal_newlines=True)
    lines = lines.split("\n")
    lines = filter(None, lines)
    return lines

def getKernelName(path):
    return check_output(['lsblk', '-ndso', 'KNAME', path],
            universal_newlines=True).rstrip("\n")

def getDeviceType(path):
    return check_output(['lsblk', '-no', 'TYPE', path],
            universal_newlines=True).strip() 

def getFSType(path):
    global attributeMaps
    return attributeMaps[path].get("ID_FS_TYPE")

def isLUKSPartition(path):
    return getFSType(path) == "crypto_LUKS"

def isSwapPartition(path):
    return getFSType(path) == "swap"

def getFSLabel(path):
    global attributeMaps
    label = attributeMaps[path].get("ID_FS_LABEL_ENC", "")
    if label:
        label = label.encode().decode("unicode-escape")
        if type(TRUNCATE_FS_LABELS) == int:
            if TRUNCATE_FS_LABELS >= 0:
                label = label[:TRUNCATE_FS_LABELS]
            elif TRUNCATE_FS_LABELS < 0:
                label = label[TRUNCATE_FS_LABELS:]
    return label

def getFSOptions(path):
    lines = check_output(['findmnt', '-no', 'FS-OPTIONS', path],
            universal_newlines=True).strip()
    lines = lines.split(",")
    return lines

def isReadOnly(path):
    return "ro" in getFSOptions(path)

def isExtendedPartitionMarker(path):
    global attributeMaps
    MARKERS = ["0xf", "0x5"]
    return attributeMaps[path].get("ID_PART_ENTRY_TYPE") in MARKERS

def getMountPoint(path):
    return check_output(['lsblk', '-ndo', 'MOUNTPOINT', path],
            universal_newlines=True).rstrip("\n")

def getSpaceAvailable(path):
    lines = check_output(['df', '-h', '--output=avail', path],
            universal_newlines=True)
    lines = lines.split("\n")
    if len(lines) != 3:
        return ""
    else:
        return lines[1].strip()

def getLockedCryptOutput(path):
    form = "<span color='{}'>[{} {}]</span>"
    kname = pangoEscape(getKernelName(path))
    output = form.format(LOCKED_COLOR, FA_LOCK, kname)
    return output

def getParentKernelName(path):
    lines = check_output(['lsblk', '-nso', 'KNAME', path],
            universal_newlines=True)
    lines = lines.split("\n")
    if len(lines) > 2:
        return lines[1].rstrip("\n")
    else:
        return ""

def getUnlockedCryptOutput(path):
    mountPoint = getMountPoint(path)
    if mountPoint:
        color = MOUNTED_COLOR
        if isReadOnly(path):
            spaceAvail = "ro"
        else:
            spaceAvail = pangoEscape(getSpaceAvailable(path))
        mountPoint = "<i>{}</i>:".format(pangoEscape(mountPoint))
    else:
        color = UNLOCKED_NOT_MOUNTED_COLOR
        spaceAvail = ""
    kernelName = pangoEscape(getKernelName(path))
    parentKernelName = pangoEscape(getParentKernelName(path))
    
    block = "<span color='{}'>[{} {}:{}]</span>"
    block = block.format(color, FA_UNLOCK, parentKernelName, kernelName)

    label = pangoEscape(getFSLabel(path))
    if label:
        label = '"{}"'.format(label)

    items = [block, label, mountPoint, spaceAvail]
    return " ".join(filter(None, items))

def getSwapOutput(path):
    return ""

def getUnencryptedPartitionOutput(path): 
    mountPoint = getMountPoint(path)
    if mountPoint:
        color = MOUNTED_COLOR
        if isReadOnly(path):
            spaceAvail = "ro" 
        else:
            spaceAvail = pangoEscape(getSpaceAvailable(path))
        mountPoint = "<i>{}</i>:".format(pangoEscape(mountPoint))
    else:
        color = PLUGGED_COLOR
        spaceAvail = ""
    kernelName = pangoEscape(getKernelName(path))

    block = "<span color='{}'>[{}]</span>"
    block = block.format(color, kernelName)

    label = pangoEscape(getFSLabel(path))
    if label:
        label = '"{}"'.format(label)

    items = [block, label, mountPoint, spaceAvail]
    return " ".join(filter(None, items))

def getDiskWithNoPartitionsOutput(path):
    form = "<span color='{}'>[{}] {}</span>"
    kernelName = pangoEscape(getKernelName(path))
    return form.format(PARTITIONLESS_COLOR, kernelName, PARTITIONLESS_TEXT)

def getOutput(path):
    if isSwapPartition(path):
        return getSwapOutput(path)
    t = getDeviceType(path)
    if t == "part":
        if isExtendedPartitionMarker(path):
            return ""
        elif isLUKSPartition(path):
            return getLockedCryptOutput(path)
        else:
            return getUnencryptedPartitionOutput(path)
    elif t == "disk":
        return getDiskWithNoPartitionsOutput(path)
    elif t == "crypt":
        return getUnlockedCryptOutput(path)
    elif t == "rom" :
        return ""

def makeAttributeMap(path):
    attributeMap = {}
    lines = check_output(
            ['udevadm','info','--query=property','--name={}'.format(path)],
            universal_newlines=True)
    lines = lines.split("\n")
    for line in lines:
        if line:
            key, val = line.split("=", maxsplit=1)
            attributeMap[key] = val
    return attributeMap

def getAttributeMaps(paths):
    return {path : makeAttributeMap(path) for path in paths}

leaves = getLeafDevicePaths()
leaves = [path for path in leaves if not fastIgnore(path)]
attributeMaps = getAttributeMaps(leaves)
leaves = (path for path in leaves if not ignore(path, attributeMaps[path]))
outputs = filter(None, map(getOutput, leaves))
output = SEPARATOR.join(outputs)
if output:
    output = "<span color='{}'>{}</span>".format(INFO_TEXT_COLOR, output)
print(output)
print(output)
