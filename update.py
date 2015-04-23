#!/usr/bin/python
import thread_update
import mem_update

base='/home/brian/monitor/tomcat/'
server = 'wifi'
host = 'localhost'
port = '8080'
threadUpdate = thread_update.Threadpdate()
threadUpdate.update(host,port,base+'/'+server+'_thread.rrd')

memUpdate = mem_update.MemUpdate()
memUpdate.update(host,port,base+'/'+server+'_mem.rrd')
