#!/usr/bin/env python

# skydbg v0.1
# Logs all skype notifications
# Usage: python skydbg.py >> dbg.log &
# 2013, Laurent Ghigonis <laurent@p1sec.com>

import Skype4Py
import time
import sys
import atexit

do_exit = False

def cb_exit():
  print sys.stderr, "skydbg: cb_exit()"
  print "EXIT"

def cb_notify(notification):
  t = time.strftime("%Y%m%d-%H%M%S", time.localtime())
  print "%s %s" % (t, notification)
  sys.stdout.flush()

def cb_attachmentstatus(status):
  global do_exit

  print >> sys.stderr, "skydbg: cb_attachmentstatus: %s" % status
  if status != Skype4Py.apiAttachSuccess:
    print >> sys.stderr, "skydbg: Disconnected from skype ! exiting"
    do_exit = True

atexit.register(cb_exit)
skype = Skype4Py.Skype()
skype.RegisterEventHandler('AttachmentStatus', cb_attachmentstatus)
skype.RegisterEventHandler('Notify', cb_notify)
skype.Attach()
print >> sys.stderr, 'Started'

while True:
  time.sleep(0.1)
  if do_exit is True:
    break
