# aur-update

List available updates from the Arch User Repository (AUR)

![](example.png)

## Setup / Usage

Example i3blocks configuration:

```
[aur-update]
command=$SCRIPT_DIR/aur-update
markup=pango
interval=43200
UPDATE_COLOR=red
QUIET=1
IGNORE=root vidyodesktop
```

Right or middle click sends a notification (via notify-send) with a list of outdated packages
and the corresponding version information.


## Dependencies

- python3 [requests library](http://docs.python-requests.org/en/master/)
- optional: libnotify/notify-send

