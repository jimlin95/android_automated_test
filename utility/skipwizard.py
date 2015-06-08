#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os
import time
from uiautomator import Device
from common import  *
def skip_setupwizard(d):
    # wait system server ready
    loop =100 
    while not d.server.alive and loop > 0 :
        time.sleep(10)
        loop -= 1
        try:
            d.server.start()
            print("try to start")
            time.sleep(3)
        except:
            print("pass")
            pass 
    print ("loop =%d" %loop)
    loop=100
    while loop>0:
        time.sleep(3)
        loop -= 1
        print ("loop =%d" %loop)
        try:
            d.wakeup()
            ret = d(resourceId='com.google.android.setupwizard:id/start').wait.exists(timeout=5000)
            if ret:
                print("Found it!!!")
                break
            d.server.start()
        except:
            print("pass1")
            pass
    print("System ready,Go Go Go !!!")
    #print("server status = %s" % d.server.alive)
    d.wakeup()
    # page 1
    d(resourceId='com.google.android.setupwizard:id/start').click()

    d.wait.update()
    d(resourceId='com.android.settings:id/setup_wizard_navbar_next').click()
    # page 2 (wifi)
    # page 2 sub page (wifi)
    d(resourceId='android:id/button2').click()
    d.wait.update()
    # page 3 Date& Time
    d(resourceId='com.google.android.setupwizard:id/setup_wizard_navbar_next').click()
    d.wait.update()
    # page 4 Name
    #d(resourceId="com.google.android.setupwizard:id/first_name_edit").set_text("LCBU")
    #d.press.enter()
    #d(resourceId="com.google.android.setupwizard:id/last_name_edit").set_text("Quanta")
    #d.press.enter()
    d.wait.update()
    d.press.back()
    d(resourceId='com.google.android.setupwizard:id/setup_wizard_navbar_next').click()
    d.wait.update()
    # page 5 Google Services More
    d(resourceId='com.google.android.setupwizard:id/setup_wizard_navbar_next').click()
    d.wait.update()
    # page 5 Google Services Next
    d(resourceId='com.google.android.setupwizard:id/setup_wizard_navbar_next').click()
    d.wait.update()
    # page   Setup complete
    d(resourceId='com.google.android.setupwizard:id/setup_wizard_navbar_next').click()
    d.wait.update()
    
    # Set Up Wi-Fi
    d(text="OK").click()
    d.wait.update()
    ap_name = "dlink-549"
    ap_password = "38017549"
    timeout = 15000
    time.sleep(2) 
    d.wait.update()
    d(text=ap_name).click()
    d.wait.update()
    if d(text=ap_name).exists:
        d(resourceId='com.android.settings:id/password').set_text(ap_password)
    else:
        d.press.back()
        d(text=ap_name).click()
        d(resourceId='com.android.settings:id/password').set_text(ap_password)
    d(text=u'Connect').click()
    ret = d(text=u'Connected').wait.exists(timeout=timeout)
    if ret:
        d.press.back()
    else:
        ret = d(text=u'Connected').wait.exists(timeout=timeout)
        d.press.back()
    #d(text=u'GOT IT').click()
if __name__ == '__main__':
    d = Device()
    skip_setupwizard(d) 
