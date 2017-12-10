# temperature

Show system temperatures.

![](temperature.png)

# Dependencies

* `lm-sensors`

# Usage

The script may be called with `-w` and `-c` switches to specify 
thresholds, see the script for details.

# Installation

Add the following to your i3blocks config:

``` ini
[temperature]
command=$SCRIPT_DIR/temperature
label=TEMP
interval=10
```
