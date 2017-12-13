# disk

Show disk usage. The directory defaults to $HOME if the instance is not
specified. The script may be called with an optional argument to set the
alert (defaults to 10 for 10%).
The script also accepts the flag `-n` to allow checking the disk usage of network devices, 
which is disabled by default.


# Config

```
[disk]
command=$SCRIPT_DIR/disk
label=HOME
#instance=/mnt/data
interval=30
```
