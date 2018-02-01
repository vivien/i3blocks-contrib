# aur-update

List available updates from the Arch User Repository (AUR)

![](example.png)

## Setup / Usage

Example i3blocks configuration:

```
[aur-update]
command=$SCRIPT_DIR/aur-update -u red -q -i root vidyodesktop
markup=pango
interval=43200 # 12h
signal=13
```

Right or middle click sends a notification (via notify-send) with a list of outdated packages
and the corresponding version information.

### Options

```
usage: aur-update [-h] [-u COLOR] [-q] [-i IGNORE [IGNORE ...]]

Check for AUR updates

optional arguments:
  -h, --help            show this help message and exit
  -u COLOR, --updates_available_color COLOR
                        color of the output, if updates are available
  -q, --quiet           Do not produce output when system is up to date
  -i IGNORE [IGNORE ...], --ignore IGNORE [IGNORE ...]
                        Ignore packages
```

## Dependencies

- python3 [requests library](http://docs.python-requests.org/en/master/)
- optional: libnotify/notify-send

