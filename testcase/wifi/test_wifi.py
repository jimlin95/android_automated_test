#! /usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator import Device
from time import sleep
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises

class TestWiFi(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        self.d = Device()
        self.ap_name='dlink-549'
        self.ap_password='38017549'
        self.d.press.home()
    def teardown(self):
        """This method is run once after _each_ test method is executed"""
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


    def test_connect2wifiap(self):
        print("Test to connect to  Wifi AP")
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
        assert self.d(text=u'Connected').wait.exists(timeout=15000)

if __name__ == '__main__':
    wifi=TestWiFi()
    wifi.setUp()
    wifi.test_TurnOffWiFi()
    wifi.test_TurnOnWiFi()
    wifi.test_connect2wifiap()
