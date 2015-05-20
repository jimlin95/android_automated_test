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
        #criterion
        self.sound_min=60.0
        self.sound_max=73.0
        self.light_min=15.0
        self.light_max=20.0
        self.g_xmin=-0.40
        self.g_xmax=-0.20
        self.g_ymin=-2.50
        self.g_ymax=-1.90
        self.DUT_serial_no = "70400121"
        #================================
        # get params from unittest.ini
        #================================
        self.DUT_serial_no = u.getparas('common','DUT_serial_no')
        self.g_xmin = float(u.getparas('gsensor','spec_xmin'))
        self.g_xmax = float(u.getparas('gsensor','spec_xmax'))
        self.g_ymin = float(u.getparas('gsensor','spec_ymin'))
        self.g_ymax = float(u.getparas('gsensor','spec_ymax'))
        
        self.sound_min = float(u.getparas('sound','spec_min'))
        self.sound_max = float(u.getparas('sound','spec_max'))
        self.light_min = float(u.getparas('light','spec_min'))
        self.light_max = float(u.getparas('light','spec_max'))
        #================================
        self.d = Device(self.DUT_serial_no)
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
        u.setup(self.d)
        #Install Meter toolbox apk
        ret = self.d.server.adb.cmd("install -r ./Meter\ Toolbox_1.1.2_14.apk").communicate()
        if not ret:
            print("Failure to install Meter Toolbox apk")
        else:
            print("install Meter toolbox apk sucessfuly")
        self.d.press.home()
        self.d.server.adb.cmd("shell am start -n com.jkfantasy.meterbox/.MainActivity").communicate()
        self.d.wait.update()
    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        u.teardown(self.d)
        #Uninstall Meter toolbox apk
        #get package name by "adb shell pm list packages | grep "meter"
        ret = self.d.server.adb.cmd("uninstall com.jkfantasy.meterbox").communicate()
        if not ret:
            print("Failure to uninstall Meter Toolbox apk")
        else:
            print("Sucessful to uninstall Meter Toolbox apk")

        self.d.press.home()
    def test_SoundMeter(self):
        print("Test to Sound Meter")
        self.d(resourceId="com.jkfantasy.meterbox:id/btn_tab0").click()
        sleep(5)
        self.d(resourceId="com.jkfantasy.meterbox:id/btn_pause").click()
        min=self.d(resourceId="com.jkfantasy.meterbox:id/tv_sound_min_value").text
        max=self.d(resourceId="com.jkfantasy.meterbox:id/tv_sound_max_value").text
        avg=self.d(resourceId="com.jkfantasy.meterbox:id/tv_sound_avg_value").text
        cur=self.d(resourceId="com.jkfantasy.meterbox:id/tv_sound_cur_value").text
        print("sound_min  = %3.2f" % float(min))
        print("sound_max  = %3.2f" % float(max))
        print("sound_avg  = %3.2f" % float(avg))
        print("sound_curr = %3.2f" % float(cur))
        assert (float(cur) > self.sound_min) and (float(cur) < self.sound_max)
        
    def test_LightMeter(self):
        print("Test to Light Meter")
        # Change to light meter tab
        self.d(resourceId="com.jkfantasy.meterbox:id/btn_tab1").click()
        sleep(5)
        
        self.d(resourceId="com.jkfantasy.meterbox:id/btn_pause").click()

        min=self.d(resourceId="com.jkfantasy.meterbox:id/tv_light_min_value").text
        max=self.d(resourceId="com.jkfantasy.meterbox:id/tv_light_max_value").text
        avg=self.d(resourceId="com.jkfantasy.meterbox:id/tv_light_avg_value").text
        cur=self.d(resourceId="com.jkfantasy.meterbox:id/tv_light_cur_value").text
        print("light_min  = %3.2f" % float(min))
        print("light_max  = %3.2f" % float(max))
        print("light_avg  = %3.2f" % float(avg))
        print("light_cur  = %3.2f" % float(cur))
        assert (float(cur) > self.light_min) and (float(cur) < self.light_max)
    def test_Gsensor(self):
        print("Test to Gradienter")
        # Change to Gradienter tab
        self.d(resourceId="com.jkfantasy.meterbox:id/btn_tab2").click()
        sleep(5)
        
        self.d(resourceId="com.jkfantasy.meterbox:id/btn_pause").click()
        x_min=self.d(resourceId="com.jkfantasy.meterbox:id/tv_gradi_min_value_x").text.split('=')[1]
        y_min=self.d(resourceId="com.jkfantasy.meterbox:id/tv_gradi_min_value_y").text.split('=')[1]
        x_max=self.d(resourceId="com.jkfantasy.meterbox:id/tv_gradi_max_value_x").text.split('=')[1]
        y_max=self.d(resourceId="com.jkfantasy.meterbox:id/tv_gradi_max_value_y").text.split('=')[1]
        x_avg=self.d(resourceId="com.jkfantasy.meterbox:id/tv_gradi_avg_value_x").text.split('=')[1]
        y_avg=self.d(resourceId="com.jkfantasy.meterbox:id/tv_gradi_avg_value_y").text.split('=')[1]
        x_cur=self.d(resourceId="com.jkfantasy.meterbox:id/tv_gradi_cur_value_x").text.split('=')[1]
        y_cur=self.d(resourceId="com.jkfantasy.meterbox:id/tv_gradi_cur_value_y").text.split('=')[1]

        print("x_min  = %3.2f" % float(x_min))
        print("y_min  = %3.2f" % float(y_min))
        print("x_max  = %3.2f" % float(x_max))
        print("y_max  = %3.2f" % float(y_max))
        print("x_avg  = %3.2f" % float(x_avg))
        print("y_avg  = %3.2f" % float(y_avg))
        print("x_cur  = %3.2f" % float(x_cur))
        print("y_cur  = %3.2f" % float(y_cur))
        assert (float(x_cur) >= self.g_xmin) and (float(x_cur) <= self.g_xmax)
        assert (float(y_cur) >= self.g_ymin) and (float(y_cur) <= self.g_ymax)
if __name__ == '__main__':
    sensor=TestSensor()
    sensor.setUp()
    sensor.test_LightMeter()
    sensor.test_SoundMeter()
    sensor.test_Gsensor()
    sensor.teardown()
