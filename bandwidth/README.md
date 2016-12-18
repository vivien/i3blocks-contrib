# bandwidth

Monitor bandwidth usage.

![](bandwidth.png)

# Usage

The default configuration uses

```
printf "<span font='FontAwesome'>  </span>%-5.1f/%5.1f %s/s\n", rx, wx, unit;
```

as the default print command. The `%-5.1f` and `%5.1f` indicate that 
the speeds will be accurate to one decimal, and right/left padded to be at least
five characters.
The reason this is the default is to prevent the length of the block from
changing and shifting all of your blocklets.
Modify the printf command using the `-p` option to fit your needs if this default
is not acceptable to you.

Note that the interface will be guessed using `ip route` but it can also be specified 
using the `-i` switch or using `$BLOCK_INSTANCE`, with the former taking precedence 
over the latter. On the fly interface switching is not supported, if you change
your default interface, simply issue `i3-msg restart` and the script will pick
up on the new default. However, the block will wait until a default interface
is found upon starting, so no restart is needed if you start i3 and then connect 
to wifi later.

# Options

```
Usage: bandwidth [-i interface] [-t time] [-u unit] [-p printf_command] [-l] [-h]
Options:
-i  Network interface to measure. Default determined using `ip route`.
-t  Time interval in seconds between measurements. Default: 3
-u  Units to measure bytes in. Default: Mb
    Allowed units: Kb, KB, Mb, MB, Gb, GB, Tb, TB
    Units may have optional it/its/yte/ytes on the end, e.g. Mbits, KByte
-p  Awk command to be called after a measurement is made. 
    Default: printf "<span font='FontAwesome'>  </span>%-5.1f/%5.1f %s/s\n", rx, wx, unit;
    Exposed variables: rx, wx, tx, unit, iface
-l  List available interfaces in /proc/net/dev
-h  Show this help text
```
