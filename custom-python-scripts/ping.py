#This script will ping all ip addresses which are possible to get ip of oblu.

import os
import re
import time
import sys
from threading import Thread

class testit(Thread):
   def __init__ (self,ip):
      Thread.__init__(self)
      self.ip = ip
      self.status = -1
   def run(self):
      pingaling = os.popen("ping -q -c2 "+self.ip,"r")
      while 1:
        line = pingaling.readline()
        if not line: break
        igot = re.findall(testit.lifeline,line)
        if igot:
           self.status = int(igot[0])

testit.lifeline = re.compile(r"(\d) received")
report = ("No response","Partial Response","Alive")

MAX_PARALLEL = 15

print time.ctime()

pinglist = []
top = 254
new_dict = {}

for t in range(1,top+1):
 for host in range(1,top+1):
   ip = "172.17."+str(t)+"."+str(host)
   current = testit(ip)
   pinglist.append(current)
   current.start()

   waitfor = 0
   if len(pinglist) > MAX_PARALLEL: waitfor = 1
   if host == top: waitfor = len(pinglist)

   for reap in range(waitfor):
       pingle = pinglist[0]
       pinglist = pinglist[1:]
       pingle.join()
       if(pingle.status==2):
          print "Status from ",pingle.ip,"is",report[pingle.status]
 print t," done"
print time.ctime()
