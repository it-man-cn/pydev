#!/usr/bin/python
import mem_graph
import thread_graph

base = '/home/brian/monitor/tomcat/'
server = 'wifi'
memGraph = mem_graph.MemGraph()
memGraph.graph(server,base+'/'+server+'_mem.rrd',base+'/'+server+'_mem.png')

memGraph = thread_graph.MemGraph()
memGraph.graph(server,base+'/'+server+'_thread.rrd',base+'/'+server+'_thread.png')