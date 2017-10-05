# time

Show the current time and changes displayed timezone on click.

![](time.png)

# Dependencies

perl

# Installation

To use with i3blocks, copy the below configuration into your i3blocks configuration file

```INI
[time]
instance=%Y-%m-%d %H:%M
command=$SCRIPT_DIR/time [/path/to/tz/file]
interval=1
```

Instance is an optional time format string. See [strftime](https://linux.die.net/man/3/strftime).

# Configuration

In the script there are two hashes that control the timezones used and the way they are displayed.

This hash defines the timezones that are switched to when clicking (ie. clicking when displaying Europe/London switches to Brazil/East)
```perl
my %tzmap = (
	""                   => "Europe/London",
	"Europe/London"      => "Brazil/East",
	"Brazil/East"        => "Australia/Brisbane",
	"Australia/Brisbane" => "Asia/Calcutta",
	"Asia/Calcutta"      => "Europe/London",
);
```

This hash defines how each timezone should be displayed (ie. Europe/London displays as "UK")
```perl
my %display_map = (
	"Europe/London"      => "UK",
	"Brazil/East"        => "Brazil",
	"Australia/Brisbane" => "AU",
	"Asia/Calcutta"      => "Hyderabad",
);
```
