# keyindicator

Show the status of capslock or numlock.

![](keyindicator-active.png)

![](keyindicator-inactive.png)

# Installation

Add the following bindings to i3 config file:

```
bindsym --release Caps_Lock exec pkill -SIGRTMIN+11 i3blocks
bindsym --release Num_Lock  exec pkill -SIGRTMIN+11 i3blocks
```

Use the following in your i3blocks config file:

``` ini
[keyindicator]
command=$SCRIPT_DIR/keyindicator
#Allowed keys are CAPS and NUM
KEY=CAPS
markup=pango
interval=once
signal=11
#COLOR_ON=#00FF00
#COLOR_OFF=#222222
#BG_COLOR_ON=
#BG_COLOR_OFF=
 
[keyindicator]
command=$SCRIPT_DIR/keyindicator
KEY=NUM
markup=pango
interval=once
signal=11
#COLOR_ON=#00FF00
HIDE_WHEN_OFF=1
```

# Options

```
Usage: keyindicator [-c <color on>] [-C <color off>] [-b <bg color on>] [-B <bg color off>] [--hide]
  -c <color on>: hex color to use when indicator is on
  -C <color off>: hex color to use when indicator is off
  -b <background color on>: hex color to use when indicator is on
  -B <background color off>: hex color to use when indicator is off
  --hide: don't output anything when indicator is off

```
