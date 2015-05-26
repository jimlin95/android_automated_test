#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from time import sleep
from uiautomator import Device
def record(self):

    current_filename = "record.wav"
    if os.path.exists(current_filename):
        os.remove(current_filename)
    # Get pythonpath
    try:
           user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
    except KeyError:
           user_paths = []
    user_paths = ''.join(user_paths)

    ret = self.server.adb.cmd("install -r " + user_paths + "/utility/apks/Smart\ Voice\ Recorder_1.7.1_12.apk").communicate()
    if not ret:
        print("Failure to install Smart Voice Recorder")
    else:
        print("Sucessful to install Smart Voice Recorder")
    self.server.adb.cmd("shell rm /sdcard/SmartVoiceRecorder/*").communicate()
    self.server.adb.cmd("shell refresh /sdcard/SmartVoiceRecorder").communicate()
    ret = self.server.adb.cmd("shell am start -n com.andrwq.recorder/.RecorderActivity").communicate()
    beforeR = self.server.adb.cmd("shell ls /sdcard/SmartVoiceRecorder").communicate()
    self.wait.update()
    self(className="android.widget.ImageButton",description="More options").click()
    self(text="Settings").click()
    self(text="Sample rate (quality)").click()
    self(text="44.1 kHz (CD)",className="android.widget.CheckedTextView").click()
    self.press.back()

    self(text="Start recording   ").click()
    self(text="Finish   ").click()
    self(resourceId="android:id/button1").click()
    sleep(3)
    afterR = self.server.adb.cmd("shell ls /sdcard/SmartVoiceRecorder").communicate()
    filename=''.join(afterR)
    filename=filename.split('\r\n')[0]
    #print(filename)
    # adb pull picture and rename to $current_filename
    self.server.adb.cmd("pull /sdcard/SmartVoiceRecorder/"+ filename +" ./"+ current_filename ).communicate()

    ret = self.server.adb.cmd("uninstall com.andrwq.recorder").communicate()
    if not ret:
        print("Failure to uninstall Smart Voice Recorder")
    else:
        print("Sucessful to uninstall Smart Voice Recorder")

    self.server.adb.cmd("shell rm /sdcard/SmartVoiceRecorder/*").communicate()
    self.server.adb.cmd("shell refresh /sdcard/SmartVoiceRecorder").communicate()

def record_init(self):
    # Get pythonpath
    try:
           user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
    except KeyError:
           user_paths = []
    user_paths = ''.join(user_paths)
    print("PYTHONPATH = " + user_paths)
    ret = self.server.adb.cmd("install -r " + user_paths + "/utility/apks/Smart\ Voice\ Recorder_1.7.1_12.apk").communicate()
    if not ret:
        print("Failure to install Smart Voice Recorder")
    else:
        print("Sucessful to install Smart Voice Recorder")
    self.server.adb.cmd("shell rm /sdcard/SmartVoiceRecorder/*").communicate()
    self.server.adb.cmd("shell refresh /sdcard/SmartVoiceRecorder").communicate()
    ret = self.server.adb.cmd("shell am start -n com.andrwq.recorder/.RecorderActivity").communicate()
    self.wait.update()
    self(className="android.widget.ImageButton",description="More options").click()
    self(text="Settings").click()
    self(text="Sample rate (quality)").click()
    self(text="44.1 kHz (CD)",className="android.widget.CheckedTextView").click()
    self.press.back()
def record_start(self):

    ret = self.server.adb.cmd("shell am start -n com.andrwq.recorder/.RecorderActivity").communicate()
    self(text="Start recording   ").click()

def record_stop(self):

    self(text="Finish   ",className="android.widget.Button").click()
    self(resourceId="android:id/button1").click()

def record_end(self):
    if os.path.exists(self.wav_filename):
        os.remove(self.wav_filename)
    sleep(2)
    afterR = self.server.adb.cmd("shell ls /sdcard/SmartVoiceRecorder").communicate()
    filename=''.join(afterR)
    filename=filename.split('\r\n')[0]
    #print(filename)
    # adb pull picture and rename to self.wav_filename
    self.server.adb.cmd("pull /sdcard/SmartVoiceRecorder/"+ filename +" ./"+ self.wav_filename ).communicate()

    ret = self.server.adb.cmd("uninstall com.andrwq.recorder").communicate()
    if not ret:
        print("Failure to uninstall Smart Voice Recorder")
    else:
        print("Sucessful to uninstall Smart Voice Recorder")

    self.server.adb.cmd("shell rm /sdcard/SmartVoiceRecorder/*").communicate()
    self.server.adb.cmd("shell refresh /sdcard/SmartVoiceRecorder").communicate()
if __name__ == '__main__':
    d = Device()
    record(d)
    #record_init(d)
    #record_start(d)
    #record_end(d)
