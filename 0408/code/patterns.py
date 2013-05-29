#! /usr/bin/python

import os
import sys
import re
import glob
import operator

files = glob.glob("/Users/chhuang/stick/0408/content/*")

trigram_count = {}

for file in files:
	fin = open(file,"r")
	lines = fin.readlines()
	fin.close()

	for line in lines:
		line = line.lower()
		if "big data" in line:
			line  = line.rstrip()
			itms = line.split(" ")
			trigrams = zip(itms,itms[1:],itms[2:])
			for trigram in trigrams:
				if "big" in trigram[0] and "data" in trigram[1]:
					if trigram in trigram_count.keys():
						trigram_count[trigram] += 1	
					else:
						trigram_count[trigram] = 1
			
for trigram in sorted(trigram_count.iteritems(), key=operator.itemgetter(1), reverse=True):
	print trigram

