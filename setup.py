# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: mrdong

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gpu4u",
    version="0.2.0",
    author="mrdong",
    maintainer="mrdong",
    description="A Python Package for Automatically Monitoring & Occupying NVIDIA GPUs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/imrdong/gpu4u",
    packages=setuptools.find_packages(),
    license="GPL-3.0",
    install_requires=["pynvml", "requests"],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
