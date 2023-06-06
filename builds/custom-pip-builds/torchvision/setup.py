#!/usr/bin/env python
import os
import io
import re
import shutil
import sys
from setuptools import setup, find_packages
from pkg_resources import get_distribution, DistributionNotFound


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def get_dist(pkgname):
    try:
        return get_distribution(pkgname)
    except DistributionNotFound:
        return None


def find_version(*file_paths):
    version_file = read(*file_paths)
    if version_match := re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    ):
        return version_match[1]
    raise RuntimeError("Unable to find version string.")


readme = open('README.rst').read()

VERSION = find_version('torchvision', '__init__.py')
#    'torch',

pillow_ver = ' >= 4.1.1'
pillow_req = 'pillow-simd' if get_dist('pillow-simd') is not None else 'pillow'
tqdm_ver = ' == 4.19.9' if sys.version_info[0] < 3 else ''
requirements = ['numpy', 'six', pillow_req + pillow_ver, f'tqdm{tqdm_ver}']
setup(
    # Metadata
    name='torchvision-nightly',
    version=VERSION,
    author='PyTorch Core Team',
    author_email='soumith@pytorch.org',
    url='https://github.com/pytorch/vision',
    description='image and video datasets and models for torch deep learning',
    long_description=readme,
    license='BSD',

    # Package info
    packages=find_packages(exclude=('test',)),

    zip_safe=True,
    install_requires=requirements,
)
