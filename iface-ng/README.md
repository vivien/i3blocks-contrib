# iface-ng

Display information about network interfaces, more flexible than default `iface`.

``` ini
[iface-ng]
command=./iface-ng -psd ''
label=eth0:
instance=eth0
interval=10
```

## Usage

    Usage: iface-ng [-d down] [-n "no ip"] [-c FF0000] [-C 00FF00] [-e] [-p] [-s] [-6]
        -d down: Placeholder text if the specified interface is down. If set to an empty string,
           the entire block is hidden (useful to save space on small screens).
        -n "no ip": Placeholder text to display when the interface is up but it does not
           have any ip address yet.
        -c FF0000: Text color when interface is down.
        -C 00FF00: Text color when interface is up.
        -e: Show interface even if it does not exist (useful for tun/tap).
        -p: Include CIDR prefix.
        -s: Include link speed (ethernet only).
        -6: Use ipv6 address insead of v4.
