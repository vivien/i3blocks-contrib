# iface

Show network interface status.
If the instance is not specified, it uses the interface for the default route.
To display the label of the default interface, pass the -L switch.

The address can be forced to IPv4 or IPv6 with -4 or -6 switches.

If an invalid interface is specified, nothing is printed.


![](iface-up.png)
![](iface-down.png)

# Config

```
[iface]
command=$SCRIPT_DIR/iface
#label=wlan0:
#IFACE=wlan0
color=#00FF00
interval=10
```
