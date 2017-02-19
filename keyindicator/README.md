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
instance=CAPS
markup=pango
interval=once
signal=11
 
[keyindicator]
command=$SCRIPT_DIR/keyindicator
instance=NUM
markup=pango
interval=once
signal=11
```

# Options

```
Usage: keyindicator [-c <color on>] [-C <color off>] [-b <bg color on>] [-B <bg color off>] [--hide]
  -c <color on>: hex color to use when indicator is on
  -C <color off>: hex color to use when indicator is off
  -b <background color on>: hex color to use when indicator is on
  -B <background color off>: hex color to use when indicator is off
  --hide: don't output anything when indicator is off

Note: environment variable $BLOCK_INSTANCE should be one of:
  CAPS, NUM (default is CAPS).
```
