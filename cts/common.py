#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
def start_activity(d,activity):
	d.server.adb.cmd("shell am start -n" + activity).communicate()
										 
def print_dict(mydic):
    for key, value in mydic.iteritems() :
        print key, value



