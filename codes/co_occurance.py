#! /usr/bin/python
# Compute organziations' quarterly co-occurance frequency at paragraph level

import os
import re
import sys

# Keep all the name variations
fin = open(sys.argv[1], "r")
lines = fin.readlines()
fin.close()

name_dic = {}
name_var = {}

for line in lines:
	line = line.rstrip()
	if "REMOVE" not in line:
		itms = line.split("::")
		
		sub_itms = []
		if ":" in itms[1]:
			sub_itms = itms[1].split(":")
		else:
			sub_itms.append(itms[1])
		
		for sub_itm in sub_itms:
			name_dic[itms[0]] = sub_itm
			if sub_itm not in name_var.keys():
				name_var[sub_itm] = set()
				name_var[sub_itm].add(sub_itm)

			name_var[sub_itm].add(itms[0])
			


# ID meta-data
fin = open(sys.argv[2], "r")
lines = fin.read().split("\n")
fin.close()

id_date = {}

# these are all the months in the MOOC data, need revision for other type of data
#month_quarter = {'Aug':3,'Dec':4,'Feb':1,'Jan':1,'Mar':1,'May':2,'Nov':4,'Sep':3}
month_quarter = {'April':2,'August':3,'December':4,'February':1,'January':1,'July':3,'June':2,'March':1,'May':2,'November':4,'October':4,'September':3}

for line in lines:
	line = line.rstrip()
	itms = line.split("\t")
	if len(itms) > 1:
		id = itms[0]
		date = itms[6]

		# decide the quarter of the date:
		date_itms = date.split(" ")
		month = date_itms[0]
		year = date_itms[2]
		quarter = month_quarter[month]
		id_date[id]=str(year)+"Q"+str(month_quarter[month])
	
# ID Org
fin = open(sys.argv[3], "r")
lines = fin.read().split("\n")
fin.close()

# txt folder location
txt_loc = sys.argv[4]

# check existence
def isExist(org, txt):
	for org_1 in name_var[org]:
		# handle the case when the organization name is edX and happens when EdX is the head word of the text
		if org_1[0].upper()+org_1[1:] in txt[0:len(org_1)]:
			return True
		if org_1 in txt:
			#			print org_1+"\t: "+ txt
			return True
	return False

# now run the co-occurance process
# Note that the file should be sorted by document ID
pre_id = 0
quarter_orgs = {}
id_orgs = []

for line in lines:
	line = line.rstrip()
	itms = line.split("\t")

	if len(itms) == 1:
		continue
	
	id = itms[1]
	org = itms[0]
	name_dic[org] = org
	if org not in name_var.keys():
		name_var[org] = set()
	name_var[org].add(org)

	if pre_id == 0:
		pre_id = id
		id_orgs.append(org)
	elif pre_id != id:
		#print pre_id,id_orgs
	
		# open txt file
		fin = open(txt_loc+"/"+str(pre_id)+".txt","r")
		txt_lines = fin.readlines()
		fin.close()

		#check paragraph wise
		for txt_line in txt_lines:
			# check for each org
			for i in range(len(id_orgs)):
				# if the org is in
				if isExist(id_orgs[i],txt_line):
					# check for every other org
					is_alone = True
					for j in range(len(id_orgs)):
						if i == j:
							continue
						# check for the org
						if isExist(id_orgs[j],txt_line):
							#print txt_line
							is_alone = False
							# count frequency
							if id_date[pre_id] not in quarter_orgs.keys():
								quarter_orgs[id_date[pre_id]] = {}
							if id_orgs[i]+"\t"+id_orgs[j] not in quarter_orgs[id_date[pre_id]].keys():
								quarter_orgs[id_date[pre_id]][id_orgs[i]+"\t"+id_orgs[j]] = 0
							quarter_orgs[id_date[pre_id]][id_orgs[i]+"\t"+id_orgs[j]] += 1
							print pre_id +"\t"+ id_orgs[i]+"\t"+id_orgs[j]
				#print quarter_orgs[id_date[pre_id]][id_orgs[i]+"\t"+id_orgs[j]]
					if is_alone == True:
						#						print txt_line
						#print pre_id+"\t"+id_orgs[i]
						if id_date[pre_id] not in quarter_orgs.keys():
							quarter_orgs[id_date[pre_id]] = {}
						if id_orgs[i] not in quarter_orgs[id_date[pre_id]].keys():
							quarter_orgs[id_date[pre_id]][id_orgs[i]] = 0
						quarter_orgs[id_date[pre_id]][id_orgs[i]] += 1
		#print quarter_orgs[id_date[pre_id]][id_orgs[i]]
		pre_id = id
		id_orgs = [org]
	else:
		id_orgs.append(org)
		#print pre_id,id_orgs
	
# open txt file
fin = open(txt_loc+"/"+str(pre_id)+".txt","r")
txt_lines = fin.readlines()
fin.close()

#check paragraph wise
for txt_line in txt_lines:
	# check for each org
	for i in range(len(id_orgs)):
		# if the org is in
		if isExist(id_orgs[i],txt_line):
			# check for every other org
			is_alone = True
			for j in range(len(id_orgs)):
				if i == j:
					continue
				# check for the org
				if isExist(id_orgs[j],txt_line):
					#print txt_line
					is_alone = False
					# count frequency
					if id_date[pre_id] not in quarter_orgs.keys():
						quarter_orgs[id_date[pre_id]] = {}
					if id_orgs[i]+"\t"+id_orgs[j] not in quarter_orgs[id_date[pre_id]].keys():
						quarter_orgs[id_date[pre_id]][id_orgs[i]+"\t"+id_orgs[j]] = 0
					quarter_orgs[id_date[pre_id]][id_orgs[i]+"\t"+id_orgs[j]] += 1
					print pre_id +"\t"+ id_orgs[i]+"\t"+id_orgs[j]
		#print quarter_orgs[id_date[pre_id]][id_orgs[i]+"\t"+id_orgs[j]]
			if is_alone == True:
				#						print txt_line
				#print pre_id+"\t"+id_orgs[i]
				if id_date[pre_id] not in quarter_orgs.keys():
					quarter_orgs[id_date[pre_id]] = {}
				if id_orgs[i] not in quarter_orgs[id_date[pre_id]].keys():
					quarter_orgs[id_date[pre_id]][id_orgs[i]] = 0
				quarter_orgs[id_date[pre_id]][id_orgs[i]] += 1

# output network by quarter
# network folder location
network_loc = sys.argv[5]
orgs_set = set()
for quarter in quarter_orgs.keys():
	fout = open(network_loc+"/"+quarter+".txt", "a")
	for orgs in quarter_orgs[quarter].keys():
		org_itms = orgs.split("\t")
		if len(org_itms) == 2:
			if org_itms[1]+"\t"+org_itms[0] not in orgs_set:
				fout.write(orgs+"\t"+str(quarter_orgs[quarter][orgs])+"\n")
				orgs_set.add(orgs)
		else:
			fout.write(orgs+"\t"+str(quarter_orgs[quarter][orgs])+"\n")
	#		fout.write(orgs+"\n")
	fout.close()



