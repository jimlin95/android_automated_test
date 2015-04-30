#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os
from uiautomator import Device
from common import  *
 
def enable_device_admin_setting(vc, name):
    checkbox = d(className="android.widget.ListView",resourceId="android:id/list").\
            child_by_text(name,className="android.widget.LinearLayout").\
            child(className="android.widget.CheckBox")
    if checkbox.checked == False:
        print (name + " not enabled, enabling it")
        checkbox.click()
        d.wait.update()
        d(resourceId="com.android.settings:id/action_button").click()
    else:
        print(name + " enabled")


def set_device_admins(self):
        package = 'com.android.settings'
        activity = '.DeviceAdminSettings'
        component_name = package + '/' + activity
        start_activity(d,component_name)
        d.wait.update()
        enable_device_admin_setting(self,"android.deviceadmin.cts.CtsDeviceAdminReceiver")
        enable_device_admin_setting(self,"android.deviceadmin.cts.CtsDeviceAdminReceiver2")

if __name__ == '__main__':
    d = Device()
    # Press the HOME button to start the test from the home screen
    d.press.home()
    set_device_admins(d)
