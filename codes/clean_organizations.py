#! /opt/local/bin/python2.7
# This script takes modified, manually checked output from identify_dup_organizations.py, and remove the duplicated organizations names based on the list

import os
import sys
import re

# First load the list of organization names that are to remove
fin = open(sys.argv[1], "r")
lines = fin.readlines()
fin.close()

#print lines

remove_list = []
replace_list = {}

for line in lines:
    line = line.rstrip()
    itms = line.split("::")
    if itms[1] == "REMOVE":
        remove_list.append(itms[0])
    else:
        replace_list[itms[0]] = itms[1]

# Now clean the organization list according to the results
fin = open(sys.argv[2], "r")
lines = fin.readlines()
fin.close()

output_set = set()

for line in lines:
    line = line.rstrip()
    itms = line.split("\t")

    print line
    if itms[1] in remove_list:
        continue
    elif itms[1] in replace_list:
       output_set.add(itms[0]+"\t"+replace_list[itms[1]])
    else:
       output_set.add(line)
    
fout = open(sys.argv[2]+"_1","w")
while len(output_set) > 0:
    itm = output_set.pop()
    if ":" in itm:
        sub_itm0 = itm.split("\t")[0]
        sub_itms = itm.split("\t")[1].split(":")
        
        for i in sub_itms:
            fout.write(sub_itm0+"\t"+i+"\n")
    else:
        fout.write(itm+"\n")
fout.close()





