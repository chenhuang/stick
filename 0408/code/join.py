#! /usr/bin/python

import os
import sys

#meta-data
fin = open(sys.argv[1], "r")
lines = fin.readlines()
fin.close()

ID_line = {}

for line in lines:
	line = line.rstrip()
	itms = line.split("\t")
	ID_line[itms[0]] = line

	
#ID-org
fin = open(sys.argv[2], "r")
lines = fin.readlines()
fin.close()

fout = open(sys.argv[3],"w")

for line in lines:
	line = line.rstrip()
	itms = line.split("\t")

	id = itms[0]
	org = itms[1]
	meta_data = ID_line[itms[0]].rstrip().split("\t")
	fout.write(itms[1]+"\t"+itms[0]+"\t"+meta_data[6]+"\t"+meta_data[5]+"\t"+meta_data[4]+"\n")

fout.close()
