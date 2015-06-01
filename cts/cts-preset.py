#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os

from uiautomator import Device
from cts_wifisetting import SetWifiConnect,ModifyNetwork
from utility.skipwizzard import skip_setupwizzard
from cts_setchrome import set_chrome
from utility.changelanguage import changeLanguage
from utility.setsecurity import setSecurity
from utility.setdevelop import ChangeDeveloper_settings
from utility.settimezone import setTimezone
ap_name = 'dlink-549'
ap_password = '38017549'

# Connect to device with the IP received as a parameter
d = Device()
print u'Start to Skip setup wizzard'
d.watcher("OK").when(text="OK").when(text="OK").click(text="OK")
d.watcher("Ok").when(text="Ok").when(text="Ok").click(text="Ok")
d.watcher("GOT IT").when(text="GOT IT").when(text="GOT IT").click(text="GOT IT")
skip_setupwizzard(d)
# Press the HOME button to start the test from the home screen
d.press.home()
print u'Start to Change the settings in Developer'
ChangeDeveloper_settings(d)
print u'Start to Change the settings in Security'
setSecurity(d)
print u'Start to Change the TimeZone to GMT + 00:00'
#timezone=u'London, Dublin'
timezone=u'Azores'
setTimezone(d,timezone)
print u'Start to Connect device to Wifi'
#SetWifiConnect(d,ap_name,ap_password)
print u'Start to Modify the network to fit CTS\'s requirement'
ModifyNetwork(d,ap_name)
# Press the HOME button to start the test from the home screen
d.press.home()
print u'Start to Run Chrome browser & confirm the settings'
set_chrome(d)
print u'Run Chrome browser & confirm the settings --- Done'
d.watchers.remove()
d.press.home()
d(text="GOT IT").click()

