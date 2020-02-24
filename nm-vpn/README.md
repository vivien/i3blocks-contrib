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

`nm-vpn` gets active connection info from `nmcli`, looks for interface type `tun`, `tap`, `vpn`. A VPN connection is treated as established only when `tun`|`tap` is present, when it's not and a `vpn` connection is listed as active it is treated as initializing.

# Tunables

`init_color` - color used for marking a connection in initializing state, default is '#FFFF00'

`on_color` - color used for marking a connection in established state, default is '#00FF00'

## Output

When `tun`|`tap` is active, `nm-vpn` will print in the following form:
  - Full: `VPN Name`
  - Short: `ON`
  - Color will be set to `on_color` value

When `tun`|`tap` in not active, `nm-vpn` will print in the following form:
  - Full: `VPN Name`
  - Short: `INIT`
  - Color will be set to `init_color` value

# Config

``` ini
[nm-vpn]
#init_color=#FFFF00
#on_color=#00FF00
label=VPN: 
interval=5
```
