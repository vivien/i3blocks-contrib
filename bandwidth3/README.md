# bandwidth3

Monitor bandwidth usage.

![](bandwidth3.png)

# Usage

```
[bandwidth3]
command=$SCRIPT_DIR/bandwidth3
interval=persist
markup=pango
#IFACE=[automatically determined]
#DT=3
#UNIT=Mb
# Exposed variables: rx, wx, tx, unit, iface
#PRINTF_COMMAND=printf "<span font='FontAwesome'>  </span>%-5.1f/%5.1f %s/s\n", rx, wx, unit;
```

Note that the interface will be guessed using `ip route` but it can also be specified 
using the `$IFACE` property.
If you would like on the fly interface switching, pass `-a` or set `$AUTORELOAD` to 1.
Even without AUTORELOAD, the block will wait until a default interface is found upon
starting, so no restart is needed if you start i3 and then connect to wifi later.
