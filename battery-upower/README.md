# battery-upower

Show battery status from [UPower] daemon.

![](battery-upower.png)

The blocklet shows the power plug character 🔌 if the battery is charging or
fully charged, or the battery character 🔋otherwise, along with the time to full
or empty respectively.  If UPower provides no information about the remaining
time show the battery level in percentage instead.

As short text the blocklet shows the percentage along with a `+` sign
(charging), a `-` sign (discharging) or no sign (fully charged).

This blocklet does not poll the battery; instead it is a persisted blocket
which connects to the UPower DBus interface at startup and listens for change
signals emitted by UPower.

[upower]: https://upower.freedesktop.org/

# Dependencies

* [UPower]
* Python 3
* [PyGObject]
* glib

[PyGObject]: https://pygobject.readthedocs.io/en/latest/

# Config

```ini
[battery-upower]
command=$SCRIPT_DIR/battery-upower
interval=persist
format=json
```
