#! /usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator import Device
from time import sleep
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
import os
from utility.record import record, record_init,record_start, record_stop, record_end
import utility.common as u
import audioop 
import wave
from utility.frequency_analysis import plotAmplitudeSpectru


class TestMic(object):
    @classmethod
    def setup_class(self):
        """This method is run once for each class before any tests are run"""
        #Initial value (criterion )
        self.fixture_serial_no = "f0e673e1"
        self.DUT_serial_no = "70400121"
        self.dbm_max_mic= 6000
        self.dbm_min_mic= 4800
        record_filename = 'record' # record.wav , record.png
        self.wav_filename = record_filename + '.wav'
        self.png_filename = record_filename + '.png'
        #================================
        # get params from unittest.ini
        #================================
        self.fixture_serial_no = u.getparas('mic','fixture_serial_no')
        self.DUT_serial_no = u.getparas('mic','DUT_serial_no')
        self.dbm_max_mic = float(u.getparas('mic','dbm_max_mic'))
        self.dbm_min_mic = float(u.getparas('mic','dbm_min_mic'))
        self.wav_filename = u.getparas('mic','wavfile')
        self.png_filename = u.getparas('mic','pngfile')
        #================================
        # Initial Fixture as self.f
        self.f = Device(self.fixture_serial_no)
        # Install Signal Generator apk
        ret = self.f.server.adb.cmd("install -r ./Signal\ Generator_1.21_6.apk").communicate()
        if not ret:
            print("Failure to install Signal Generator apk")
        else:
            print("Sucessful to install Signal Generator apk")
        # Initial DUT as self.d
        self.d = Device(self.DUT_serial_no)
        self.d.wav_filename = self.wav_filename
        record_init(self.d)
    @classmethod
    def teardown_class(self):
        """This method is run once for each class _after_ all tests are run"""
        #Uninstall Meter toolbox apk
        #get package name by "adb shell pm list packages | grep "meter"
        ret = self.f.server.adb.cmd("uninstall radonsoft.net.signalgen").communicate()
        if not ret:
            print("Failure to uninstall SignalGen apk")
        else:
            print("Sucessful to uninstall SignalGen apk")


    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        u.setup(self.d)
        u.setup(self.f)
    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        u.teardown(self.d)
        u.teardown(self.f)
    def test_mic(self):
        print("Test MIC")
        self.f.server.adb.cmd("shell am start -n radonsoft.net.signalgen/.SignalGen").communicate()
        self.f.wait.update()
        # generate sine wave
        self.f(resourceId="radonsoft.net.signalgen:id/Button03").click()
        record_start(self.d)
        record_stop(self.d)
        # stop to generate sine wave
        self.f(resourceId="radonsoft.net.signalgen:id/Button03").click()
        record_end(self.d)
        audiofp = wave.open(self.wav_filename,'r')
        params = audiofp.getparams()
        info = ['nchannels','sampwidth','framerate','nframes','comptype','compname']
        for i in range(6):
            print( str(info[i]) + " = " + str(params[i])) 
        framebuffer = audiofp.readframes(audiofp.getnframes())
        rms = audioop.rms(framebuffer,2)
        print("rms = " + str(rms))

        plotAmplitudeSpectru(self.wav_filename,self.png_filename)
        assert (float(rms) >= self.dbm_min_mic) and (float(rms) <= self.dbm_max_mic)
if __name__ == '__main__':
    pass
