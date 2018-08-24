# usb

Output connected usb storage device info.
Supports usb mass storage devices, including those with multiple partitions,
including LUKS partitions.

![](images/1.png)

![](images/2.png)

![](images/3.png)

![](images/4.png)


# Requirements

Dependencies: udev, python3, util-linux ( >= 2.23 )

Suggested: fonts-font-awesome

# Installation
The recommended i3blocks config is

```INI
[usb]
command=$SCRIPT_DIR/usb
markup=pango
signal=1
interval=10
#IGNORE_LIST=[]
#IGNORE_LIST=["sdd1", "mapper/sda1_crypt"]
#INFO_TEXT_COLOR=white
#MOUNTED_COLOR=green
#PLUGGED_COLOR=gray
#LOCKED_COLOR=gray
#UNLOCKED_NOT_MOUNTED_COLOR=yellow
#PARTITIONLESS_COLOR=red
#PARTITIONLESS_TEXT=no partitions
#SEPARATOR=<span color='gray'> | </span>
#LOCKED_INDICATOR= 
#UNLOCKED_INDICATOR= 
#READONLY_INDICATOR=ro
#TRUNCATE_FS_LABELS=[not set by default, accepts +/- integers]
```

To update the blocklet on plug/unplug device events you can add                 

    SUBSYSTEMS=="usb", RUN+="/usr/bin/pkill -RTMIN+1 i3blocks" 

in `/etc/udev/rules.d/70-persistent-usb.rules`.
You may need to create the file.
Then call

```ShellSession
sudo udevadm control --reload-rules
```

to activate the new rules.
If you do not care about updating the blocklet on plug/unplug, 
the script works fine on just an interval and you can ignore the udev rule and 
delete `signal=1` in the config.

Now restart your i3 in place with

```ShellSession
i3-msg restart
```

Try plugging in a usb device to make sure everything works.

# Configuration

The IGNORE_LIST variable, if set, must be a valid python representation of
a list of strings, e.g. `["sdd1", "mapper/sda1_crypt"]`.
Due to the way i3blocks parses config files, newlines are not allowed.
The strings are full device paths, with "/dev" optionally omitted.
For example, the previous "sdd1" is expanded to "/dev/sdd1" at runtime.
The list is safely parsed using ast.literal_eval, NOT eval.

If you decide not to install FontAwesome, 
then you will probably want to change the `LOCKED_INDICATOR` and 
`UNLOCKED_INDICATOR` variables, as these use unicode symbols provided by 
FontAwesome (and not many other fonts).
You do not need to restart i3 after making a change to the config.
