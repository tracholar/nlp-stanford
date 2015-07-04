# coding:utf-8
from os import system
import sys,time
if len(sys.argv)==2:
	msg = sys.argv[2]
else:
	msg = time.strftime('%Y%m%d')
print msg
system('git add .')
system('git commit -m "%s"' % msg)
system('git push origin master')