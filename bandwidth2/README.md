# bandwidth2

Monitor bandwidth usage.
This is a C version of the bandwidth blocklet.

![](bandwidth2.png)

It comes with some other features though:
* Automatically estimate what unit (K,M,G,T) to use depending on the value. You can still choose between bits and bytes.
* By default sum all the network interfaces (except lo) instead of only default route interface.
* Warning and critical colors as an option.

## Build

```
make
```

### Example Blocklet
```ini
[bandwidth]
label=
command=$SCRIPT_DIR/bandwidth2 -w 307200:30720 -c 512000:51200
interval=persist
markup=pango
```

## Options

```
Usage: ./bandwidth2 [-b|B] [-t seconds] [-i interface] [-w Bytes:Bytes] [-c Bytes:Bytes] [-h]

-b              use bits/s
-B              use Bytes/s  (default)
-t seconds      refresh time (default is 1)
-i interface    network interface to monitor. If not specified, check all interfaces.
-w Bytes:Bytes  Set warning (color orange) for Rx:Tx bandwidth. (default: none)
-c Bytes:Bytes  Set critical (color red) for Rx:Tx bandwidth. (default: none)
-h              this help

```
