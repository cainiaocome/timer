#!/usr/bin/env python
#encoding: utf-8

import time
import threading
from timer import ATimer

i = 0
def update_self():
    global i
    try:
        print i
        i = i + 1
        if i>3:
            #self.stop() #global name self is not defined
            threading.Event().set()
            print 'event set\n'
    except Exception,e:
        print Exception, e


update_self_handle = ATimer(fn=update_self, sleep=1)
update_self_handle.daemon = True
update_self_handle.start()
print 'main start waiting\n'
threading.Event().wait()
print 'main come here, exiting...\n'
