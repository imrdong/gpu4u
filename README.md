<p align="center">
    <img src="./img/gpu4u_logo.png" width="200" />
</p>
<p align="center">
    <img alt="Language Python" src="https://img.shields.io/badge/Language-Python-red">
    <a href="https://github.com/imrdong/gpu4u/blob/master/LICENSE">
        <img alt="License GPL-3.0" src="https://img.shields.io/github/license/imrdong/gpu4u.svg?label=License&color=blue">
    </a>
    <a href="https://pypi.org/project/gpu4u/">
        <img alt="PyPI version" src="https://img.shields.io/pypi/v/gpu4u.svg?label=Version&maxAge=10">
    </a>
    <a href="https://pepy.tech/project/gpu4u">
        <img alt="PePy downloads" src="https://static.pepy.tech/personalized-badge/gpu4u?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads">
    </a>
    <a href="https://github.com/imrdong/gpu4u/stargazers/">
        <img alt="GitHub stars" src="https://img.shields.io/github/stars/imrdong/gpu4u.svg?style=social&label=Star&maxAge=10">
    </a>
    <a href="https://github.com/imrdong/gpu4u/network/members/">
        <img alt="GitHub forks" src="https://img.shields.io/github/forks/imrdong/gpu4u?style=social&label=Fork&maxAge=10">
    </a>
</p>
<h3 align="center">
A Python Package for Automatically Monitoring & Occupying NVIDIA GPUs
</h3>

`GPU4U` locates all GPUs on the computer, determines their availablity and returns a ordered list of available GPUs. Availablity is based upon the current memory consumption and load of each GPU. The package is written with GPU selection for Deep Learning in mind, but it is not task/library specific and it can be applied to any task, where it may be useful to identify available GPUs.

## Requirements

NVIDIA GPU with latest NVIDIA driver installed. `GPU4U` uses the program `nvidia-smi` to get the GPU status of all NVIDIA GPUs. nvidia-smi should be installed automatically, when you install your NVIDIA driver.

Python libraris:

* json
* os
* random
* re
* sys
* time
* datetime
* pynvml
* requests

Tested on CUDA driver version 450.102.04 with Python 3.6.10.

## Installation

### With PIP

```
pip install gpu4u
```

### With Source Code

```bash
git clone https://github.com/imrdong/gpu4u.git
cd gpu4u
python setup.py install
```

## Usage

### Base

To combine `GPU4U` with your Python code, all you have to do is 

* Open a terminal in a folder other than the `GPU4U` folder  
* Start a python console by typing `python` in the terminal
* In the newly opened python console, type:

```python
>>> from gpu4u import auto_monitor
>>> auto_monitor(script="fill_in_your_script_here")
```

### WeChat

Given `WeChat` token, you can receive notifications from `GPU4U` in `WeChat`.

* Go to [[PushPlus]](http://www.pushplus.plus/) official website, scan the QR code through `WeChat` to log in, and copy your token.
* The next steps are the same as [Base](#Base) section

```python
>>> token = "paste_your_token_here"
>>> from gpu4u import auto_monitor
>>> auto_monitor(script="fill_in_your_script_here", use_wechat_push=True, token=token)
```

The outputs of `GPU4U` depending on your number of GPUs and their current usage, see [Demo](#Demo) for more details.

## Demo

### :smile: Script Running with Available GPUs 

```
# Find available GPUs
Find Available GPU: 0, 1, 2, 3. Start Running Your Script.

# Random select one GPU to run your script
Script: CUDA_VISIBLE_DEVICES=1 python train.py --batch_size 64

# The start time of script run
Started @: 2021-02-22 13:08:23
```

### :disappointed: Script Running with No Available GPUs

```
# No available GPUs, start automatic monitoring with waiting time prompt
No Available GPU for Now, Automatic Monitoring for 0:23:10

# Find available GPUs
Find Available GPU: 2, 3. Start Running Your Script.

# Random select one GPU to run your script
Script: CUDA_VISIBLE_DEVICES=3 python train.py --batch_size 64

# The start time of script run
Started @: 2021-02-22 13:31:33
```

## License

See [LICENSE](LICENSE)