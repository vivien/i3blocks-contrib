# wlan-dbm

Show an interface link quality in dBm.

![](wlan-dbm.png)

# Usage

The desired interface to monitor can be specified in the usual `block_instance` directive.
If it's missing, the script will fallback to `wlan0`.

# Dependencies

* `iw`

# Usage example

    [wlan-dbm]
    command=/usr/lib/i3blocks/wlan-dbm/wlan-dbm
    instance=wlan0
