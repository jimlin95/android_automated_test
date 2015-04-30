#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os
import time
from uiautomator import Device
from common import  *


def SetWifiConnect(self,ap_name,ap_password):
        # Enable Wi-Fi
        self.server.adb.cmd("shell svc wifi enable").communicate()
        # Open the Settings app
        self.server.adb.cmd("shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings").communicate()
        time.sleep(2)
        self.wait.update()
        self(text=ap_name).click()
        self(resourceId='com.android.settings:id/password').set_text(ap_password)
        self(text=u'Connect').click()
        self(text=u'Connected').wait.exists(timeout=15000)
def ModifyNetwork(self,ap_name):
        #d.server.adb.cmd("shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings").communicate()
        #long press ap_name 
        self(text=ap_name).long_click()
        self(text=u'Modify network').click()
        self(text=u'Show advanced options').click.wait()
        self.wait.update()
        self(text=u'DHCP').click()
        self(text=u'Static').click.wait()
        self(className="android.widget.ScrollView").scroll.vert.to(text=u'DNS 1')
        self.wait.update()
        #self(resourceId='com.android.settings:id/dns1').set_text("")
        self(resourceId='com.android.settings:id/dns1').clear_text()
        self.press.enter()

        self.wait.update()
        #self(resourceId='com.android.settings:id/dns1').set_text("8.8.8.8")
        #self.press.enter()
        self(resourceId='com.android.settings:id/dns2').set_text("8.8.4.4")
        self.press.enter()
        if self(resourceId='com.android.settings:id/dns1').text != u"8.8.8.8":
            print("DNS 1 with wrong Text,input \"8.8.8.8\" again")
            #self(resourceId='com.android.settings:id/dns1').set_text(u"8.8.8.8")
            self(resourceId='com.android.settings:id/dns1').clear_text()
            self.press.enter()
            #self.press.enter()
        if self(resourceId='com.android.settings:id/dns2').text != u"8.8.4.4":
            print("DNS 2 with wrong Text,input \"8.8.4.4\" again")
            self(resourceId='com.android.settings:id/dns2').set_text(u"8.8.4.4")
            self.press.enter()


        self.wait.update()
        ret = self(text=u'Save',enabled=True).click()

        if ret == False:
            print "can not find Save button"
            self.wait.update()
            #self.wait.idle()
            ret = self(text=u'Save',enabled=True).click()
if __name__ == '__main__':

    d = Device()
    d.wakeup()
    d.press.home()
    SetWifiConnect(d,u'dlink-549',u'38017549')
    ModifyNetwork(d,u'dlink-549')
    # Press the HOME button to start the test from the home screen
