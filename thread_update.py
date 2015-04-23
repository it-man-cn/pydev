#!/usr/bin/python
import rrdtool
import time,psutil
from jmx4py.jolokia.client import *

class Threadpdate:

	def update(self,host,port,rrdPath):
		proxy = JmxClient((host,port))
		proxy = JmxClient((host,port))
		resp = proxy.read("Catalina:type=ThreadPool,name=\"http-nio-"+port+"\"",["maxThreads","currentThreadsBusy","currentThreadCount","connectionCount"])
		now = int(time.time())
		maxThreads = resp.value["maxThreads"]
		currentThreadsBusy = resp.value["currentThreadsBusy"]
		currentThreadCount = resp.value["currentThreadCount"]
		connectionCount = resp.value["connectionCount"]
		update=rrdtool.updatev(rrdPath,'%s:%s:%s:%s:%s' % 
			(str(now),str(maxThreads),str(currentThreadsBusy),str(currentThreadCount),str(connectionCount)))
		print update
