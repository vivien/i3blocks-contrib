# openvpn

Support multiple VPN, with colors.

# Usage

Add the following to your i3blocks config:

``` ini
[openvpn]
command=$SCRIPT_DIR/openvpn
interval=20
PID_FILE_FORMAT='/run/openvpn/*.pid'
```

Note: devices in configuration file should be named with their number (ex: tun0, tap1),
as dynamic devices are not supported.
Also make sure that your openvpn config filename ends in `.conf`.

# Options

```
Usage: openvpn [-p pid_file_format]
-p : format string to glob all pid files (default '/run/openvpn/*.pid')
```
