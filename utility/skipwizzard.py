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


    d(resourceId='com.android.settings:id/setup_wizard_navbar_next').click()
    # page 2 (wifi)
    # page 2 sub page (wifi)
    d(resourceId='android:id/button2').click()
    # page 3 Date& Time
    d(resourceId='com.google.android.setupwizard:id/setup_wizard_navbar_next').click()
    # page 4 Name
    d(resourceId="com.google.android.setupwizard:id/first_name_edit").set_text("LCBU")
    d.press.enter()
    d(resourceId="com.google.android.setupwizard:id/last_name_edit").set_text("Quanta")
    d.press.enter()
    d.press.back()
    d(resourceId='com.google.android.setupwizard:id/setup_wizard_navbar_next').click()
    # page 5 Google Services More
    d(resourceId='com.google.android.setupwizard:id/setup_wizard_navbar_next').click()
    # page 5 Google Services Next
    d(resourceId='com.google.android.setupwizard:id/setup_wizard_navbar_next').click()
    # page   Setup complete
    d(resourceId='com.google.android.setupwizard:id/setup_wizard_navbar_next').click()
    
    # Set Up Wi-Fi
    d(text="OK").click()
    d.wait.update()
    ap_name = "dlink-549"
    ap_password = "38017549"
    timeout = 15000
    time.sleep(2) 
    d(text=ap_name).click()
    
    d(resourceId='com.android.settings:id/password').set_text(ap_password)
    d(text=u'Connect').click()
    ret = d(text=u'Connected').wait.exists(timeout=timeout)
    if ret:
        d.press.back()
    else:
        ret = d(text=u'Connected').wait.exists(timeout=timeout)
        d.press.back()
if __name__ == '__main__':
    d = Device()
    skip_setupwizzard(d) 
