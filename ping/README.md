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

| Variable             | Default     | Description                                             |
| -------------------- | ----------: | ------------------------------------------------------- |
| `PING_WARNING_COLOR` |   `#f0c674` | Warning foreground color                                |
| `PING_ERROR_COLOR`   |   `#cc6666` | Error foreground color                                  |
| `PING_RTT_WARNING`   |        `50` | Minimum in ms that triggers a round-trip time warning   |
| `PING_RTT_ERROR`     |       `100` | Minimum in ms that triggers a round-trip time error     |
| `PING_PL_WARNING`    |         `1` | Minimum in percent that triggers a package-loss warning |
| `PING_PL_ERROR`      |        `10` | Minimum in percent that triggers a package-loss error   |
| `PING_NO_PL`         |         `0` | Setting this to 1 disables package loss output          |
| `PING_INTERVAL`      |       `0.2` | Seconds to wait between sending each packet             |
| `PING_COUNT`         |       `100` | Packages to send                                        |
| `PING_TARGET`        |   `8.8.8.8` | Ping target address                                     |
| `PING_DEADLINE`      |        `70` | Timeout in seconds                                      |

Additionally one can set `PING_CMD` to specify the full ping command to execute, overriding `PING_INTERVAL`, `PING_COUNT`, `PING_TARGET` and `PING_DEADLINE`.