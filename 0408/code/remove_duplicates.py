#! /usr/bin/python

# Identify duplicated articles and aggregate them into sets. 

import os
import re
import sys
import glob

from datetime import datetime

files = glob.glob(sys.argv[1])

duplicated_ids = {}

# Record an article ID that is the most appropriate. 
signature_list = []

# A quick and dirty way to build signature set for a content
def extract_signature(content):
	content = content.rstrip()
	itms = content.split(" ")
	content_set = set()
	for itm in itms:
		itm = itm.lower()
		itm = itm.strip(",")
		itm = itm.strip(".")
		itm = itm.strip("!")
		if itm in content_set:
			itm += " "
			while itm in content_set:
				itm += " "
			content_set.add(itm+" ")
		else:
			content_set.add(itm)

	return content_set
	

def compare_similarity(content1, content2):
	return float(len(content1.intersection(content2)))/float(len(content1.union(content2)))

for file in files:
	file_id = (file.split("/")[-1]).split(".")[0]
	fin = open(file, "r")
	content = fin.read()
	fin.close()
	
	content_sign = extract_signature(content)
	is_unique = True
	
	for sign in signature_list:
		id = sign[0]
		id_content = sign[1]

		sim = compare_similarity(id_content, content_sign)
		print sim

		if sim > 0.7:
			duplicated_ids[id].append(file_id)
			is_unique = False
			break

	if is_unique == True:
		duplicated_ids[file_id] = [file_id]
		signature_list.append((file_id,content_sign))

# Remove duplicates and return the cleaned set of IDs:

#for id in duplicated_ids:
#	print " ".join(duplicated_ids[id])

if 1:
	# Location of the meta-data
	fin = open(sys.argv[2], "r")
	lines = fin.readlines()
	fin.close()

	fout = open(sys.argv[2]+"_1", "w")
	id_line = {}
	for line in lines:
		line = line.rstrip()
		itms = line.split("\t")
		id_line[itms[0]] = line

	for id in duplicated_ids.keys():
		if len(duplicated_ids[id]) == 1:
			fout.write(id_line[id]+"\n")
		else:
			latest_time = datetime.strptime("Jan 1, 1990", "%b %d, %Y")
			latest_id = ""
			for i in duplicated_ids[id]:
				date_string = id_line[i].split("\t")[6]
				date_object = datetime.strptime(date_string, "%b %d, %Y")
				if date_object >= latest_time:
					latest_time = date_object
					latest_id = i

			fout.write(id_line[latest_id]+"\n")

	fout.close()
