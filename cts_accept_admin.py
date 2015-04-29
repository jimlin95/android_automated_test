#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os
from uiautomator import Device
from common import  *
 
def accept_device_admin_install(self):
	d(resourceId="com.android.vending:id/positive_button").click()

if __name__ == '__main__':
    d = Device()
    # Press the HOME button to start the test from the home screen
    d.press.home()
    accept_device_admin_install(d)
