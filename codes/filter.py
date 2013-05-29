#! /usr/bin/python

# This script filters all content of the messages and escapse error inputs

import os
import re
import sys
import glob

files = glob.glob(sys.argv[1])
output_folder = sys.argv[2]

escape_list = {"&":""}

for file in files:
    file_name = file.split("/")[-1]
    fout = open(output_folder+"/"+file_name, "w")

    fin = open(file, "r")
    lines = fin.readlines()
    fin.close()

    for line in lines:
        for key in escape_list.keys():
            if key in line:
                line = re.sub(key, escape_list[key], line)

        fout.write(line)
    fout.close()

