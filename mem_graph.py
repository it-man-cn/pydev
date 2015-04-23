#!/usr/bin/python
import rrdtool
import time

class MemGraph:

	def graph(self,host,rrdPath,picPath):
		title = 'Tomcat '+host+' mem usage ('+time.strftime('%Y-%m-%d',time.localtime(time.time()))+')'
		rrdtool.graph(picPath,'--start','-1d','--vertical-label=byte','--x-grid','MINUTE:12:HOUR:1:HOUR:1:0:%H',\
		'--width','650','--height','230','--title',title,
		"DEF:eden_space="+rrdPath+":eden_space:AVERAGE",
		"DEF:survivor_space="+rrdPath+":survivor_space:AVERAGE",
		"DEF:tenured_gen="+rrdPath+":tenured_gen:AVERAGE",
		"DEF:code_cache="+rrdPath+":code_cache:AVERAGE",
		"DEF:perm_gen="+rrdPath+":perm_gen:AVERAGE",
		"CDEF:total=eden_space,survivor_space,tenured_gen,code_cache,perm_gen,+,+,+,+",
		"AREA:code_cache#FF0000:code_cache",
		"AREA:perm_gen#FFDC36:perm_gen:STACK",
		"AREA:survivor_space#FF00FF:survivor_space:STACK",
		"AREA:tenured_gen#00FF00:tenured_gen:STACK",
		"AREA:eden_space#0000FF:eden_space:STACK",
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
