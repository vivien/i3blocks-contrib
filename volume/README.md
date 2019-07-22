# volume

Shows the current system volume. The first parameter sets the step (and units
to display). The second parameter overrides the mixer selection.
See the script for details.

Scrolling on the block changes the volume. Right clicking toggles mute.

![](volume.png)

# Usage

This block can be run on an interval or by signal. To run the block using a
signal, it is recommended to add the following to your i3 config.

```
# change volume or toggle mute
bindsym XF86AudioRaiseVolume exec amixer -q -D pulse sset Master 5%+ && pkill -RTMIN+10 i3blocks 
bindsym XF86AudioLowerVolume exec amixer -q -D pulse sset Master 5%- && pkill -RTMIN+10 i3blocks
bindsym XF86AudioMute exec amixer -q -D pulse sset Master toggle && pkill -RTMIN+10 i3blocks
```

where the number `10` in `-RTMIN+10` can be replaced to another signal number,
as long as it agrees what you put for `signal=` in your i3blocks config.


# Config

```
[volume]
command=$SCRIPT_DIR/volume
#LABEL=♪ 
LABEL=VOL 
interval=once
signal=10
#STEP=5%
#MIXER=[determined automatically]
#SCONTROL=[determined automatically]
```
For PulseAudio users, MIXER is usually "pulse" or "default".
For Jack/Jack2 users, MIXER is usually "jackplug".
For ALSA users, use "default" for your primary card, or "hw:#" 
where # is the number of the card desired.

For a list of available SCONTROL options, use `amixer -D $MIXER scontrols`.
