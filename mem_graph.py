#!/usr/bin/python
import rrdtool
import time

class MemGraph:
	title=''
	rrdPath=''
	picPaht=''

	def __init__(self,title,rrdPath,picPath):
		self.title = title
		self.rrdPath = rrdPath
		self.picPath = picPath

	def graph(self):
		rrdtool.graph(self.picPath,'--start','-1d','--vertical-label=byte','--x-grid','MINUTE:12:HOUR:1:HOUR:1:0:%H',\
		'--width','650','--height','230','--title',self.title,
		"DEF:eden_space="+self.rrdPath+":eden_space:AVERAGE",
		"DEF:survivor_space="+self.rrdPath+":survivor_space:AVERAGE",
		"DEF:tenured_gen="+self.rrdPath+":tenured_gen:AVERAGE",
		"DEF:code_cache="+self.rrdPath+":code_cache:AVERAGE",
		"DEF:perm_gen="+self.rrdPath+":perm_gen:AVERAGE",
		"CDEF:total=eden_space,survivor_space,tenured_gen,code_cache,perm_gen,+,+,+,+",
		"AREA:perm_gen#FFDC36:perm_gen",
		"AREA:code_cache#FF0000:code_cache:STACK",
		"AREA:eden_space#0000FF:eden_space:STACK",
		"AREA:survivor_space#FF00FF:survivor_space:STACK",
		"AREA:tenured_gen#00FF00:tenured_gen:STACK",
		"COMMENT:\\r",
		"COMMENT:\\r",
		"GPRINT:eden_space:MAX:Eden Space\: %6.4lf %Sbyte",
		"COMMENT:  ",
		"GPRINT:survivor_space:MAX:Survivor Space\: %6.4lf %Sbyte",
		"COMMENT:  ",
		"GPRINT:tenured_gen:MAX:Tenured Gen\: %6.4lf %Sbyte",
		"COMMENT:  ",
		"GPRINT:code_cache:MAX:Code Cache\: %6.4lf %Sbyte",
		"COMMENT:  ",
		"GPRINT:perm_gen:MAX:Perm Gen\: %6.4lf %Sbyte")


memGraph = MemGraph('Tomcat mem usage ('+time.strftime('%Y-%m-%d',time.localtime(time.time()))+')','/home/brian/dev/python/tomcat/mem.rrd','/home/brian/dev/python/tomcat/mem.png')
memGraph.graph()




