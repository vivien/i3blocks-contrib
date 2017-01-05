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
interval=once
signal=11
 
[keyindicator]
command=$SCRIPT_DIR/keyindicator
instance=NUM
interval=once
signal=11
```

If you would rather the indicator hide itself when the status is off:

``` ini
command=$SCRIPT_DIR/keyindicator --hide
```
