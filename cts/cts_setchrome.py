#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os
from uiautomator import Device
from common import  *
def set_chrome(self):
    # page 1
	package = 'com.android.chrome'
	activity = 'com.google.android.apps.chrome.Main'
	component_name = package + '/' + activity
	start_activity(self,component_name)
	self.wait.update()
	self(resourceId="com.android.chrome:id/terms_accept").click()
	self.wait.update()
	self(resourceId="com.android.chrome:id/negative_button").click()

if __name__ == '__main__':
	d = Device()
    # Press the HOME button to start the test from the home screen
	d.press.home()
	set_chrome(d)
	#d.press.home()
