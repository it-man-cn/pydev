#!/usr/bin/python
import thread_create
import mem_create

base='/home/brian/monitor/tomcat/'
server = 'wifi'
threadCreate = thread_create.CreateThreadGraph()
threadCreate.create(base+'/'+server+'_thread.rrd')

memCreate = mem_create.CreateMemGraph()
memCreate.create(base+'/'+server+'_mem.rrd')