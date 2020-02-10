# cpu_util_detailed

Report detailed CPU utilization statistics.

Reports detailed CPU utilization as in man(1) mpstat, pango markup is used to distinguish values with colors, always prints total usage as short text. Written in bash and awk.

![block preview](cpu_util_detailed.png)

## Recommended:

 * **mpstat** - Usually a part of **sysstat** package. If `mpstat` command is not available, the script will fall back to reading '/proc/stat' and '/proc/utime' and doing its' own calculations, which consumes more CPU time.

 * **awk** - Chances are high you have it, should be under the same name in your distro's package repository. Not used in a fallback method.

## Required:

 * **bc** - Usually a part of the system core/base, should be under the same name in your distro's package repository.

## i3blocks config example:

```ini
[cpu_util_detailed]
command=$SCRIPT_DIR/cpu_util_detailed
label=CPU
markup=pango
interval=-2
#report_time=5
#stats=usr nice sys iowait
#format=%6.2f
#warn=80
#usr_color=green
#nice_color=yellow
#sys_color=red
#iowait_color=grey
#irq_color=purple
#soft_color=violet
#steal_color=orange
#guest_color=cyan
#gnice_color=blue
#idle_color=white
#total_color=white
```

**interval** must be set in i3blocks.conf, can be any, refer to [i3blocks README](https://github.com/vivien/i3blocks#interval).

**report_time** - time for gathering CPU statistics, refer to man(1) mpstat. If not set, determined based on **interval**: for 'repeat' and '-2' set to 5, for less or equal 2 set to 1, for more than 2 set to **interval** - 1. This can be used to determine blocklet refresh interval with **interval** set to 'repeat' or '-2'.

**stats** - a space separated list of stats to be displayed in the desired order. Names are as per man(1) mpstat -u option without a '%' symbol. Full list: usr nice sys iowait irq soft steal guest gnice idle total. Defailt is 'usr nice sys iowait'. You may want to add e.g. 'guest' if you're running virtual machines.

Colors of relevant stats:

**usr_color** must be a [pango markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html) compliant color value. Default is 'green'.

**nice_color** must be a [pango markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html) compliant color value. Default is 'yellow'.

**sys_color** must be a [pango markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html) compliant color value. Default is 'red'.

**iowait_color** must be a [pango markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html) compliant color value. Default is 'grey'.

**irq_color** must be a [pango markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html) compliant color value. Default is 'purple'.

**soft_color** must be a [pango markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html) compliant color value. Default is 'violet'.

**steal_color** must be a [pango markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html) compliant color value. Default is 'orange'.

**guest_color** must be a [pango markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html) compliant color value. Default is 'cyan'.

**gnice_color** must be a [pango markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html) compliant color value. Default is 'blue'.

**idle_color** must be a [pango markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html) compliant color value. Default is 'white'.

**total_color** must be a [pango markup](https://developer.gnome.org/pygtk/stable/pango-markup-language.html) compliant color value. Default is 'white'.

**format** - a format string for `printf`, example values: 

 - '%6.2f' (default) will display every stat as `' 12.34'`

 - '%5.1f' will display every stat as `' 12.3'`

 - ':%5.2f' will display every stat as `':12.34'`

**warn** - warning threshold, when reached urgent flag is set, default is '80'.

## WARNING
No sanity checks for values set in i3blocks.conf are made inside the script.
