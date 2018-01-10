# apt-upgrades

Show the number of pending system upgrades, as reported by aptitude.
More specifically, show: packages upgraded, newly installed, to remove, and not upgraded.


![](apt-upgrades.png)

# Requirements

Dependencies: aptitude, bash

Suggested: fonts-font-awesome

# Suggested usage

Copy the `i3blocks.conf` section into your i3blocks configuration.
We assume you use `signal=1` but you can choose another signal number if you prefer.
Create apt/dpkg hooks to signal the script.
For example, create `/etc/apt/apt.conf.d/80i3blocks` with contents

```
APT::Update::Post-Invoke { "pkill -RTMIN+1 i3blocks || true"; };
DPkg::Post-Invoke { "pkill -RTMIN+1 i3blocks || true"; };
```
**Warning**: make sure to 
```ShellSession
sudo chown root:root /etc/apt/apt.conf.d/80i3blocks
sudo chmod 644 /etc/apt/apt.conf.d/80i3blocks
```
so that only the root user may modify
`80i3blocks`. This is necessary because apt has root privileges when upgrading the system,
and therefore commands in `80i3blocks` will be executed with root privileges.

You may also combine this script with a cron job that calls `apt-get update` periodically for
a more "popup upgrade reminder" feeling.

# Simple usage

Instead of using `signal=1` in the configuration, you can use `interval=3600` 
to have the script execute every hour.
This method avoids the usage of apt/dpkg hooks.

# Config

```INI
[apt-upgrades]
command=$SCRIPT_DIR/apt-upgrades
signal=1
interval=once
#PENDING_SYMBOL="\uf021 "
#SYMBOL_ONLY=0
#ALWAYS_PRINT=1
#PENDING_COLOR="#00FF00"
#NONPENDING_COLOR="#FFFFFF"
```
