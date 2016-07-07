# monitor_manager

Quickly manage your monitors. 
This script supports: on/off, blank/unblank,
extend, clone, set primary, change output mode.

![](monitor_manager.png)

# Dependencies

python3, python3-tk, xrandr, fontawesome (fonts-font-awesome package), arandr suggested but not required.

# Usage

`i3blocks.conf`

```
[monitors]
command=$SCRIPT_DIR/monitor_manager.py
interval=once
```

There are also some options that can be tinkered with at the top of the file.
