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

class TestStorage(object):
    @classmethod
    def setup_class(self):
        """This method is run once for each class before any tests are run"""
        self.DUT_serial_no = "70400121"
        self.storage_int_min = 11.00
        self.storage_int_max = 12.00
        self.storage_ext_min = 30.00
        self.storage_ext_max = 32.00
        self.storage_int_min = float(u.getparas('storage','storage_int_min'))
        self.storage_int_max = float(u.getparas('storage','storage_int_max'))
        self.storage_ext_min = float(u.getparas('storage','storage_ext_min'))
        self.storage_ext_max = float(u.getparas('storage','storage_ext_max'))
        self.DUT_serial_no = u.getparas('common','DUT_serial_no')
        self.d = Device(self.DUT_serial_no)
        u.setup(self.d)

    @classmethod
    def teardown_class(self):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed""" 
        u.setup(self.d)

    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        u.teardown(self.d)
    def test_StorageSizeInt(self):
        print("Test to internal storage size")
        self.d.server.adb.cmd("shell am start -a android.intent.action.MAIN -n com.android.settings/.Settings").communicate()
        self.d.wait.update()
        self.d(text="Storage").click()
        storagesize = self.d(resourceId="android:id/summary").text
        size=float(storagesize[:-2])
        unit = storagesize[-2:]
        print("Internal storage totalsize = %2.2f %s" %(size,unit))
        assert (size <= self.storage_int_max ) and (size >= self.storage_int_min)

    def test_StorageSizeExt(self):
        pass
if __name__ == '__main__':
    t=TestStorage()
    t.setup_class()
    t.setUp()
    t.test_StorageSizeInt()
    pass
