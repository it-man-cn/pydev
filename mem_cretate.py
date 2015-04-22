#!/usr/bin/python
import rrdtool
import time

cur_time=str(int(time.time()))

mem=rrdtool.create('/home/brian/dev/python/tomcat/mem.rrd','--step','60','--start',cur_time,
	'DS:eden_space:GAUGE:600:0:U',
	'DS:survivor_space:GAUGE:600:0:U',
	'DS:tenured_gen:GAUGE:600:0:U',
	'DS:code_cache:GAUGE:600:0:U',
	'DS:perm_gen:GAUGE:600:0:U',
	'RRA:AVERAGE:0.5:1:10080',
	'RRA:AVERAGE:0.5:5:2016',
	'RRA:MAX:0.5:1:10080',
	'RRA:MAX:0.5:5:2016')


if mem:
	print rrdtool.error()

