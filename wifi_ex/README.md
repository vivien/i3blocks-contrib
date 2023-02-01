# wifi_ex

---

## Description

### This blocklet lets you see if you are connected to WIFI and which network you are connected to, along with signal strength

---

## Dependencies

- [ip (if SHOW_IP is enabled)](https://command-not-found.com/ip)
- [iwconfig](https://command-not-found.com/iwconfig)
- [awk](https://command-not-found.com/awk)
- [grep](https://command-not-found.com/grep)
- [sed](https://command-not-found.com/sed)
- [FontAwesome Icon Pack (if using default labels)](https://fontawesome.com/download)

---

## Configuration

### INTERFACE

Sets interface wifi_ex should determine connection for. If `instance` property is set, it uses its value, otherwise it defaults to `wlan0`

### CONNECTED_GOOD_COLOR

Color in which output will be printed if interface is connected and connection strength is good. Defaults to `#00ff00`

### CONNECTED_MEDIUM_COLOR

Color in which output will be printed if interface is connected and connection strength is medium. Defaults to `#ffff00`

### CONNECTION_BAD_COLOR

Color in which output will be printed if interface is connected but connection strength is bad. Defaults to `#ff0000`

### DISCONNECTED_COLOR

Color in which output will be printed if interface is not connected or down. Defaults to `#ff0000`

### CONNECTED_GOOD_LABEL

Label that will precede the ESSID of the network if connection's strength is good. Defaults to ` (FontAwesome's "wifi")`

### CONNECTED_MEDIUM_LABEL

Label that will precede the ESSID of the network if connection's strength is good. Defaults to `CONNECTED_GOOD_LABEL`

### CONNECTED_BAD_LABEL

Label that will precede the ESSID of the network if connection's strength is bad. Defaults to `CONNECTED_GOOD_LABEL`

### DISCONNECTED_LABEL

Label that will precede the output string when interface is not connected or down. Defaults to ` (FontAwesome's "xmark")`

### GOOD_THRESHOLD

Connection's strength greater or equal to this value is considered good. Defaults to `80`

### MEDIUM_THRESHOLD

Connection's strength greater or equal to this value is considered medium. Any value below this is considered bad. Defaults to `40`

### SHOW_IP

If not set to `false`, blocklet will show IP alongside ESSID and connection's strength. Defaults to `false`

### ARBITRARY_SIGNAL

Signal level that will be used instead of actual connection's signal level. Can be used to test provided colors without changing networks/carrying device around. Unset by default

---

## Example configuration

```
[wifi]
command=$SCRIPT_DIR/wifi_ex
interval=10
INTERFACE=wlan0
CONNECTED_GOOD_COLOR=#00ff00
CONNECTED_MEDIUM_COLOR=#ffff00
CONNECTED_BAD_COLOR=#ff0000
DISCONNECTED_COLOR=#ff0000
CONNECTED_GOOD_LABEL=G:
CONNECTED_MEDIUM_LABEL=M:
CONNECTED_BAD_LABEL=B:
DISCONNECTED_LABEL=!
GOOD_THRESHOLD=80
MEDIUM_THRESHOLD=40
SHOW_IP=false
```

---

## License

See [LICENSE](LICENSE)

---

## Screenshots

### Interface connected (good signal strength)

![Connected screenshot](screenshots/connected-good.png?raw=true "Connected (good signal strength)")

### Interface connected (medium signal strength)

![Connected screenshot](screenshots/connected-medium.png?raw=true "Connected (medium signal strength)")

### Interface connected (bad signal strength)

![Connected screenshot](screenshots/connected-bad.png?raw=true "Connected (bad signal strength)")

### Interface disconnected/down

![Disconnected screenshot](screenshots/disconnected.png?raw=true "Disconnected")

### Interface connected (good signal strength, IP address shown)

![Connected with IP shown screenshot](screenshots/connected-show-ip.png?raw=true "Connected (good signal strength, IP address shown")

---

### [Mikut](https://mikut.dev) 2020-2022
