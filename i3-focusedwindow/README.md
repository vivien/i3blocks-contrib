# i3 Focused window

Displays title of focused window in i3Wm

![Demo](i3-focusedwindow.png)

# Requirements

Dependencies: `xdotool`

# Command line arguments  

```bash
i3-focusedwindow -class or --classname # for classname
i3-focusedwindow -title or --titlename # for titlename
i3-focusedwindow -win or --windowname # for windowname
i3-focusedwindow -dim or --dimensions # for dimensions
```

# Installation

The recommended i3blocks config is

```INI
[i3-focused-window]
command=$SCRIPT_DIR/custom/i3-focused-window -class
interval=1
```
