#! /usr/bin/python
# USAGE: Extract Full texts from Jia's input
# INPUT: Take a list of Jia's files "/home/chhuang/stick/DataForCody/corpus/*" 
# OUTPUT: meta data about the files as meta_data, and full texts of the articles.

import sys
import os
import re
import glob
import codecs

from HTMLParser import HTMLParser

class articleExtractor(HTMLParser):
	def reset(self):
		HTMLParser.reset(self)
		self.tags = set(["organization", "person"])
		self.current_tag = "NULL"
		self.organizations = set()

	def handle_starttag(self, tag, attrs):
		if tag == "organization":
			self.current_tag = "organization"
		if tag == "person":
			self.current_tag = "person"

	def handle_endtag(self, tag):
		if tag == "organization":
			self.current_tag = "NULL"
		if tag == "person":
			self.current_tag = "NULL"
	

	def handle_data(self, text):
		text = text.strip()
		#print len(text)
		
		if self.current_tag == "organization":
			self.organizations.add(text)

files = glob.glob(sys.argv[1])
fout = open(sys.argv[2], "w")

for file in files:
	a = articleExtractor()
	fin = open(file, "r")
	source = fin.read()
	fin.close()

	a.file_name = file
	a.id = file.split("/")[-1].split(".")[0]
	a.feed(source)
	
	for i in a.organizations:
		fout.write(a.id+"\t"+i+"\n")
fout.close()

