#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os
import time
from uiautomator import Device
import utility.common as u
def enable_developer_setting(self, name):
	checkbox = self(className="android.widget.ListView",resourceId="android:id/list").\
			child_by_text(name,className="android.widget.LinearLayout").\
			child(className="android.widget.CheckBox")

	if checkbox.checked == False:
		print (name + " is not enabled, enabling it")
		checkbox.click()
	else:
		print(name + " enabled")
        
def ChangeDeveloper_settings(self):
	package = 'com.android.settings'
	activity = '.DevelopmentSettings'
	component_name = package + '/' + activity
	u.start_activity(self,component_name)
	self.wait.update()
	enable_developer_setting(self,u'Stay awake')
	enable_developer_setting(self,u'Allow mock locations')

if __name__ == '__main__':
	d = Device()
	d.wakeup()
    # Press the HOME button to start the test from the home screen
	d.press.home()
	ChangeDeveloper_settings(d) 
    # Press the HOME button to start the test from the home screen
#	d.press.home()
