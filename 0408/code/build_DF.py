#! /usr/bin/python
# Need to rewrite this shit, need to search for all name variations and include them. 

# Extract document frequency for organizations

import os
import re
import sys

# Keep all the name variations
fin = open(sys.argv[1], "r")
lines = fin.readlines()
fin.close()

ids = set()
orgs = set()
name_dic = {}

for line in lines:
	line = line.rstrip()
	if "REMOVE" not in line:
		itms = line.split("::")
		name_dic[itms[0]] = itms[1]
		orgs.add(itms[0])


# ID Org
fin = open(sys.argv[2], "r")
lines = fin.read().split("\n")
fin.close()


for line in lines:
	line = line.rstrip()
	itms = line.split("\t")
	if len(itms) < 4 and len(itms)>1:
		#print itms
		id = itms[0]
		org = itms[1]
		ids.add(id)
		orgs.add(org)
		name_dic[org] = org
	

pre_id = 0
content = ""
# new ID Org
fout = open(sys.argv[3],"w")
for id in ids:
	id_org = set()
	for org in orgs:
		# txt folder 
		fin = open(sys.argv[4]+"/"+str(id)+".txt", "r")
		content = fin.read()
		fin.close()
		pre_id = id
		
		itms = content.split()
		span = len(org.split())
		#is_found = False
		for i in range(len(itms)):
#			print " ".join(itms[i:i+span])
			if org in " ".join(itms[i:i+span]):
				#fout.write(str(id)+"\t"+org+"\t"+" ".join(itms[i-5:i+6])+"\n")
				id_org.add(str(id)+"\t"+name_dic[org]+"\n")
		#		is_found = True
				break
		#if is_found == False:
		#	print id, org
	
	for key in id_org:
		fout.write(key)
	
fout.close()
