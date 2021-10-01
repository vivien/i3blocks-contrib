# gpu-load

Shows load of Nvidia or AMD GPUs.

![](gpu-load.png)

The four values are the load of the:

1. The GPU it self
2. The load of the VRAM of the Card
3. Video buffer (NVIDIA only)
4. PCIe bus utilization (NVIDIA only)

`short_text` only shows the GPU load.

# Dependencies

Choose one depends on your GPU.

* `nvidia-settings` Note that on Debian-based systems, you have to add `contrib` and `non-free` to your `sources.list` in order to install the package via your package manager.
* [`radeontop`](https://github.com/clbr/radeontop)

# Config
```
[gpu-load]
command=$SCRIPT_DIR/gpu-load
label=GPU
interval=10
#min_width=GPU 100% 100% 100% 100%
#GPU_BRAND=NVIDIA // or AMD
#T_WARN=70
#T_CRIT=90
```
