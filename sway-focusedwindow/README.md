# sway-focusedwindow

Displays title of focused window in [Sway WM](https://swaywm.org/)

![](sway-focusedwindow.png)

# Requirements

Dependencies: swaymsg (typically distributed along with sway), [jq](https://github.com/stedolan/jq)

# Installation

The recommended i3blocks config is

```INI
[sway-focusedwindow]
command=$SCRIPT_DIR/sway-focusedwindow
interval=persist
```
