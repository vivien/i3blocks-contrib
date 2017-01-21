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

To use with i3blocks, put `usb` somewhere convenient.
We will assume it is at `$SCRIPT_DIR/usb`.
Copy the blocklet configuration in the given `i3blocks.conf` into your 
i3blocks configuration file.
The recommended i3blocks config is

```INI
[usb]
command=$SCRIPT_DIR/usb
markup=pango
signal=1
interval=10
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

Configuration can be done either by editing the top portion of `usb`, or by
specifying command line flags. 
Run with `--help` for more information.
You will find several options that you can configure.
Probably the most useful to you will be the `-i` (ignore) flag or the `ignore` 
and `fastIgnore` functions in `usb`.
These allow you to ignore devices, e.g. those that are always plugged in.
The `-i` flag can be specified multiple times and if a device does not begin 
with "/" it is assumed to be in /dev/.
E.g.
`command=$SCRIPT_DIR/usb -i sda1 -i sda2 -i mapper/sda6_crypt`
will ignore /dev/sda1, /dev/sda2, and /dev/mapper/sda6_crypt.
If you decide not to install FontAwesome, 
then you will probably want to change the `LOCKED_INDICATOR` and 
`UNLOCKED_INDICATOR` variables, as these use unicode symbols provided by 
FontAwesome (and not many other fonts).
You do not need to restart i3 after making a change to the config.

# Bugs

Please report bugs and suggestions to the issues page.
Contributions are always welcome.
A common way a bug will manifest is that you will get no output in your bar.
If this happens, try running `python3 $SCRIPT_DIR/usb` from the command 
line to get some insight into why nothing is displayed.
You will probably see a python stack trace.
Make sure to include this in your bug report, along with the output of any 
other commands that you may think are relevant (the stack trace may contain 
the exact system call that failed).
