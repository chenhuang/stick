#! /usr/bin/python

# Extract organization and people names from the corpus
# Input: NER output folder location
# Output: Concept\tOrganization\tDF\tTotal Term Frequency\tSentence

import os
import re
import sys
import glob

files = glob.glob("/Users/chhuang/stick/0408/MOOC_NER_Uniq/*")


DF = {}
TTF = {}
Sentence = {}
organizations = set()
persons = set()


for file in files:
	fin = open(file, "r")
	lines = fin.readlines()
	fin.close()
	DF_set = set()
	org_stack = []
	ppl_stack = []

	for line in lines:
		line = line.rstrip()
		itms = line.split(" ")

		i = 0
		while i < len(itms):
			if '<ORGANIZATION>' in itms[i]:
				if '</ORGANIZATION>' in itms[i]:
					print itms[i]
					entity_name = itms[i][14:-15]
					print entity_name
				else:
					entity_name = itms[i][14:]
					while '</ORGANIZATION>' not in itms[i]:
						i+=1
						entity_name += " "+itms[i]
					entity_name += " "+itms[i][0:-15]
				
				organizations.add(entity_name)

				Sentence[entity_name] = line

				if entity_name in TTF.keys():
					TTF[entity_name] += 1
				else:
					TTF[entity_name] = 1
			
				if entity_name not in DF_set:
					if entity_name in DF.keys():
						DF[entity_name] += 1
					else:
						DF[entity_name] = 1
					DF_set.add(entity_name)
				
			if '<PERSON>' in itms[i]:
				if '</PERSON>' in itms[i]:
					entity_name = itms[i][8:-9]
				else:
					entity_name = itms[i][8:]
					while '</PERSON>' not in itms[i]:
						i+=1
						entity_name += " "+itms[i]
					entity_name += " "+itms[i][0:-9]

				persons.add(entity_name)
			
				Sentence[entity_name] = line

				if entity_name in TTF.keys():
					TTF[entity_name] += 1
				else:
					TTF[entity_name] = 1
			
				if entity_name not in DF_set:
					if entity_name in DF.keys():
						DF[entity_name] += 1
					else:
						DF[entity_name] = 1
					DF_set.add(entity_name)
			i += 1

for key in organizations:
	print key+"\t"+str(DF[key])+"\t"+str(TTF[key])
			
#print "----------"

#for key in persons:
#	print key+"\t"+str(DF[key])+"\t"+str(TTF[key])+Sentence[key]



