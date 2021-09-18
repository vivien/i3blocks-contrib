# Before using this block

This is a fork of the block volume-pulseaudio, that supports pipewire,
pulseaudio, and alsa. This is achieved by using the tool pactl instead of pacmd.
So hopefuly this should be the future of this block.

# volume-pipewire

Display the system volume and
optionally the default playback device and indeax.
Offers controls for these via clicks/scrolling.
Supports changing audiostreams that are already playing.

![](volume-pipewire-high.png)
![](volume-pipewire-med.png)
![](volume-pipewire-low.png)
![](volume-pipewire-mute.png)

# Dependencies

pipewire-pulse, pipewire-alsa, pipewire-jack, alsa-utils, fontawesome (fonts-font-awesome package) for the speaker symbols

# Usage

Left/right clicks change default playback device, middle click mutes, scrolling
adjusts volume. If your keyboard has audio buttons, it is suggested to add the
the following to your i3 config

```
# Pipewire-pulse
bindsym XF86AudioMute $exec pactl set-sink-mute 0 toggle
bindsym XF86AudioLowerVolume $exec pactl set-sink-volume 0 -5%
bindsym XF86AudioRaiseVolume $exec pactl set-sink-volume 0 +5%

# Media player controls
bindsym XF86AudioPlay $exec playerctl play-pause
bindsym XF86AudioPause $exec playerctl play-pause
bindsym XF86AudioNext $exec playerctl next
bindsym XF86AudioPrev $exec playerctl previous
```

where the number `1` in `-RTMIN+1` can be replaced to another signal number,
as long as it agrees what you put for `signal=` in your i3blocks config.
The previous lines also assume your mixer is "pulse" and your scontrol is "Master".
If yours are different, change them appropriately.

Alternatively to using signals, you may use the `SUBSCRIBE=1` option in your config in order to have the block
automatically respond to audio change events. This option requires `interval=persist`
and always uses the `LONG_FORMAT`.

# Config

```INI
[volume-pipewire]
command=$SCRIPT_DIR/volume-pipewire
interval=once
signal=1
#MIXER=[determined automatically]
#SCONTROL=[determined automatically]
##exposed format variables: ${SYMB}, ${VOL}, ${INDEX}, ${NAME}
#LONG_FORMAT="${SYMB} ${VOL}% [${INDEX}:${NAME}]"
#SHORT_FORMAT="${SYMB} ${VOL}% [${INDEX}]"
#AUDIO_HIGH_SYMBOL='  '
#AUDIO_MED_THRESH=50
#AUDIO_MED_SYMBOL='  '
#AUDIO_LOW_THRESH=0
#AUDIO_LOW_SYMBOL='  '
#AUDIO_DELTA=5
#DEFAULT_COLOR="#ffffff"
#MUTED_COLOR="#a0a0a0"
#USE_ALSA_NAME=0
#USE_DESCRIPTION=0
## SUBSCRIBE=1 requires interval=persist and always uses LONG_FORMAT
#SUBSCRIBE=0
```
