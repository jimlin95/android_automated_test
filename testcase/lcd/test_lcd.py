#! /usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator import Device
from time import sleep
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
import utility.common as u
class Testlcd(object):
    # constructor
    def __init__(self):
        
        #Initial value (criterion )
        self.fixture_serial_no = "f0e673e1"
        self.DUT_serial_no = "70400121"
        self.lux_max_lcd_on = 50
        self.lux_min_lcd_on = 40
        self.lux_max_lcd_off = 10
        self.lux_min_lcd_off = 20
        #================================
        # get params from unittest.ini
        #================================
        self.fixture_serial_no = u.getparas('lcd','fixture_serial_no')
        self.DUT_serial_no = u.getparas('lcd','DUT_serial_no')
        self.lux_max_lcd_on = float(u.getparas('lcd','lux_max_lcd_on'))
        self.lux_min_lcd_on = float(u.getparas('lcd','lux_min_lcd_on'))
        self.lux_max_lcd_off = float(u.getparas('lcd','lux_max_lcd_off'))
        self.lux_min_lcd_off = float(u.getparas('lcd','lux_min_lcd_off'))
        #================================
        # Initial Fixture as self.f
        self.f = Device(self.fixture_serial_no)
        # Initial DUT as self.d
        self.d = Device(self.DUT_serial_no)
        #TODO , set Display timeout to maximum (30 minutes) on DUT before testing.
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
        u.setup(self.f)
        #Install Meter toolbox apk
        ret = self.f.server.adb.cmd("install -r ./Meter\ Toolbox_1.1.2_14.apk").communicate()
        if not ret:
            print("Failure to install Meter Toolbox apk")
        else:
            print("install Meter toolbox apk sucessfuly")
        # Install Display Tester apk
        ret = self.d.server.adb.cmd("install -r ./Display\ Tester_1.2_4.apk").communicate()
        if not ret:
            print("Failure to install Display Tester apk")
        else:
            print("Sucessful to install Display Tester apk")
        self.f.press.home()
        self.d.press.home()
        self.d.server.adb.cmd("shell am start -n com.sain.device.displaytest/.Main").communicate()
        self.d.wait.update()
    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        u.teardown(self.d)
        u.teardown(self.f)
        #Uninstall Meter toolbox apk
        #get package name by "adb shell pm list packages | grep "meter"
        ret = self.f.server.adb.cmd("uninstall com.jkfantasy.meterbox").communicate()
        if not ret:
            print("Failure to uninstall Meter Toolbox apk")
        else:
            print("Sucessful to uninstall Meter Toolbox apk")
        ret = self.d.server.adb.cmd("uninstall com.sain.device.displaytest").communicate()
        if not ret:
            print("Failure to uninstall Display Tester apk")
        else:
            print("Sucessful to uninstall Display Tester  apk")

    def test_lcd_off(self):
        print("Test LCD OFF")
        #show Black screen
        self.d(className="android.widget.Button",resourceId="com.sain.device.displaytest:id/lcdblack").click()
        self.d.screen.off() 
        # Change to light meter tab in fixure device
        self.f.server.adb.cmd("shell am start -n com.jkfantasy.meterbox/.MainActivity").communicate()
        self.f.wait.update()
        self.f(resourceId="com.jkfantasy.meterbox:id/btn_tab1").click()
        # Wait 3 seconds to get lux
        sleep(3)
        self.f(resourceId="com.jkfantasy.meterbox:id/btn_pause").click()
        min=self.f(resourceId="com.jkfantasy.meterbox:id/tv_light_min_value").text
        max=self.f(resourceId="com.jkfantasy.meterbox:id/tv_light_max_value").text
        avg=self.f(resourceId="com.jkfantasy.meterbox:id/tv_light_avg_value").text
        cur=self.f(resourceId="com.jkfantasy.meterbox:id/tv_light_cur_value").text
        print("light_min  = %3.2f" % float(min))
        print("light_max  = %3.2f" % float(max))
        print("light_avg  = %3.2f" % float(avg))
        print("light_cur  = %3.2f" % float(cur))
        self.d.screen.on() 
        self.d.press.back()
        assert (float(avg) >= self.lux_min_lcd_off) and (float(avg) <= self.lux_max_lcd_off)
    def test_lcd_on(self):
        print("Test LCD ON")
        #show White screen
        self.d(className="android.widget.Button",resourceId="com.sain.device.displaytest:id/lcdwhite").click()
        self.d.screen.on() 
        # Change to light meter tab
        self.f.server.adb.cmd("shell am start -n com.jkfantasy.meterbox/.MainActivity").communicate()
        self.f.wait.update()
        self.f(resourceId="com.jkfantasy.meterbox:id/btn_tab1").click()
        # Wait 3 seconds to get lux
        sleep(3)
        self.f(resourceId="com.jkfantasy.meterbox:id/btn_pause").click()
        min=self.f(resourceId="com.jkfantasy.meterbox:id/tv_light_min_value").text
        max=self.f(resourceId="com.jkfantasy.meterbox:id/tv_light_max_value").text
        avg=self.f(resourceId="com.jkfantasy.meterbox:id/tv_light_avg_value").text
        cur=self.f(resourceId="com.jkfantasy.meterbox:id/tv_light_cur_value").text
        print("light_min  = %3.2f" % float(min))
        print("light_max  = %3.2f" % float(max))
        print("light_avg  = %3.2f" % float(avg))
        print("light_cur  = %3.2f" % float(cur))
        self.d.press.back()
        assert (float(avg) >= self.lux_min_lcd_on) and (float(avg) <= self.lux_max_lcd_on)
 
if __name__ == '__main__':
    lcd=Testlcd()
    lcd.setUp()
    lcd.test_lcd_on()
    lcd.test_lcd_off()
    lcd.teardown()
