#!/bin/sh
nmcli -t connection show --active | awk -F ':' '
/tun0/{vpn="ON"} /vpn/{name=$1}
END{if(vpn) printf("%s\n%s\n%s\n", name, vpn, "#00FF00")}'
