#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os

from uiautomator import Device

def setTimezone(self,tz):        
	# call Date & Time settings
	self.server.adb.cmd("shell am start -a android.settings.DATE_SETTINGS")
	ret = self(text=u'Select time zone').click()
	if ret == False:
		print("Can not find \"Select time zone\"")
		ret = self(text=u'Select time zone').click()
	self.wait.idle()
	ret = self(resourceId="android:id/list").scroll.vert.to(text=tz)
	if ret == False:
            ret = self(resourceId="android:id/list").scroll.vert.to(text=tz)
	self.wait.update()
	self(text=tz).click()
 
if __name__ == '__main__':
        # Connect to device with the IP received as a parameter
        d = Device()
        d.press.home()
#        timezone=u'London, Dublin'
        timezone=u'Azores'
        setTimezone(d,timezone)
        # Press the HOME button to start the test from the home screen
        d.press.home()
