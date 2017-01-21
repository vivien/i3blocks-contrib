# monitor_manager

Quickly manage your monitors. 
This script supports: on/off, blank/unblank,
extend, clone, set primary, change output mode,
rotate, reflect, adjust brightness.

![](monitor_manager.png)

# Dependencies

python3, python3-tk, xrandr, fontawesome (fonts-font-awesome package), arandr suggested but not required.

# Usage

Add the following to your i3blocks config:

```
[monitors]
command=$SCRIPT_DIR/monitor_manager
interval=once
```

There are also some options that can be tinkered with at the top of the file.
The `SHOW_*` variables can be set to `False` in order to hide those components.
E.g. if you don't care about reflection, set `SHOW_REFLECTION = False` and the
button for reflection will not appear.
