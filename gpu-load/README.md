# gpu-load

Shows load of Nvidia GPUs.

![](gpu-load.png)

The four values are the load of the:

1. The GPU it self
2. The load of the VRAM of the Card
3. Video buffer
4. PCIe bus utilization

`short_text` only shows the GPU load.

# Dependencies

* `nvidia-settings` Note that on Debian-based systems, you have to add `contrib` and `non-free` to your `sources.list` in order to install the package via your package manager.

# Config
```
[gpu-load]
command=$SCRIPT_DIR/gpu-load
label=GPU
interval=10
#min_width=GPU 100% 100% 100% 100%
#T_WARN=70
#T_CRIT=90
```
