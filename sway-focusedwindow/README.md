# sway-focusedwindow

Displays title of focused window in [Sway WM](https://swaywm.org/)

![](sway-focusedwindow.png)

# Requirements

Dependencies: swaymsg (typically distributed along with sway), [jq](https://github.com/stedolan/jq)

# Command line arguments  

```bash
sway-focusedwindow [maxlen [alignment]]
```

First argument is maximum line length. `0` means unlimited length, i.e. output line can occupy all available space.  
Default value: `0`.  

Second argument is alignment. If output line length is lesser than maximum line length, then it will be aligned.  
Possible values: `left`, `right`, `center`.  
Default value: `center`.

# Installation

The recommended i3blocks config is

```INI
[sway-focusedwindow]
command=$SCRIPT_DIR/sway-focusedwindow 200 center
interval=persist
```
