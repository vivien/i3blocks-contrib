# iface

Show network interface status.
If the instance is not specified, it uses the interface for the default route.
The address can be forced to IPv4 or IPv6 with -4 or -6 switches.

![](iface-up.png)
![](iface-down.png)

# Config

```
[iface]
command=$SCRIPT_DIR/iface
#label=wlan0:
#instance=wlan0
color=#00FF00
interval=10
```
