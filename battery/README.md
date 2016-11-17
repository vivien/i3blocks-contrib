## i3blocks-battery

An i3blocks blocklet script to output the current status of your battery.

Dependencies: fonts-font-awesome, acpi, python3

It looks like this:

![](images/full.png)

![](images/charging.png)

![](images/unplugged.png)

![](images/unknown.png)

![](images/nobattery.png)

To use with i3blocks, copy the blocklet configuration in the given `i3blocks.conf` into your i3blocks configuration file, the recommended config is

```INI
[battery]
command=$SCRIPT_DIR/battery.py
markup=pango
interval=30
```
