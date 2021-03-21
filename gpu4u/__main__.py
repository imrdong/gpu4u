# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: mrdong

import json
import os
import random
import re
import sys
import time
from datetime import datetime

import pynvml
import requests

pynvml.nvmlInit()

SCRIPT_RUN_PROMPT = ". Start Running Your Script."
GPU_BUSY_PROMPT = "No Available GPU for Now, Automatic Monitoring for "

TEMPLATE = "markdown"
TITLE = "GPU4U Notification"
URL = "http://pushplus.plus/send?"
GPU_FREE_PUSH = "<font color=Green>**Find Available GPU <br> Start Running Your Script**</font>"
GPU_BUSY_PUSH = "<font color=Red>**No Available GPU for Now <br> Automatic Monitoring is in Progress**</font>"


def wechat_push(token, content, use_wechat_push):
    """
    WeChat push
    :param token: push token
    :param content: push content
    :param use_wechat_push: True or False
    :return: none
    """
    data = {"token": token,
            "title": TITLE,
            "content": content,
            "template": TEMPLATE}
    body = json.dumps(data).encode(encoding="utf-8")
    headers = {'Content-Type': 'application/json'}
    if use_wechat_push:
        requests.post(url=URL, data=body, headers=headers)


def get_memory_usage():
    """
    Get GPUs device count, use 'nvidia-smi' command to get memory usage for each GPU
    :return: memory
    """
    memory = []
    for i in range(pynvml.nvmlDeviceGetCount()):
        gpu_status = os.popen('nvidia-smi -q -i {0} -d MEMORY'.format(i)).read()
        memory.append(re.search("Used:" + r"\d+" + "MiB", gpu_status.replace(" ", "")).group())
    return memory


def run_script(memory, script, flag, use_wechat_push, token):
    """
    Start running your script
    :param memory: current gpu memory usage
    :param script: your script
    :param flag: free or busy
    :param use_wechat_push: True or False
    :param token: push token
    :return none
    """
    gpu_available_list = [str(gpu_index) for gpu_index, gpu_memory in enumerate(memory) if gpu_memory == "Used:0MiB"]
    if flag == "free":
        print("\033[1;32mFind Available GPU: " + ", ".join(gpu_available_list) + SCRIPT_RUN_PROMPT + "\033[0m")
        wechat_push(token=token, content=GPU_FREE_PUSH, use_wechat_push=use_wechat_push)
    if flag == "busy":
        print("\033[1;32m\nFind Available GPU: " + ", ".join(gpu_available_list) + SCRIPT_RUN_PROMPT + "\033[0m")
        wechat_push(token=token, content=GPU_FREE_PUSH, use_wechat_push=use_wechat_push)
    cmd = 'CUDA_VISIBLE_DEVICES={} '.format(random.choice(gpu_available_list)) + script
    print("\033[1;32mScript: %s\nStarted @: %s\033[0m" % (cmd, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    os.system(cmd)


def auto_monitor(script, use_wechat_push=False, token=None):
    """
    If there are available GPUs, the script starts running directly
    else, GPU4U start automatic monitoring GPUs status with waiting time prompt
    :param script: your script
    :param use_wechat_push: True or False
    :param token: push token
    :return none
    """
    now = time.strftime('%Y%m%d%H%M%S', time.localtime())
    start = datetime.fromtimestamp(time.mktime(time.strptime(now, '%Y%m%d%H%M%S')))
    memory = get_memory_usage()
    if memory.count("Used:0MiB") > 0:
        flag = "free"
        run_script(memory, script, flag, use_wechat_push, token)
    else:
        wechat_push(token=token, content=GPU_BUSY_PUSH, use_wechat_push=use_wechat_push)
        while True:
            now = time.strftime('%Y%m%d%H%M%S', time.localtime())
            end = datetime.fromtimestamp(time.mktime(time.strptime(now, '%Y%m%d%H%M%S')))
            sys.stdout.write("\r\033[1;31m" + GPU_BUSY_PROMPT + "{0}\033[0m".format(end - start))
            sys.stdout.flush()
            memory = get_memory_usage()
            if memory.count("Used:0MiB") > 0:
                flag = "busy"
                run_script(memory, script, flag, use_wechat_push, token)
                break
