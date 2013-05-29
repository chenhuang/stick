#! /usr/bin/python

# Extract the sample sentence for the organization names
import os
import re
import sys

fin = open("/Users/chhuang/stick/0408/MOOC_ID_Org.txt", "r")
lines = fin.readlines()
fin.close()

pre_id = 0
content = ""
fout = open("/Users/chhuang/stick/0408/MOOC_ID_Org_Sample.txt","w")
for line in lines:
	line = line.rstrip()
	itms = line.split("\t")

	id = itms[0]
	org = itms[1]

	if id != pre_id:
		fin = open("/Users/chhuang/stick/0408/MOOC_content/"+str(id)+".txt", "r")
		content = fin.read()
		fin.close()
		pre_id = id
		
		itms = content.split()
		span = len(org.split())
		is_found = False
		for i in range(len(itms)):
#			print " ".join(itms[i:i+span])
			if org in " ".join(itms[i:i+span]):
				fout.write(line+"\t"+" ".join(itms[i-5:i+6])+"\n")
				is_found = True
				break
		if is_found == False:
			print id, org
	else:	
		itms = content.split()
		span = len(org.split())
		is_found = False
		for i in range(len(itms)):
#			print " ".join(itms[i:i+span])
			if org in " ".join(itms[i:i+span]):
				fout.write(line+"\t"+" ".join(itms[i-5:i+6])+"\n")
				is_found = True
				break
		if is_found == False:
			print id, org
	
fout.close()
