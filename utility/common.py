#! /usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
import os
from ConfigParser import RawConfigParser
def backHome(d):
    d.press('back')
    sleep(1)
    d.press('back')
    sleep(1)
    d.press('home')

def registerSysWatchers(d):
    d.watchers.remove()
    d.watcher("AUTO_FC_WHEN_ANR").when(textContains="isn't responding").when(text="Wait").click(text="OK")
    d.watcher("WEIBO_SEARCH_FRIENDS").when(text="搜寻好友").when(text="Skip").click(text="Skip")
    d.watcher("WEIBO_UPDATE").when(text="Download").when(text="Cancel").click(text="Cancel")
    d.watcher("ZDEV_WARN").when(text="Ok").when(text="Ok").click(text="Ok")
    d.watcher("NEXT").when(text="NEXT").when(text="NEXT").click(text="NEXT")
    d.watcher("Accept").when(text="Accept").when(text="Accept").click(text="Accept")
    d.watcher("OK").when(text="OK").when(text="OK").click(text="OK")
    d.watcher("GOT IT").when(text="GOT IT").when(text="GOT IT").click(text="GOT IT")

def checkSystemWatchers(d):
    if d.watcher("AUTO_FC_WHEN_ANR").triggered:
        raise Exception('AUTO_FC_WHEN_ANR')
    d.watchers.remove()

def setup(d):
    d.wakeup()
    d.info
    registerSysWatchers(d)
    backHome(d)

def teardown(d):
    checkSystemWatchers(d)
    backHome(d)

def getparas(section,key):
    configParser = RawConfigParser()
    configFilePath = r'./unittest.ini'
    if os.path.exists(configFilePath):
        configParser.read(configFilePath)
    else:
        print("Configuration file 'unittest.ini not found")
    section_exist = configParser.has_option(section,key)
    if section_exist:
        return configParser.get(section,key)
    else:
        return ""

def start_activity(d,activity):
    d.server.adb.cmd("shell am start -n" + activity).communicate()

def print_dict(mydic):
    for key, value in mydic.iteritems() :
        print key, value


