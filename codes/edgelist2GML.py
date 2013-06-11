#! /usr/bin/python
# This script transforms edgelist format to GraphML format for NodeXL to use
# NetworkX package is used to do the transformation

import os
import re
import sys
import networkx as nx
import glob

files = glob.glob(sys.argv[1])
folder_loc = sys.argv[2]
for file in files:
	G=nx.Graph()

	fh = open(file, 'rb')
	for line in fh.readlines():
		itms = line.split("\t")
		if len(itms) == 3:
			G.add_edge(itms[0], itms[1], weight=int(itms[2]))
			
		if len(itms) == 2:
			G.add_node(itms[0])
	fh.close()

	#print G.nodes()
	#print G.edges(data = True)
	file_name = ".".join(file.split(".")[:-1])
	nx.write_graphml(G, file_name+".graphml")




