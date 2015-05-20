#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os
from uiautomator import Device
import utility.common as u
def setDisplayTimeout(d,timeout):
    package = 'com.android.settings'
    activity = '.DisplaySettings'
    component_name = package + '/' + activity
    u.start_activity(d,component_name)
    SLEEP_TIMEOUT = {
        "15sec":"15 seconds",
        "30sec":"30 seconds", 
        "1min":"1 minutes",
        "2min":"2 minutes",
        "10min":"10 minutes",
        "30min":"30 minutes"
    }

    for k, v in SLEEP_TIMEOUT.iteritems():
        if k == timeout:
            ftimeout = v
            print("set Display timeout to " + v)
            break

    d(text=u'Sleep').click()
    d(text=ftimeout).click()


if __name__ == '__main__':
    d = Device()
    # Press the HOME button to start the test from the home screen
    d.press.home()
    setDisplayTimeout(d,u"30min")
    # Press the HOME button to start the test from the home screen
    d.press.home()
