#! /usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator import Device
import os
if __name__ == '__main__':
    filename="dump.xml"
    d=Device()
    if os.path.exists(filename):
            os.remove(filename)
    d.dump(filename)
