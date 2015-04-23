#!/usr/bin/python
import rrdtool
import os
import time

class CreateMemGraph:

	def create(self,rrdPath,step,start):
		if os.path.exists(rrdPath):
			return
		else:
			rrd=rrdtool.create(rrdPath,'--step',step,'--start',start,
			'DS:eden_space:GAUGE:600:0:U',
			'DS:survivor_space:GAUGE:600:0:U',
			'DS:tenured_gen:GAUGE:600:0:U',
			'DS:code_cache:GAUGE:600:0:U',
			'DS:perm_gen:GAUGE:600:0:U',
			'RRA:AVERAGE:0.5:1:10080',
			'RRA:AVERAGE:0.5:5:2016',
			'RRA:MAX:0.5:1:10080',
			'RRA:MAX:0.5:5:2016')	
			if rrd:
				print rrdtool.error()

cur_time=str(int(time.time()))
createGraph = CreateMemGraph()
createGraph.create('/home/brian/dev/python/tomcat/mem.rrd',60,cur_time)






