#!/usr/bin/python
import rrdtool
import time

class MemGraph:

	def graph(self,host,rrdPath,picPath):
		title = 'Tomcat '+host+' mem usage ('+time.strftime('%Y-%m-%d',time.localtime(time.time()))+')'
		rrdtool.graph(picPath,'--start','-1d','--vertical-label=byte','--x-grid','MINUTE:12:HOUR:1:HOUR:1:0:%H',\
		'--width','650','--height','230','--title',title,
		"DEF:maxThreads="+rrdPath+":maxThreads:AVERAGE",
		"DEF:currentThreadsBusy="+rrdPath+":currentThreadsBusy:AVERAGE",
		"DEF:currentThreadCount="+rrdPath+":currentThreadCount:AVERAGE",
		"DEF:connectionCount="+rrdPath+":connectionCount:AVERAGE",
		"LINE1:currentThreadsBusy#FF0000:currentThreadsBusy",
		"LINE1:currentThreadCount#0000FF:currentThreadCount",
		"LINE1:connectionCount#FF00FF:connectionCount",
		"COMMENT:\\r",
		"COMMENT:\\r",
		"GPRINT:maxThreads:MAX:maxThreads\: %6.0lf %S",
		"COMMENT:  ",
		"GPRINT:currentThreadsBusy:MAX:currentThreadsBusy\: %6.0lf %S",
		"COMMENT:  ",
		"GPRINT:currentThreadCount:MAX:currentThreadCount\: %6.0lf %S",
		"COMMENT:  ",
		"GPRINT:connectionCount:MAX:connectionCount\: %6.0lf %S")
