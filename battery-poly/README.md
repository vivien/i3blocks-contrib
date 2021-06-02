# battery-poly
Generates a pretty battery string for multi-battery systems. Based on [cogitantium/poly-battery-status-py](https://github.com/cogitantium/poly-battery-status-py). Licensed under GPLv3.

![](battery-poly.png)

## Features
- Uses sysfs for gathering batteries and values on these
- Calculates time-to-depleted and time-to-full from current power-draw
- Takes battery-thresholds, such as [TLP](https://github.com/linrunner/TLP), into account when calculating time-to-**full**. Defaults to 100% but is overrideable through arguments.
- Omits time-to-* when passive (specifically when sysfs delivers a status of `Unknown` or `Full`)
- Takes a Python formatting string for percentage. Default is `.2%` rendering a percentage with two decimals.

## Dependencies
- python3
- sysfs (provided by Linux kernel since 2.5)

## Config
```
[battery-poly]
command=$SCRIPT_DIR/battery-poly
LABEL=BAT
interval=5
```

Two positional arguments are supported; battery-threshold as float and percentage formatting as Python formatting string.

To configure battery-poly for a battery-threshold of 42%, edit the `command`-line as such:
```
[battery-poly]
command=$SCRIPT_DIR/battery-poly 0.42
```

If no decimals are desired for the percentage and battery-threshold is not to be changed, simply put the default value as follows:
```
[battery-poly]
command=$SCRIPT_DIR/battery-poly 1.0 .0%
```  