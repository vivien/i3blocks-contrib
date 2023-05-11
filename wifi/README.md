# wifi

Show the strength of your wifi connection.
If no instance is specified, wlan0 is used.

Dependency: iw

![](wifi.png)

# Config

```
[wifi]
command=$SCRIPT_DIR/wifi
label=wifi:
#INTERFACE=wlan0
interval=60
```
