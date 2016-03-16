#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup

# import DistUtilsExtra.command.build_extra
# import DistUtilsExtra.command.build_i18n
# import DistUtilsExtra.command.clean_i18n

# to update i18n .mo files (and merge .pot file into .po files) run on Linux:
# ,,python setup.py build_i18n -m''

# silence pyflakes, __VERSION__ is properly assigned below...
__VERSION__ = '0.2'
# for line in file('fbsdupdatecheck').readlines():
#    if (line.startswith('__VERSION__')):
#        exec(line.strip())
PROGRAM_VERSION = __VERSION__


def datafilelist(installbase, sourcebase):
    datafileList = []
    for root, subFolders, files in os.walk(sourcebase):
        fileList = []
        for f in files:
            fileList.append(os.path.join(root, f))
        datafileList.append((root.replace(sourcebase, installbase), fileList))
    return datafileList


setup(name="fbsdupdatecheck", version=PROGRAM_VERSION,
      description="This update FreeBSD system cache it for update-station",
      license='BSD',
      author='Eric Turgeon',
      url='https://github/GhostBSD/fbsdupdatecheck/',
      package_dir={'': '.'},
      install_requires=['setuptools'],
      scripts=['fbsdupdatecheck'])
