# systemd_unit

Show the status of a systemd unit as active, inactive or failed. This
blocklet uses dbus-send to get the current state of a systemd
unit. Both system and user units are supported.

![](systemd_unit.png)

# Config

Simple example for dhcpd service:
```
[dhcpcd_service]
command=$SCRIPT_DIR/systemd_unit
markup=pango
label=dhcpcd: 
interval=30
UNIT_NAME=dhcpcd.service
```

Full example for dhcpd service:
```
[dhcpcd_service]
command=$SCRIPT_DIR/systemd_unit
markup=pango
label=dhcpcd: 
interval=30
UNIT_NAME=dhcpcd.service
USER_UNIT=false
ACTIVE_COLOR=green
INACTIVE_COLOR=orange
FAILED_COLOR=red
```

For user units set `USER_UNIT=true`
