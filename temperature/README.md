# temperature

Show system temperatures.

![](temperature.png)

# Dependencies

* `lm-sensors`

# Usage

``` ini
[temperature]
command=$SCRIPT_DIR/temperature
label=TEMP
interval=10
#T_WARN=70
#T_CRIT=90
#SENSOR_CHIP=""
```
