#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os
import time
from uiautomator import Device
from common import  *
def skip_setupwizzard(d):
    # page 1
    d(resourceId='com.google.android.setupwizard:id/start').click()
    # page 2 (wifi)
    d(resourceId='com.android.settings:id/custom_button').click()
    # page 2 sub page (wifi)
    d(resourceId='android:id/button2').click()
    # page 3
    d(resourceId='com.google.android.setupwizard:id/next_button').click()
    # page 4
    d(resourceId='com.google.android.setupwizard:id/next_button').click()
    # page 5
    d(resourceId='com.google.android.setupwizard:id/next_button').click()
    # page 6
    d(text='OK').click()
    time.sleep(1)
    # page 7
    d(text='OK').click()


if __name__ == '__main__':
    d = Device()
    skip_setupwizzard(d) 
