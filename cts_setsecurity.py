#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os
from uiautomator import Device
from common import  *
# otherwise the import fails.
def setSecurity(d):
        package = 'com.android.settings'
        activity = '.SecuritySettings'
        component_name = package + '/' + activity
        start_activity(d,component_name)

        d(text=u'Screen lock').click()
        d(text=u'None').click()


if __name__ == '__main__':
    d = Device()
    # Press the HOME button to start the test from the home screen
    d.press.home()
    setSecurity(d)
    # Press the HOME button to start the test from the home screen
    d.press.home()
