# mediaplayer

Generic media player status/controls.

![Example screenshot](mediaplayer.png)

This displays "ARTIST - SONG" if music is playing. By
left-clicking/right-clicking the displayed text, it will play the previous/next
song. Middle-clicking will pause/unpause the song.

Any player supporting the MPRIS DBus Interface Specification is supported.
Note you may need to install or enable a plugin for this.

You also need to have the playerctl binary in your path.
See: https://github.com/acrisci/playerctl

If you leave the instance empty playerctl will try to find an
active MPRIS-compatible player on its own.

# Installation

Add the following to your i3blocks config:

``` ini
[mediaplayer]
command=$SCRIPT_DIR/mediaplayer
instance=spotify
interval=persist
```
