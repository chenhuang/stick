#! /opt/local/bin/python2.7
# This script takes input from a list of documentID\torganization, and identify the following list of errors automatically:
# 1. Duplicated names: New York Times vs New York Times Company 
# 2. Non-sense names: Organziations that appeared rarely in the corpus (This has been shown to be not very useful)
# 3. Abbrv.ed organization names: short, totally capitalized organziation names
# OUTPUT: list of possible erratic organization names

import os
import re
import sys
import nltk
from numpy import *

fin = open(sys.argv[1], "r")
lines = fin.readlines()
fin.close()

Uppercases = set(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
abbvs = set()

index = 0

fdist = nltk.FreqDist()
for line in lines:
    index += 1
    line = line.rstrip()
    itms = line.split("\t")
    if (len(itms) != 3):
        raise Exception("Input data format error", "required format: id\torg"+line+" at:" + str(index))
    itm_org = itms[2]

    # Identify if it's a abbrv.ed name
    not_abbv = False
    for i in range(len(itm_org)):
        if itm_org[i] not in Uppercases:
            not_abbv = True
    if not_abbv is False:
        abbvs.add(itm_org)
        #print itm_org

    # Identify rare org names
    if not_abbv is True:
        fdist.inc(itm_org)
     
# After collected all the org names, first identify the list of organization names that are  
# Does not work well, so commented out
if 0:
    value_size = fdist.B()
    threshold = int(float(max(fdist.values())) * 0.05)
    rare_terms = [i for i in fdist.keys() if fdist.freq(i) <= threshold]
    print fdist.keys()
    print fdist.values()

# Now collect similar terms
def similarity(term1, term2):
   term1_set = set()
   term2_set = set()
   for i in range(len(term1)):   
        term1_set.add(term1[i])
        if i+2 <= len(term1):
            term1_set.add(term1[i:i+2])
   for i in range(len(term2)):
        term2_set.add(term2[i])
        if i+2 <= len(term2):
            term2_set.add(term2[i:i+2])

   term1_set_size = len(term1_set)
   term2_set_size = len(term2_set)

   term1_term2 = term1_set.intersection(term2_set)
   term1_term2_set_size = len(term1_term2)
   

   similarity_val = float(term1_term2_set_size) / float(term1_set_size+term2_set_size-term1_term2_set_size)
   
   if 0:
       if similarity_val > 0.6:
            print term1
            print term2
            print term1_set
            print term2_set
            print term1_term2

   return similarity_val
    
# Now circule through all the terms and identify similar terms
term_pair_dict = {}
term_pair_dist = nltk.FreqDist()

fdist_key_len = len(fdist.keys())
duplicated_org_pair = {}
for i in range(fdist_key_len):
    for j in range(i+1,fdist_key_len):
        #term_pair_dist[(i,j)] = similarity(i,j)
        #val = nltk.metrics.jaccard_distance(i,j)
        term1 = fdist.keys()[i]
        term2 = fdist.keys()[j]
        val = similarity(term1,term2)
        term_pair_dict[(term1,term2)] = val
        term_pair_dist.inc(val)
        if val >= 0.5:
            if len(term1) > len(term2):
                duplicated_org_pair[term1] = term2
            else:
                duplicated_org_pair[term2] = term1

# Now produce a list of term pair to replace with:
for key in duplicated_org_pair.keys():
    print key+"::"+duplicated_org_pair[key]

while len(abbvs) > 0:
    org_name = abbvs.pop()
    print org_name+"::"+"REMOVE"


