#!/usr/bin/env python3
#
# Copyright (C) 2015 James Murphy                                                  
# Licensed under the terms of the GNU GPL v2 only.                                 
#                                                                                  
# i3blocks blocklet script to output connected usb storage device info. 

import os

def _default(name, default='', arg_type=str):
    val = default
    if name in os.environ:
        val = os.environ[name]
    return arg_type(val)

###############################################################################
# BEGIN CONFIG
# Most of these can be specified as command line options, run with --help for
# more information.
# You may edit any of the following entries.  DO NOT delete any of them, else 
# the main script will have unpredictable behavior.
###############################################################################

# Color options, can be a color name or #RRGGBB
INFO_TEXT_COLOR = _default("INFO_TEXT_COLOR", "white")
MOUNTED_COLOR = _default("MOUNTED_COLOR", "green")
PLUGGED_COLOR = _default("PLUGGED_COLOR", "gray")
LOCKED_COLOR = _default("LOCKED_COLOR", "gray")
UNLOCKED_NOT_MOUNTED_COLOR = _default("UNLOCKED_NOT_MOUNTED_COLOR", "yellow")
PARTITIONLESS_COLOR = _default("PARTITIONLESS_COLOR", "red")

# Default texts
PARTITIONLESS_TEXT = _default("PARTITIONLESS_TEXT", "no partitions")
SEPARATOR = _default("SEPARATOR", "<span color='gray'> | </span>")

# Indicate whether an encrypted partition is locked/unlocked, "" is allowed. 
LOCKED_INDICATOR = _default("LOCKED_INDICATOR", "\uf023 ")
UNLOCKED_INDICATOR = _default("UNLOCKED_INDICATOR", "\uf09c ")

# Shows instead of space available when a partition is mounted readonly
READONLY_INDICATOR = _default("READONLY_INDICATOR", "ro")

# Maximum length of a filesystem label to display. Use None to disable
# truncation, a positive integer to right truncate to that many characters, or
# a negative integer to left truncate to that many characters. Setting this
# option to 0 will disable the displaying of filesystem labels.
TRUNCATE_FS_LABELS = _default("TRUNCASE_FS_LABELS", None)

# List of devices to ignore. Must be a valid python3 representation of a list
# of strings
IGNORE_LIST = _default("IGNORE_LIST", "[]")
if IGNORE_LIST:
    import ast
    IGNORE_LIST = list(map(lambda p: 
        p if p.startswith("/") 
        else "/dev/{}".format(p),
        ast.literal_eval(IGNORE_LIST)
    ))


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
    if path in IGNORE_LIST:
        return True

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
import argparse

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
    form = "<span color='{}'>[{}{}]</span>"
    kname = pangoEscape(getKernelName(path))
    output = form.format(LOCKED_COLOR, LOCKED_INDICATOR, kname)
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
            spaceAvail = READONLY_INDICATOR
        else:
            spaceAvail = pangoEscape(getSpaceAvailable(path))
        mountPoint = "<i>{}</i>:".format(pangoEscape(mountPoint))
    else:
        color = UNLOCKED_NOT_MOUNTED_COLOR
        spaceAvail = ""
    kernelName = pangoEscape(getKernelName(path))
    parentKernelName = pangoEscape(getParentKernelName(path))
    
    block = "<span color='{}'>[{}{}:{}]</span>"
    block = block.format(color, UNLOCKED_INDICATOR, parentKernelName, kernelName)

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
            spaceAvail = READONLY_INDICATOR 
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

def parseArguments():
    parser = argparse.ArgumentParser(prog="usb.py",
        description="i3blocks blocklet script to output connected"
        " usb storage device info")
    parser.add_argument("--info-text-color", nargs=1, 
        help="Set the info text color. "
        "Default: {}".format(INFO_TEXT_COLOR))
    parser.add_argument("--mounted-color", nargs=1, 
        help="Set the color of mounted devices. "
        "Default: {}".format(MOUNTED_COLOR))
    parser.add_argument("--plugged-color", nargs=1, 
        help="Set the color of plugged devices. "
        "Default: {}".format(PLUGGED_COLOR))
    parser.add_argument("--locked-color", nargs=1, 
        help="Set the color of locked crypt devices. "
        "Default: {}".format(LOCKED_COLOR))
    parser.add_argument("--unlocked-not-mounted-color", nargs=1, 
        help="Set the color of unlocked not mounted crypt devices. "
        "Default: {}".format(UNLOCKED_NOT_MOUNTED_COLOR))
    parser.add_argument("--partitionless-color", nargs=1, 
        help="Set the color of devicees with no partitions. "
        "Defaut: {}".format(PARTITIONLESS_COLOR))
    parser.add_argument("--partitionless-text", nargs=1, 
        help="Set the text to display for a device with no partitions. "
        "Default: {}".format(PARTITIONLESS_TEXT))
    parser.add_argument("--separator", nargs=1, 
        help="Set the separator between devices. "
        "Default: {}".format(SEPARATOR))
    parser.add_argument("--locked-indicator", nargs=1, 
        help="Set the indicator to use for a locked crypt device. "
        "Default: {}".format(LOCKED_INDICATOR))
    parser.add_argument("--unlocked-indicator", nargs=1, 
        help="Set the indicator to use for an unlocked crypt device. "
        "Default: {}".format(UNLOCKED_INDICATOR))
    parser.add_argument("--readonly-indicator", nargs=1, 
        help="Set the indicator to use for a readonly device. "
        "Default: {}".format(READONLY_INDICATOR))
    parser.add_argument("--truncate-fs-labels", type=int, nargs=1, 
        help="Trucate device labels to a certain number of characters, must be"
        "an integer."
        "Default: {}".format(TRUNCATE_FS_LABELS))
    parser.add_argument("-i", "--ignore", action="append", 
        help="Ignore a device by path. "
        "If path doesn't begin with / then it is assumed to be in /dev/")
    args = parser.parse_args()
    setParsedArgs(args)
    
def setParsedArgs(args):
    if args.info_text_color != None:
        global INFO_TEXT_COLOR
        INFO_TEXT_COLOR = args.info_text_color[0]
    if args.mounted_color != None:
        global MOUNTED_COLOR
        MOUNTED_COLOR = args.mounted_color[0]
    if args.plugged_color != None:
        global PLUGGED_COLOR
        PLUGGED_COLOR = args.plugged_color[0]
    if args.locked_color != None:
        global LOCKED_COLOR
        LOCKED_COLOR = args.locked_color[0]
    if args.unlocked_not_mounted_color != None:
        global UNLOCKED_NOT_MOUNTED_COLOR
        UNLOCKED_NOT_MOUNTED_COLOR = args.unlocked_not_mounted_color[0]
    if args.partitionless_color != None:
        global PARTITIONLESS_COLOR
        PARTITIONLESS_COLOR = args.partitionless_color[0]
    if args.partitionless_text != None:
        global PARTITIONLESS_TEXT
        PARTITIONLESS_TEXT = args.partitionless_text[0]
    if args.separator != None:
        global SEPARATOR
        SEPARATOR = args.separator[0]
    if args.locked_indicator != None:
        global LOCKED_INDICATOR
        LOCKED_INDICATOR = args.locked_indicator[0]
    if args.unlocked_indicator != None:
        global UNLOCKED_INDICATOR
        UNLOCKED_INDICATOR = args.unlocked_indicator[0]
    if args.readonly_indicator != None:
        global READONLY_INDICATOR
        READONLY_INDICATOR = args.readonly_indicator[0]
    if args.truncate_fs_labels != None:
        global TRUNCATE_FS_LABELS
        TRUNCATE_FS_LABELS = args.truncate_fs_labels[0]
    if args.ignore != None:
        args.ignore = list(map(lambda p: 
            p if p.startswith("/") else "/dev/{}".format(p), args.ignore))
        global fastIgnore
        oldFastIgnore = fastIgnore
        def newFastIgnore(path):
            return oldFastIgnore(path) or path in args.ignore
        fastIgnore = newFastIgnore

parseArguments()
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
