# nm-vpn

Parses output from `nmcli` to show the current connected VPN name/status

![](images/full.png)

![](images/short.png)

# Requirements

  - NetworkManager/`nmcli`
  - `sh`
  - `awk`
    - tested on nawk, gawk, mawk, [goawk](https://github.com/benhoyt/goawk), Plan 9 awk and busybox awk.

# Usage

`nm-vpn` gets active connection info from `nmcli` for interface `tun0`.
A VPN connection in NetworkManager is established only when `tun0` is
active, thus the blocklet’s response time depends on how long it takes
to connect.

## Output

When `tun0` is active, `nm-vpn` will print in the following form:
  - Full: `VPN: "Name"`
  - Short: `ON`

In addition, each form will be coloured green (“\#00FF00”).

# Config

``` ini
[nm-vpn]
label=VPN:
interval=5
```
