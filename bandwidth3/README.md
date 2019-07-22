# bandwidth3

Monitor bandwidth usage.

![](bandwidth3.png)

# Usage

```
[bandwidth3]
command=$SCRIPT_DIR/bandwidth3
interval=persist
markup=pango
#LABEL=<span font='FontAwesome'>  </span>
#IFACE=[automatically determined]
#DT=3
#UNIT=Mb
# Exposed variables: rx, wx, tx, unit, iface
#PRINTF_COMMAND=printf "${LABEL}%-5.1f/%5.1f %s/s\n", rx, wx, unit;
```

Note that the interface will be guessed using `ip route` but it can also be specified 
using the `$IFACE` property.
On the fly interface switching is not supported, if you change
your default interface, simply issue `i3-msg restart` and the script will pick
up on the new default. However, the block will wait until a default interface
is found upon starting, so no restart is needed if you start i3 and then connect 
to wifi later.
