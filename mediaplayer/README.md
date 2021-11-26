# mediaplayer

Generic media player status/controls.

![Example screenshot](mediaplayer.png)

This displays "ARTIST - SONG" if music is playing. By
left-clicking/right-clicking the displayed text, it will play the previous/next
song. Middle-clicking will pause/unpause the song.

Supported players are:
- spotify, vlc, audacious, xmms2, mplayer and others that
use MPRIS DBus Interface Specification
- mpd
- cmus
- rhythmbox

mpd is supported through mpc (music player client).

For MPRIS support you need to have the playerctl binary in your path.
See: https://github.com/acrisci/playerctl

If you leave the instance empty playerctl will try to find an
active MPRIS-compatible player on its own.

# Installation

Add the following to your i3blocks config:

``` ini
[mediaplayer]
command=$SCRIPT_DIR/mediaplayer
instance=spotify
interval=5
signal=10
```
