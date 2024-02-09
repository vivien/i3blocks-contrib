# mpris
Display the currently playing song/media from the MPRIS interface. Offers 
a persistent mode and it works with mouse controls. It also allows truncation
of long song/media titles.

![](mpris.png)

# Dependencies
It only requires [playerctl](https://github.com/acrisci/playerctl), dbus-monitor (should
be included by your distribution's dbus package or dbus-tools package), and standard UNIX shell
(bash isn't required, any `/bin/sh` will do, though bash works fine).

# Usage
Left click toggles play/pause, right click goes to the next song,
middle click goes to the previous song. Scrolling up/down will change 
the volume of the player.

It is recommended to use the script with the `SUBSCRIBE=1` option,
which will allow the script to automatically update whenever the
song/media changes. This option requires `interval=persist`.

# Config
```INI
[mpris]
command=$SCRIPT_DIR/mpris
## SUBSCRIBE=1 requires interval=persist
SUBSCRIBE=1
interval=persist
## if set, will truncate the string at a number of characters, adding a ... at the end
#ELLIPSE_LEN=60
#PAUSED_ICON=' '
#PLAYING_ICON=' '
#ARTIST_SEP=' - '
## amount to change volume by with scroll wheel
#STEP=0.01
```
