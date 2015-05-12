#! /usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator import Device
from time import sleep
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises

import sys
sys.path.append("../utility")

import utility as u
class TestSensor(object):
    # constructor
    def __init__(self):
        #criterion , TODO: need to redefine them.
        self.g_xmin=-0.0800
        self.g_xmax=-0.0300
        self.g_ymin=-0.500
        self.g_ymax=-0.300
        self.g_zmin=10.250
        self.g_zmax=10.400
        self.gyro_xmin=-1
        self.gyro_xmax=1
        self.gyro_ymin=-1
        self.gyro_ymax=1
        self.gyro_zmin=-1
        self.gyro_zmax=1
        self.mag_xmin=10
        self.mag_xmax=50 
        self.mag_ymin=-100
        self.mag_ymax=50
        self.mag_zmin=-50
        self.mag_zmax=50
        self.d = Device()
    # destructor
    def __del__(self):
        pass
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        #Install Meter toolbox apk
        u.setup(self.d)
        ret = self.d.server.adb.cmd("install -r ./Z-DeviceTest_1.7_47.apk").communicate()
        if not ret:
            print("Failure to install Z-DeviceTest")
        else:
            print("Sucessful to install Z-DeviceTest")
        self.d.press.home()
        self.d.server.adb.cmd("shell am start -n zausan.zdevicetest/.zdevicetest").communicate()
        self.d.wait.update()
    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        #Uninstall Meter toolbox apk
        #get package name by "adb shell pm list packages | grep "meter"
        ret = self.d.server.adb.cmd("uninstall zausan.zdevicetest").communicate()
        if not ret:
            print("Failure to uninstall Z-DeviceTest apk")
        else:
            print("Sucessful to uninstall Z-DeviceTest apk")
        u.teardown(self.d)
        self.d.press.home()
    def test_Accel(self):
        print("Test to Gradienter")
        self.d(resourceId="zausan.zdevicetest:id/boton_acelerometros").click()
        # Change to Gradienter tab (got text is "0.323232 m/s2")
        x = self.d(resourceId="zausan.zdevicetest:id/acelerometro_x").text.split(" ")[0]
        y = self.d(resourceId="zausan.zdevicetest:id/acelerometro_y").text.split(" ")[0]
        z = self.d(resourceId="zausan.zdevicetest:id/acelerometro_z").text.split(" ")[0]

        print ("acele X = %f" % float(x))
        print ("acele Y = %f" % float(y))
        print ("acele Z = %f" % float(z))
    def test_Gyro(self):
        print("Test to Gyro")
    def test_Mag(self):
        print("Test to Mag Field")
if __name__ == '__main__':
    sensor=TestSensor()
    sensor.setUp()
    sensor.test_Accel()
    #sensor.test_Gyro()
    #sensor.test_Mag()
    sensor.teardown()
