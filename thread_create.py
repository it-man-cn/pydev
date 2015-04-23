#!/usr/bin/python
import rrdtool
import os
import time

class CreateThreadGraph:

	def create(self,rrdPath):
		if os.path.exists(rrdPath):
			return
		else:
			now=str(int(time.time()))
			rrd=rrdtool.create(rrdPath,'--step','60','--start',now,
			'DS:maxThreads:GAUGE:600:0:U',
			'DS:currentThreadsBusy:GAUGE:600:0:U',
			'DS:currentThreadCount:GAUGE:600:0:U',
			'DS:connectionCount:GAUGE:600:0:U',
			'RRA:AVERAGE:0.5:1:10080',
			'RRA:AVERAGE:0.5:5:2016',
			'RRA:MAX:0.5:1:10080',
			'RRA:MAX:0.5:5:2016')	
			if rrd:
				print rrdtool.error()
