# ytdl-mpv

Play youtube videos (any video compatible with youtube-dl) from your clipboard. 
Left click for video, middle click for audio, right click to kill all instances of mpv.

![](ytdl-mpv.png)

# Requirements

Dependencies: fonts-font-awesome, mpv, xclip, youtube-dl, perl, Data::Validate::URI perl module
(libdata-validate-uri-perl package)

# Installation

The recommended i3blocks config is

```INI
[ytdl-mpv]
command=$SCRIPT_DIR/ytdl-mpv
markup=pango
interval=once
signal=4
#CACHE_DEFAULT=1048576
#PLAYING_COLOR=red
#NOT_PLAYING_COLOR=white
```

Copy a youtube URL into your clipboard and then click on the blocklet to make sure everything works.
