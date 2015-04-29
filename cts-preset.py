#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os

from uiautomator import Device
from common import  *
from cts_develop import ChangeDeveloper_settings
from cts_setsecurity import setSecurity
from cts_settimezone import setTimezone
from cts_wifisetting import SetWifiConnect,ModifyNetwork
from cts_skipwizzard import skip_setupwizzard
from cts_setchrome import set_chrome
from changelanguage import changeLanguage


ap_name = 'dlink-549'
ap_password = '38017549'

# Connect to device with the IP received as a parameter
d = Device()
print u'Start to Skip setup wizzard'
skip_setupwizzard(d)
# Press the HOME button to start the test from the home screen
d.press.home()
#Change language to English (United States)
print u'Start to Change Language to English'
changeLanguage(d,'en-rUS')
print u'Start to Change the settings in Developer'
ChangeDeveloper_settings(d)
print u'Start to Change the settings in Security'
setSecurity(d)
print u'Start to Change the TimeZone to GMT + 00:00'
setTimezone(d)
print u'Start to Connect device to Wifi'
SetWifiConnect(d,ap_name,ap_password)
print u'Start to Modify the network to fit CTS\'s requirement'
ModifyNetwork(d,ap_name)
# Press the HOME button to start the test from the home screen
d.press.home()
print u'Start to Run Chrome browser & confirm the settings'
set_chrome(d)
print u'Run Chrome browser & confirm the settings --- Done'
d.press.home()

