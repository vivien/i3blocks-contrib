# miccontrol

Shows the status of you microphone. Left and right click toggles mute.

![](screenshot1.png) ![](screenshot2.png)

# Usage

This block can be run on an interval or by signal. To run the block using a
signal, it is recommended to add the following to your i3 config.

```
# toggle mute
bindsym XF86AudioMicMute exec --no-startup-id pactl set-source-mute "alsa_input.pci-0000_00_1f.3.analog-stereo" toggle && pkill -RTMIN+10 i3blocks
```
where the `alsa_input.pci-0000_00_1f.3.analog-stereo` after `set-source-mute` can be changed to another source name
and `10` in `-RTMIN+10` can be replaced to another signal number,
as long as it agrees what you put for `signal=` in your i3blocks config.

# Config

```
[miccontrol]
command=$SCRIPT_DIR/miccontrol
#label=MIC
SOURCE=alsa_input.pci-0000_00_1f.3.analog-stereo
interval=10
signal=10
```

