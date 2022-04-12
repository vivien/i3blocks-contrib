# volume-pulseaudio

Display the system volume and
optionally the default playback device and index.
Offers controls for these via clicks/scrolling.
Supports changing audiostreams that are already playing.

![](volume-pulseaudio-high.png)
![](volume-pulseaudio-med.png)
![](volume-pulseaudio-low.png)
![](volume-pulseaudio-mute.png)

# Dependencies

pulseaudio, alsa (alsa-utils package), fontawesome (fonts-font-awesome package) for the speaker symbols

# Usage

Left/right clicks change default playback device, middle click mutes, scrolling
adjusts volume. If your keyboard has audio buttons, it is suggested to add the
the following to your i3 config

```
# change volume or toggle mute
bindsym XF86AudioRaiseVolume exec amixer -q -D pulse sset Master 5%+ && pkill -RTMIN+1 i3blocks
bindsym XF86AudioLowerVolume exec amixer -q -D pulse sset Master 5%- && pkill -RTMIN+1 i3blocks
bindsym XF86AudioMute exec amixer -q -D pulse sset Master toggle && pkill -RTMIN+1 i3blocks
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
[volume-pulseaudio]
command=$SCRIPT_DIR/volume-pulseaudio
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
