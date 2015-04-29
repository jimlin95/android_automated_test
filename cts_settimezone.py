#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os


from uiautomator import Device
from common import *
def setTimezone(d):        
        # call Date & Time settings
        d.server.adb.cmd("shell am start -a android.settings.DATE_SETTINGS")
        d(text=u'Select time zone').click()
        d(resourceId="android:id/list").scroll.vert.to(text=u'London, Dublin')
        d(text=u'London, Dublin').click()
 
if __name__ == '__main__':
        # Connect to device with the IP received as a parameter
        d = Device()
        d.press.home()

        setTimezone(d)

        # Press the HOME button to start the test from the home screen
        d.press.home()
