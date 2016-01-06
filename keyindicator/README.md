# Key indicators

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
