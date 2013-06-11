#! /usr/bin/python
# This script do what ../merge.sh does

import os
import re
import sys
import glob

folder_loc = sys.argv[1]

# merge metadata
metadata_files = glob.glob(folder_loc+"/*_1")

content = ""
for file in metadata_files:
	fin = open(file,"r")
	content += fin.read()
	fin.close()
	
fout = open(sys.argv[2],"w")
fout.write(content)
fout.close()

# merge id_org
id_org_content = ""
id_org_files = glob.glob(folder_loc+"/id_org/*")
for file in id_org_files:
	fin = open(file,"r")
	id_org_content += fin.read()
	fin.close()

lines = id_org_content.split("\n")	
for line in lines:
	itms = line.split('\t')
	id = itms[1]




