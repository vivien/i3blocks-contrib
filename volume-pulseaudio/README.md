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
bindsym XF86AudioMute exec amixer -q -D pulse sset Master toggle && pkill -RTMIN+1 i3blocks
```

where the number `1` in `-RTMIN+1` can be replaced to another signal number,
as long as it agrees what you put for `signal=` in your i3blocks config.
The previous lines also assume your mixer is "pulse" and your scontrol is "Master".
If yours are different, change them appropriately.

# Known bug

The script tries its best to guess your mixer and scontrol variables, which are needed for
scrolling up/down and muting with middle click to work.
However, there are an unknown number of edge cases and no known way to account for all of them. 
Therefore, the `-m` and `-s`flags are provided to specify them manually. 
In almost all cases, one of the following two will work

- `-m default -s Master`
- `-m pulse -s Master`

If neither of these works for you, try using `alsamixer`, `amixer`, and `amixer info` to guide your guesses,
and let us know what turned out to work.

# Options

```
Usage: volume-pulseaudio [-S] [-F format] [-f format] [-p] [-a|-d] [-H symb] [-M symb]
        [-L symb] [-X symb] [-T thresh] [-t thresh] [-C color] [-c color] [-i inter] 
        [-m mixer] [-s scontrol] [-h]
Options:
-F, -f	Output format (-F long format, -f short format) to use, amongst:
	0	 symb vol [index:name]	 (default long)
	1	 symb vol [name]
	2	 symb vol [index]	 (default short)
	3	 symb vol
-S	Subscribe to volume events (requires persistent block, always uses long format)
-p	Omit the percent sign (%) in volume
-a	Use ALSA name if possible
-d	Use device description instead of name if possible
-H	Symbol to use when audio level is high. Default: '  '
-M	Symbol to use when audio level is medium. Default: '  '
-L	Symbol to use when audio level is low. Default: '  '
-X	Symbol to use when audio is muted. Default: '  '
-T	Threshold for medium audio level. Default: 50
-t	Threshold for low audio level. Default: 0
-C	Color for non-muted audio. Default: #ffffff
-c	Color for muted audio. Default: #a0a0a0
-i	Interval size of volume increase/decrease. Default: 5
-m	Use the given mixer.
-s	Use the given scontrol.
-h	Show this help text
```
