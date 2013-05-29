#! /usr/bin/python

# This script loads in a id_org file from: /Users/chhuang/stick/0504/MOOC_ID_Org
# Output network file in the format of: org1\torg2\b

import os
import re
import sys

fin = open("/Users/chhuang/stick/0504/MOOC_ID_Org", "r")
lines = fin.readlines()
fin.close()
id_orgs = {}

for line in lines:
	line = line.rstrip()
	itms = line.split("\t")

	org = itms[0]
	id = itms[1]
	
	if id not in id_orgs.keys():
		id_orgs[id] = set()
	id_orgs[id].add(org)

fout = open("/Users/chhuang/stick/0504/org_org.txt", "w")
org_orgs = set()

for id in id_orgs.keys():
	orgs = list(id_orgs[id])
	for i in range(len(orgs)-1):
		for j in range(i+1, len(orgs)):
			#fout.write(orgs[i]+"\t"+orgs[j]+"\n")
			edge1 = orgs[i]+"\t"+orgs[j]
			edge2 = orgs[j]+"\t"+orgs[i]
			#org_orgs.add(orgs[i]+"\t"+orgs[j])
			#org_orgs.add(orgs[j]+"\t"+orgs[i])
			if edge1 not in org_orgs: 
				if edge2 not in org_orgs:
					org_orgs.add(edge1)
				
			if edge2 not in org_orgs:
				if edge1 not in org_orgs:
					org_orgs.add(edge2)

for org_org in org_orgs:
	fout.write(org_org+"\n")
fout.close()

