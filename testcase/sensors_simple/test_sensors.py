#! /usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator import Device
from time import sleep
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises

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
        ret = self.d.server.adb.cmd("install -r ./SensorSimple_1.0_1.apk").communicate()
        if not ret:
            print("Failure to install Sensor Simpleapk")
        else:
            print("Install Sensor Simple apk sucessfuly")
        self.d.press.home()
        self.d.server.adb.cmd("shell am start -n  com.invensense.app.sensorsimple/.SensorSimpleActivity").communicate()
        self.d.wait.update()
    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        #Uninstall Meter toolbox apk
        #get package name by "adb shell pm list packages | grep "meter"
        ret = self.d.server.adb.cmd("uninstall com.invensense.app.sensorsimple").communicate()
        if not ret:
            print("Failure to uninstall Sensor Simple apk")
        else:
            print("Sucessful to uninstall Sensor Simple apk")

        self.d.press.home()
    def test_Accel(self):
        print("Test to Gradienter")
        # Change to Gradienter tab
        self.d(resourceId="com.invensense.app.sensorsimple:id/CheckBox10").click()
        sleep(5)
        self.d(resourceId="com.invensense.app.sensorsimple:id/CheckBox10").click()
        
        self.d.wait.update()
        x=self.d(resourceId="com.invensense.app.sensorsimple:id/TextView11").text
        y=self.d(resourceId="com.invensense.app.sensorsimple:id/TextView12").text
        z=self.d(resourceId="com.invensense.app.sensorsimple:id/TextView13").text

        print("x  = %3.7f" % float(x))
        print("y  = %3.7f" % float(y))
        print("z  = %3.7f" % float(z))
        #print("y=%f, y_min=%f, y_max=%f" % (float(y),self.g_ymin,self.g_ymax))
        assert (float(x) >= self.g_xmin) and (float(x) <= self.g_xmax)
        assert (float(y) >= self.g_ymin) and (float(y) <= self.g_ymax)
        assert (float(z) >= self.g_zmin) and (float(z) <= self.g_zmax)
    def test_Gyro(self):
        print("Test to Gyro")
        self.d(resourceId="com.invensense.app.sensorsimple:id/CheckBox20").click()
        sleep(5)
        self.d(resourceId="com.invensense.app.sensorsimple:id/CheckBox20").click()
        
        self.d.wait.update()
        x=self.d(resourceId="com.invensense.app.sensorsimple:id/TextView21").text
        y=self.d(resourceId="com.invensense.app.sensorsimple:id/TextView22").text
        z=self.d(resourceId="com.invensense.app.sensorsimple:id/TextView23").text

        print("x  = %3.7f" % float(x))
        print("y  = %3.7f" % float(y))
        print("z  = %3.7f" % float(z))
        #print("y=%f, y_min=%f, y_max=%f" % (float(y),self.g_ymin,self.g_ymax))
        assert (float(x) >= self.gyro_xmin) and (float(x) <= self.gyro_xmax)
        assert (float(y) >= self.gyro_ymin) and (float(y) <= self.gyro_ymax)
    def test_Mag(self):
        print("Test to Mag Field")
        self.d(resourceId="com.invensense.app.sensorsimple:id/CheckBox30").click()
        sleep(5)
        self.d(resourceId="com.invensense.app.sensorsimple:id/CheckBox30").click()
        
        self.d.wait.update()
        x=self.d(resourceId="com.invensense.app.sensorsimple:id/TextView31").text
        y=self.d(resourceId="com.invensense.app.sensorsimple:id/TextView32").text
        z=self.d(resourceId="com.invensense.app.sensorsimple:id/TextView33").text

        print("x  = %3.7f" % float(x))
        print("y  = %3.7f" % float(y))
        print("z  = %3.7f" % float(z))
        #print("y=%f, y_min=%f, y_max=%f" % (float(y),self.g_ymin,self.g_ymax))
        assert (float(x) >= self.mag_xmin) and (float(x) <= self.mag_xmax)
        assert (float(y) >= self.mag_ymin) and (float(y) <= self.mag_ymax)
        assert (float(z) >= self.mag_zmin) and (float(z) <= self.mag_zmax)
        assert (float(z) >= self.mag_zmin) and (float(z) <= self.mag_zmax)
if __name__ == '__main__':
    sensor=TestSensor()
    sensor.setUp()
    sensor.test_Accel()
    sensor.test_Gyro()
    sensor.test_Mag()
    sensor.teardown()
