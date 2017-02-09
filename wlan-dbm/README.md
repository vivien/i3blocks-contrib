# wlan-dbm

Show wifi interface link quality in dBm or percent.

![](wlan-dbm.png)

# Usage

The desired interface to monitor can be specified in the usual `block_instance` directive.
If it's missing, the script will fallback to `wlan0`.
The block uses dBm by default, but you may pass a `-p` flag to the script
to use percent.
Note, however, that percent is just an estimate that may not accurately predict
whether you have a good signal.

# Dependencies

* `iw`

# Config

    [wlan-dbm]
    command=$SCRIPT_DIR/wlan-dbm
    instance=wlan0
