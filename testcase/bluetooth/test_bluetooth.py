#! /usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator import Device
from time import sleep
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises

class TestBluetooth(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        self.d = Device()
        self.d.press.home()
    def teardown(self):
        """This method is run once after _each_ test method is executed"""
    def test_TurnOffBluetooth(self):
        print("Test to turn off bluetooth")
        # Turn off bluetooth 
        self.d.server.adb.cmd("shell am start -n com.android.settings/.Settings").communicate()

        self.d.wait.update()
        BT_SW=self.d(className="android.widget.ListView", resourceId="android:id/list") \
                .child_by_text("Bluetooth", className="android.widget.LinearLayout") \
                .child(className="android.widget.Switch")

        OnOff=BT_SW.text
        if OnOff == "ON":
            BT_SW.click()
            self.d.wait.update()

        OnOff=BT_SW.text
        assert_equal(OnOff,u"OFF")
    def test_TurnOnBluetooth(self):
        print("Test to turn on bluetooth")
        # Turn on bluetooth 
        self.d.server.adb.cmd("shell am start -n com.android.settings/.Settings").communicate()
        self.d.wait.update()
        BT_SW=self.d(className="android.widget.ListView", resourceId="android:id/list") \
                .child_by_text("Bluetooth", className="android.widget.LinearLayout") \
                .child(className="android.widget.Switch")

        OnOff=BT_SW.text

        if OnOff == "OFF":
            BT_SW.click()
            self.d.wait.update()

        OnOff= BT_SW.text
        assert_equal(OnOff,u"ON")


    def test_Search_Bluetooth_Devices(self):
        print("Test to search BT Devices")
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
        ret = self.d(text="Search for devices").wait.exists(timeout=15000)
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
if __name__ == '__main__':
    bluetooth=TestBluetooth()
    bluetooth.setUp()
    bluetooth.test_TurnOffBluetooth()
    bluetooth.test_TurnOnBluetooth()
    bluetooth.test_Search_Bluetooth_Devices()
