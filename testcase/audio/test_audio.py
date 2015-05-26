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

from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write

class TestAudio(object):
    @classmethod
    def setup_class(self):
        """This method is run once for each class before any tests are run"""
        #Initial value (criterion )
        self.fixture_serial_no = "f0e673e1"
        self.DUT_serial_no = "70400121"
        self.dbm_max_audio = 6000
        self.dbm_min_audio = 4800
        record_filename = 'record' # record.wav , record.png
        self.wav_filename = record_filename + '.wav'
        self.png_filename = record_filename + '.png'
        #================================
        # get params from unittest.ini
        #================================
        self.fixture_serial_no = u.getparas('audio','fixture_serial_no')
        self.DUT_serial_no = u.getparas('audio','DUT_serial_no')
        self.dbm_max_audio = float(u.getparas('audio','dbm_max_audio'))
        self.dbm_min_audio = float(u.getparas('audio','dbm_min_audio'))
        self.wav_filename = u.getparas('audio','wavfile')
        self.png_filename = u.getparas('audio','pngfile')
        #================================
        # Initial Fixture as self.f
        self.f = Device(self.fixture_serial_no)
        self.f.wav_filename = self.wav_filename
        # Initial DUT as self.d
        self.d = Device(self.DUT_serial_no)
        # Install Signal Generator apk
        ret = self.d.server.adb.cmd("install -r ./Signal\ Generator_1.21_6.apk").communicate()
        if not ret:
            print("Failure to install Signal Generator apk")
        else:
            print("Sucessful to install Signal Generator apk")
        record_init(self.f)
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
    def test_audioout(self):
        print("Test Audio speak")
        self.d.server.adb.cmd("shell am start -n radonsoft.net.signalgen/.SignalGen").communicate()
        self.d.wait.update()
        # generate sine wave
        self.d(resourceId="radonsoft.net.signalgen:id/Button03").click()
        record_start(self.f)
        record_stop(self.f)
        # stop to generate sine wave
        self.d(resourceId="radonsoft.net.signalgen:id/Button03").click()
        record_end(self.f)
        audiofp = wave.open(self.wav_filename,'r')
        params = audiofp.getparams()
        info = ['nchannels','sampwidth','framerate','nframes','comptype','compname']
        for i in range(6):
            print( str(info[i]) + " = " + str(params[i])) 
        framebuffer = audiofp.readframes(audiofp.getnframes())
        rms = audioop.rms(framebuffer,2)
        print("rms = " + str(rms))

        assert (float(rms) >= self.dbm_min_audio) and (float(rms) <= self.dbm_max_audio)
        plotAmplitudeSpectru(self.wav_filename,self.png_filename)
if __name__ == '__main__':
    d = Device()
    record(d)

