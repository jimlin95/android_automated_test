#! /usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator import Device
from time import sleep
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
import os
import utility.common as u
from utility.comparison import isMatch 
from nose.tools import nottest
class TestWiFi(object):
    @classmethod
    def setup_class(self):
        """This method is run once for each class before any tests are run"""
        self.DUT_serial_no = "70400121"
        self.wifi_mac = "12:34:56:78:9A:BC"
        self.DUT_serial_no = u.getparas('common','DUT_serial_no')
        self.wifi_mac= u.getparas('wifi','wifi_mac')
        self.d = Device(self.DUT_serial_no)
        u.setup(self.d)
        self.ap_name='dlink-549'
        self.ap_password='38017549'
        self.d.press.home()

    @classmethod
    def teardown_class(self):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed""" 
        u.setup(self.d)

    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        u.teardown(self.d)
        self.d.press.home()
    def test_TurnOffWiFi(self):
        print("Test to turn off Wifi")
        # Turn off Wifi 
        self.d.server.adb.cmd("shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings").communicate()
        self.d.wait.update()
        if self.d(text="ON").exists:
            self.d(text="ON").click()
            sleep(3)
        self.d.wait.update()

        assert self.d(text="OFF").exists

    def test_TurnOnWiFi(self):
        print("Test to turn on Wifi")
        # Turn on Wifi 
        self.d.server.adb.cmd("shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings").communicate()
        self.d.wait.update()
        if self.d(text="OFF").exists:
            self.d(text="OFF").click()
            sleep(3)
        self.d.wait.update()
 
        assert self.d(textContains="ON").exists

    def test_Connect2wifiap(self):
        print("Test to connect to  Wifi AP")
        #================================
        # get params from unittest.ini
        #================================
        self.ap_name = u.getparas('wifi','ap_name')
        self.ap_password = u.getparas('wifi','ap_password')
        self.timeout = int(u.getparas('wifi','timeout'))
        #================================
        # Open the Settings app
        self.d.server.adb.cmd("shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings").communicate()
        sleep(2)
        self.d.wait.update()
        self.d(text=self.ap_name).click()
        forget=self.d(text="Forget").exists
        if forget:
            self.d(text="Forget").click()
            self.d.wait.update()
            self.d(text=self.ap_name).click()
        self.d(resourceId='com.android.settings:id/password').set_text(self.ap_password)
        self.d(text=u'Connect').click()
        assert self.d(text=u'Connected').wait.exists(timeout=self.timeout)
    def test_CheckWiFiMac(self):
        print("Check Wifi Mac")
        self.d.server.adb.cmd("shell am start -n com.android.settings/.deviceinfo.Status").communicate()
        self.d.wait.update()
        wifi_mac = self.d(text="Wi‑Fi MAC address").down(className="android.widget.TextView").text
        print("wifi_mac = %s" % wifi_mac)
        assert (wifi_mac.upper() == self.wifi_mac.upper())
    @nottest
    def test_nottest(self):
        pass
if __name__ == '__main__':
    wifi=TestWiFi()
    wifi.setup_class()
    wifi.setUp()
   # wifi.test_TurnOffWiFi()
   # wifi.test_TurnOnWiFi()
   # wifi.test_Connect2wifiap() 
    wifi.test_CheckWiFiMac()
