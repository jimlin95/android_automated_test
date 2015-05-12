#! /usr/bin/env python
# -*- coding: utf-8 -*-
from uiautomator import Device as d
from time import sleep
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
