#!/usr/bin/python
import rrdtool
import time,psutil
from jmx4py.jolokia.client import *

class MemUpdate:

	def update(self,host,port,rrdPath):
		proxy = JmxClient((host,port))
		resp = proxy.read("java.lang:type=MemoryPool,name=PS Eden Space",["Usage"])
		eden_space = resp.value.get("Usage")["used"]
		resp = proxy.read("java.lang:type=MemoryPool,name=PS Survivor Space",["Usage"])
		survivor_sapce = resp.value.get("Usage")["used"]
		resp = proxy.read("java.lang:type=MemoryPool,name=PS Old Gen",["Usage"])
		old_gen = resp.value.get("Usage")["used"]
		resp = proxy.read("java.lang:type=MemoryPool,name=Code Cache",["Usage"])
		code_cache = resp.value.get("Usage")["used"]
		resp = proxy.read("java.lang:type=MemoryPool,name=PS Perm Gen",["Usage"])
		perm_gen = resp.value.get("Usage")["used"]
		now = int(time.time())
		update=rrdtool.updatev(rrdPath,'%s:%s:%s:%s:%s:%s' % 
			(str(now),str(eden_space),str(survivor_sapce),str(old_gen),str(code_cache),str(perm_gen)))
		print update
