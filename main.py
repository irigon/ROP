#!/usr/bin/python3

import _thread
import time
import sys
import os

from libs import g 
from libs import monitor

def start_monitor_thread():
   try:
      _thread.start_new_thread( monitor.monitor, ("Thread-1", 2, ) )
   except:
      print ("Error: unable to start thread")
            

start_monitor_thread()

while 1:
    time.sleep(1)
    print(g.roles)
    #import pdb; pdb.set_trace()
    for role in g.roles:
       g.roles[role].play() 
