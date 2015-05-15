#! /usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator import Device
from time import sleep
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
import utility.common as u
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
        self.light_min = 0
        self.light_max = 100

        #================================
        # get params from unittest.ini
        #================================
        self.g_xmin = float(u.getparas('gsensor','spec_xmin'))
        self.g_xmax = float(u.getparas('gsensor','spec_xmax'))
        self.g_ymin = float(u.getparas('gsensor','spec_ymin'))
        self.g_ymax = float(u.getparas('gsensor','spec_ymax'))
        self.g_zmin = float(u.getparas('gsensor','spec_zmin'))
        self.g_zmax = float(u.getparas('gsensor','spec_zmax'))
 
        self.gyro_xmin = float(u.getparas('gyro','spec_xmin'))
        self.gyro_xmax = float(u.getparas('gyro','spec_xmax'))
        self.gyro_ymin = float(u.getparas('gyro','spec_ymin'))
        self.gyro_ymax = float(u.getparas('gyro','spec_ymax'))
        self.gyro_zmin = float(u.getparas('gyro','spec_zmin'))
        self.gyro_zmax = float(u.getparas('gyro','spec_zmax'))

        self.mag_xmin = float(u.getparas('mag','spec_xmin'))
        self.mag_xmax = float(u.getparas('mag','spec_xmax'))
        self.mag_ymin = float(u.getparas('mag','spec_ymin'))
        self.mag_ymax = float(u.getparas('mag','spec_ymax'))
        self.mag_zmin = float(u.getparas('mag','spec_zmin'))
        self.mag_zmax = float(u.getparas('mag','spec_zmax'))

        self.light_min = float(u.getparas('light','spec_min'))
        self.light_max = float(u.getparas('light','spec_max'))
        #================================
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
        #Install Z-Devicetest apk
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
        #Uninstall Z-Devicetest apk
        #get package name by "adb shell pm list packages | grep "zdevice"
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
        x = self.d(resourceId="zausan.zdevicetest:id/acelerometro_x").text.split(" ")[0]
        y = self.d(resourceId="zausan.zdevicetest:id/acelerometro_y").text.split(" ")[0]
        z = self.d(resourceId="zausan.zdevicetest:id/acelerometro_z").text.split(" ")[0]

        print ("acele X = %f" % float(x))
        print ("acele Y = %f" % float(y))
        print ("acele Z = %f" % float(z))
        assert (float(x) >= self.g_xmin) and (float(x) <= self.g_xmax)
        assert (float(y) >= self.g_ymin) and (float(y) <= self.g_ymax)
        assert (float(z) >= self.g_zmin) and (float(z) <= self.g_zmax)
    def test_Compass(self):
        print("Test to Compass")
        self.d(resourceId="zausan.zdevicetest:id/boton_brujula").click()
        x = self.d(resourceId="zausan.zdevicetest:id/brujula_x").text.split(" ")[0]
        y = self.d(resourceId="zausan.zdevicetest:id/brujula_y").text.split(" ")[0]
        z = self.d(resourceId="zausan.zdevicetest:id/brujula_z").text.split(" ")[0]
        
        print ("acele X = %f" % float(x))
        print ("acele Y = %f" % float(y))
        print ("acele Z = %f" % float(z))
        assert (float(x) >= self.mag_xmin) and (float(x) <= self.mag_xmax)
        assert (float(y) >= self.mag_ymin) and (float(y) <= self.mag_ymax)
        assert (float(z) >= self.mag_zmin) and (float(z) <= self.mag_zmax)
    def test_Light(self):
        print("Test to Compass")
        self.d(resourceId="zausan.zdevicetest:id/boton_luz").click()
        intensity = self.d(resourceId="zausan.zdevicetest:id/luz_intensidad").text.split(" ")[0]
        
        print (" intensity = %f" % float(intensity))
        assert (float(intensity) >= self.light_min) and (float(intensity) <= self.light_max)
if __name__ == '__main__':
    pass
