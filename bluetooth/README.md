# bluetooth

Show the bluetooth connection status. Allows clicking to toggle the connection.

## Config Options

```bash
markup=pango
interval=1

# the following options are only applicable when markup=pango

# text color when bluetooth is ON
ON_COLOR=#50fa7b

# text color when bluetooth is OFF
OFF_COLOR=#FF5555

# bluetooth icon color
ICON_COLOR=#8be9fd
```

## Dependencies

- [fonts-font-awesome](https://packages.ubuntu.com/bionic/fonts-font-awesome)
- [bluetooth](https://manpages.ubuntu.com/manpages/bionic/man1/bluetooth.1.html)


## TODOs

- Add names of connected bluetooth devices
- Allow connection management per-device
