# ping

Displays the average round-trip time in milliseconds and the current package loss in percent for a specified target.

![normal status example](images/normal.png) ![warning status example](images/warning.png) ![error status example](images/error.png)

# Dependencies

A POSIX compatible shell,  ping ([iputils](https://github.com/iputils/iputils)) and optionally FontAwesome for the label.

# i3blocks.conf

```ini
[batterybar]
label= 
command=$SCRIPT_DIR/ping/ping
interval=repeat
markup=pango
min_width=99.99ms (0% PL)
```

# Environment Variables

* `PING_WARNING_COLOR`: Warning foreground color, default #f0c674
* `PING_ERROR_COLOR`: Error foreground color, default #cc6666

* `PING_RTT_WARNING`: Minimum in ms that triggers a round-trip time warning, default 50
* `PING_RTT_ERROR`: Minimum in ms that triggers a round-trip time error, default 100

* `PING_PL_WARNING`: Minimum in percent that triggers a package-loss warning, default 1
* `PING_PL_ERROR`: Minimum in percent that triggers a package-loss error, default 10

* `PING_NO_PL`: Disables package loss output, default 0

* `PING_INTERVAL`: Seconds to wait between sending each packet, default 0.2 - only root can go lower
* `PING_COUNT`: Packages to send, default 100
* `PING_TARGET`: Ping target address, default 8.8.8.8
* `PING_DEADLINE`: Timeout in seconds, default 70

* `PING_CMD`: Full ping command to execute, setting this overrides `PING_INTERVAL`, `PING_COUNT`, `PING_TARGET`, `PING_DEADLINE`!