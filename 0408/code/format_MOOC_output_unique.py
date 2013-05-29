#! /usr/bin/python

# Format MOOC_output_unique as the format required by Brain and Ping:
# DocID\tQuery\tDB\tPublications\tSource\tDate

import os
import re
import sys

fin = open("/Users/chhuang/stick/0408/MOOC_output_unique.txt", "r")
lines = fin.readlines()
fin.close()

for line in lines:
	line = line.rstrip()
	itms = lint.split("\t")
	
	docID = itms[0]
	date = itms[1]
	query = 'ft("MOOC")'
	db = "Proquest"
	publication_title = 
	
