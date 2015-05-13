#! /usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator import Device
from time import sleep
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
from os.path import join, exists
import os
import time
import sys
sys.path.append("../utility")
import ConfigParser
import utility as u
from comparison import isMatch, getMatchedCenterOffset

class TestCamera(object):
    # constructor
    def __init__(self):
        #criterion , TODO: need to redefine them.
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
        u.setup(self.d)
        self.d.server.adb.cmd("shell rm /sdcard/DCIM/Camera/*").communicate()
        self.d.server.adb.cmd("shell refresh /sdcard/DCIM/Camera").communicate()
        self.d.server.adb.cmd("shell am start -n com.google.android.GoogleCamera/com.android.camera.CameraActivity").communicate()
        self.d.wait.update()
    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        u.teardown(self.d)
    def test_TakePicture(self):
        print("Test to Camera take picture")
        # default value
        #=================================
        expect_filename = "expect.jpg"
        current_filename = "current.jpg"
        sleep_time = 5
        threshold = 0.02
        #================================
        # get params from unittest.ini
        #================================
        configParser = ConfigParser.RawConfigParser()   
        configFilePath = r'./unittest.ini'
        configParser.read(configFilePath)
        expect_filename = configParser.get('takepicture','expect_filename')
        current_filename = configParser.get('takepicture','current_filename')
        threshold = float(configParser.get('takepicture','threshold'))
        sleep_time = float(configParser.get('takepicture','sleep'))

        #================================
        if os.path.exists(current_filename):
                os.remove(current_filename)
        expect_image_path = os.path.abspath(expect_filename)
        current_image_path = os.path.abspath(current_filename)
        beforeC = self.d.server.adb.cmd("shell ls /sdcard/DCIM/Camera").communicate()
        self.d(description='Shutter').wait.exists(timeout=5000)
        #================================
        # Take picture action
        #================================
        self.d(resourceId="com.android.camera2:id/shutter_button").click.wait(timeout=2000)
        sleep(sleep_time)
        afterC = self.d.server.adb.cmd("shell ls /sdcard/DCIM/Camera").communicate()
        if afterC == beforeC:
            print("take picture fail")
            assert False
            return 
        # AfterC = ('IMG_20150513_150900.jpg\r\n', '') , it's a example
        # print(afterC)
        # Convert tuple to string
        filename=''.join(afterC)
        filename=filename.split('\r\n')[0]
        # adb pull picture and rename to $current_filename
        self.d.server.adb.cmd("pull /sdcard/DCIM/Camera/" + filename +" ./"+ current_filename ).communicate()


        #================================
        # compare two images
        #================================
        assert os.path.exists(expect_image_path), 'the local expected image %s not found!' % expect_image_path 
        ret, minVal = isMatch(expect_image_path , current_image_path, threshold)
        if ret:
            print('Picture Match! , threshold = ' + str(threshold)) + ' ,minVal = ' + str(minVal)
            assert True         
        else:
            print("Unmatkch")
            assert False, 'Picture UnMatch! , threshold = ' + str(threshold) + ' ,minVal = ' + str(minVal)

if __name__ == '__main__':
    camera=TestCamera()
    camera.setUp()
    camera.test_TakePicture()
    camera.teardown()
