# volume-pulseaudio

Display the system volume and
optionally the default playback device and index.
Offers controls for these via clicks.

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
bindsym XF86AudioMute exec amixer -q -D pulse sset Master toggle && pkill -RTMIN+1
```

where the number `1` in `-RTMIN+1` can be replaced to another signal number,
as long as it agrees what you put for `signal=` in your i3blocks config.

# Options

```
Usage: volume-pulseaudio [-S] [-F format] [-f format] [-p] [-a] [-H symb] [-M symb]
        [-L symb] [-X symb] [-T thresh] [-t thresh] [-C color] [-c color] [-h]
Options:
-F, -f	Output format (-F long format, -f short format) to use, amonst:
	0	 symb vol [index:name]	 (default long)
	1	 symb vol [name]
	2	 symb vol [index]	 (default short)
	3	 symb vol
-S  Subscribe to volume events (requires persistent block, always uses long format)
-p	Omit the percent sign (%) in volume
-a	Use ALSA name if possible
-H	Symbol to use when audio level is high. Default: '  '
-M	Symbol to use when audio level is medium. Default: '  '
-L	Symbol to use when audio level is low. Default: '  '
-X	Symbol to use when audio is muted. Default: '  '
-T	Threshold for medium audio level. Default: 50
-t	Threshold for low audio level. Default: 0
-C	Color for non-muted audio. Default: #ffffff
-c	Color for muted audio. Default: #a0a0a0
-h	Show this help text
```
