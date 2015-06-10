#! /usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator import Device
from time import sleep
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
import utility.common as u

class TestBluetooth(object):
    @classmethod
    def setup_class(self):
        """This method is run once for each class before any tests are run"""
        self.DUT_serial_no = "70400121"
        self.bluetooth_mac = "12:34:56:78:9A:BC"
        self.DUT_serial_no = u.getparas('common','DUT_serial_no')
        self.bluetooth_mac= u.getparas('bluetooth','bluetooth_mac')
        self.d = Device(self.DUT_serial_no)
    @classmethod
    def teardown_class(self):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        u.setup(self.d)
    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        u.teardown(self.d)
    def test_01_TurnOffBluetooth(self):
        print("Test to turn off bluetooth")
        # Turn off bluetooth 
        self.d.server.adb.cmd("shell am start -a android.intent.action.MAIN -n com.android.settings/.bluetooth.BluetoothSettings"). \
                communicate()
        self.d.wait.update()
        if self.d(text="ON").exists:
            self.d(text="ON").click()
            sleep(3)
        self.d.wait.update()

        assert self.d(text="OFF").exists

    def test_02_TurnOnBluetooth(self):
        print("Test to turn on bluetooth")
        # Turn off bluetooth 
        self.d.server.adb.cmd("shell am start -a android.intent.action.MAIN -n com.android.settings/.bluetooth.BluetoothSettings"). \
                communicate()
        self.d.wait.update()
        if self.d(text="OFF").exists:
            self.d(text="OFF").click()
            sleep(3)
        self.d.wait.update()
 
        assert self.d(text="ON").exists

    def test_03_Search_Bluetooth_Devices(self):
        print("Test to search BT Devices")
        #================================
        # get params from unittest.ini
        #================================
        self.timeout = int(u.getparas('bluetooth','timeout'))
        #================================
        # Open the Settings app
        self.d.server.adb.cmd("shell am start -a android.intent.action.MAIN -n com.android.settings/.bluetooth.BluetoothSettings"). \
                communicate()

        if self.d(text="OFF").exists:
            self.d(text="OFF").click()
            sleep(3)
        else:
            self.d(text="ON").click()
            sleep(3)
            self.d(text="OFF").click()
            sleep(3)
        self.d.wait.update()
        ret = self.d(text="Search for devices").wait.exists(timeout=self.timeout)
        print("The string of search for devices is found ? = " + str(ret))
        avl = self.d(className="android.widget.ListView").child_by_text("Available devices").childCount
        # child 1 FARTMB611Y
        # child 2 Available devices
        # after child 3 searched devices. "No nearby Bluetooth devices were found."
        found=self.d(text="No nearby Bluetooth devices were found.").exists
        print("The string of No nearby Bluetooth devices were found." "? = " + str(found))
        if found:
            avl = avl -1

        print("Number of devices has been found = " + str(avl-2))
        assert avl > 2 and  found == False
    def test_04_Check_Bluetooth_MAC_address(self):
        print("Check Bluetooth Mac address")
        self.d.server.adb.cmd("shell am start -n com.android.settings/.deviceinfo.Status").communicate()
        self.d.wait.update()
        bluetooth_mac = self.d(text="Bluetooth address").down(className="android.widget.TextView").text
        print("bluetooth_mac = %s" % bluetooth_mac)
        assert (bluetooth_mac.upper() == self.bluetooth_mac.upper())

if __name__ == '__main__':
    bluetooth=TestBluetooth()
    bluetooth.setUp()
    bluetooth.test_TurnOffBluetooth()
    bluetooth.test_TurnOnBluetooth()
    bluetooth.test_Search_Bluetooth_Devices()
