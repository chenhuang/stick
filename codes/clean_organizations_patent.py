#! /opt/local/bin/python2.7
# This script takes modified, manually checked output from identify_dup_organizations.py, and remove the duplicated organizations names based on the list

import os
import sys
import re

# First load the list of organization names that are to remove
fin = open(sys.argv[1], "r")
lines = fin.readlines()
fin.close()

remove_list = []
replace_list = {}

index = 0

for line in lines:
    index += 1
    line = line.rstrip()
    itms = line.split("::")
    try:
        if itms[1] == "REMOVE":
            remove_list.append(itms[0])
        else:
            replace_list[itms[0]] = itms[1]
    except:
        print "REMOVE Error: "+line+" line number: " + str(index)
        sys.exit(0);

# Now clean the organization list according to the results
fin = open(sys.argv[2], "r")
lines = fin.readlines()
fin.close()

output_set = set()

for line in lines:
    line = line.rstrip()
    itms = line.split("\t")

    if itms[2] in remove_list:
        continue
    elif itms[2] in replace_list:
       output_set.add(itms[0]+"\t"+itms[1]+"\t"+replace_list[itms[2]])
    else:
       output_set.add(line)
    
while len(output_set) > 0:
    itm = output_set.pop()
    print itm





