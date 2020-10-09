# aur-update

List available updates from the Arch User Repository (AUR)

![](example.png)

## Setup / Usage

Example i3blocks configuration:

```
[aur-update]
command=$SCRIPT_DIR/aur-update
markup=pango
format=json
interval=43200
UPDATE_COLOR=red
QUIET=1
IGNORE=root vidyodesktop
#CACHE_UPDATES=0
```

Right or middle click sends a notification (via notify-send) with a list of outdated packages
and the corresponding version information.
If you enable caching (`CACHE_UPDATES=1`), the update list will be cached as an environment variable.
This will be read on a (right/middle) click to directly show the notification without the delay caused by updating the list.


## Dependencies

- python3 [requests library](http://docs.python-requests.org/en/master/)
- optional: libnotify/notify-send

