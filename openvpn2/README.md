# openvpn

Support OpenVPN (require nmcli binary)

# Usage

Add the following to your i3blocks config:

``` ini
[openvpn]
command=$SCRIPT_DIR/openvpn
interval=20
```

Note: devices in configuration file should be named with their number (ex: tun0, tap1),
as dynamic devices are not supported.
