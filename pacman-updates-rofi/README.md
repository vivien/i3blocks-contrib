#  pacman-updates-rofi

Show the number of available updates for pacman, and display them in a small menu when left-clicking.
Update the machine with a right-click.

![](avail.png)

![](number.png)

# Dependencies

fonts-font-awesome, rofi, gksu

# Installation

To use with i3blocks, copy the blocklet configuration in the given `i3blocks.conf` into your i3blocks configuration file, the recommended config is

```INI
[pacman-updates-rofi]
command=$SCRIPT_DIR/pacman-updates-rofi
markup=pango
interval=3600
label=
```
