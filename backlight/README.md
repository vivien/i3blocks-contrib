# backlight

Show the screen brightness value given by `xbacklight`.
Clicking uses `xset` to turn off the backlight, scrolling increases or decreases
the brightness.

![](example.png)

## Setup / Usage

Example i3blocks configuration:

```
[backlight]
command=$SCRIPT_DIR/backlight
label=☀
interval=20
#STEP_SIZE=5
#USE_SUDO=0
```

- right click: turn off backlight
- scroll: increase/decrease the brightness in percentage steps according to `STEP_SIZE`

## Dependencies

These tools from the xorg-suite are needed:

- `xorg-xbacklight`
- `xorg-xset`

You need to allow the user to change the brightness (only if you want to use scrolling).
If you don't have the proper permissions, you will get an error like

```bash session
$ xbacklight -inc 5
/usr/bin/xbacklight: [Errno 13] Permission denied: '/sys/class/backlight/intel_backlight/brightness'
```

One option is to create a [udev rule](https://wiki.archlinux.org/index.php/Backlight#Udev_rule).

Another option is to allow the user to execute `xbacklight` without a password using the
[sudoers file](https://wiki.archlinux.org/index.php/Sudo#Configuration).
For the user `<user>` it would be something like

```
<user> ALL=(ALL) NOPASSWD: /usr/bin/xbacklight
```

Then use `USE_SUDO=1` in the configuration of this block.
