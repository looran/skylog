#!/usr/bin/env python

# skylog.py
# Logs skype users status changes to stdout in CSV format
# On startup all online users are added to CSV
# On startup, exit and local user status change, lines from simulated user
# "syslog-info" are added to CSV
# Format: 20130219-154801,Marimounette,OFFLINE
# Usage: python skylog.py >> skylog.csv &
# 2013, Laurent Ghigonis <laurent@p1sec.com>

import Skype4Py
import time
import sys
import atexit

do_exit = False

def cb_exit():
  print sys.stderr, "skylog: cb_exit()"
  print_csv("<<<skylog-info", "EXIT")

def cb_attachmentstatus(status):
  global do_exit

  print >> sys.stderr, "skylog: cb_attachmentstatus: %s" % status
  if status != Skype4Py.apiAttachSuccess:
    print >> sys.stderr, "skylog: Disconnected from skype ! exiting"
    do_exit = True

def cb_userstatus(status):
  print_csv("***skylog-info", status)

def cb_onlinestatus(user, status):
  print_csv(user.Handle, status)

def print_csv(user, status):
  t = time.strftime("%Y%m%d-%H%M%S", time.localtime())
  print "%s,%s,%s" % (t, user, status)
  sys.stdout.flush()

def print_online_users(skype):
  for f in skype.Friends:
    if f.OnlineStatus != Skype4Py.cusOffline:
      print_csv(f.Handle, f.OnlineStatus)

atexit.register(cb_exit)
skype = Skype4Py.Skype()
skype.RegisterEventHandler('AttachmentStatus', cb_attachmentstatus)
skype.RegisterEventHandler('UserStatus', cb_userstatus)
skype.RegisterEventHandler('OnlineStatus', cb_onlinestatus)
skype.Attach()
print >> sys.stderr, 'Started'
print_csv(">>>skylog-info", "STARTUP")

print_online_users(skype)
while True:
  time.sleep(0.1)
  if do_exit is True:
    break
