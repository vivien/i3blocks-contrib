# governor

Display the current governor for your CPU. Upon clicking, cycle through
the available governors.

# Config

```
[governor]
command=$SCRIPT_DIR/governor
interval=5
```

To be able to cycle through the different CPU governors, you will also need 
to allow your user to run `/usr/bin/cpupower` as root.

This can be done by adding the following line in `/etc/sudoers.d/$(whoami)`:

```shell
$ grep cpupower /etc/sudoers.d/qdii
qdii ALL= (root) NOPASSWD: /usr/bin/cpupower
```
