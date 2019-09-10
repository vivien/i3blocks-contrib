# wifi

Show the strength of your wifi connection.
If no instance is specified, wlan0 is used.
If $QUIET is set to true, supress the output rather than displaying "down"

![](wifi.png)

# Config

```
[wifi]
command=$SCRIPT_DIR/wifi
label=wifi:
#INTERFACE=wlan0
#QUIET=true
interval=60
```
