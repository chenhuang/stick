#! /usr/bin/python

# This script addes header to 
# INPUT1: folder to the dataset
# INPUT2: trajectory input file
# INPUT3: output folder name
# OUTPUT: files that have the STICK header, and also have the trajectory substituted.

import os
import re
import sys
import glob

files = glob.glob(sys.argv[1])
trajectory_file = sys.argv[2]
output_folder = sys.argv[3]

fin = open(trajectory_file, "r")
lines = fin.readlines()
fin.close()

trajectory_hash = {}

for line in lines:
    line = line.strip()
    itms = line.split("\t")
    trajectory_hash[itms[0].lower().rstrip()] = itms[1]


for file in files:
    fin = open(file, "r")
    lines = fin.readlines()
    fin.close()

    file_name = file.split("/")[-1]

    fout = open(output_folder+"/"+file_name, "w")
    fout.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en"><head><link rel="stylesheet" type="text/css" href="http://stick.ischool.umd.edu/1024px.css" title="1024px" media="screen,projection" /><link rel="stylesheet" type="text/css" href="http://stick.ischool.umd.edu/style.css" title="1024px" media="screen,projection" /><title>STICK</title><head><script type="text/javascript" src="http://stick.ischool.umd.edu/lib/load.js"></script> <script type="text/javascript" src="http://stick.ischool.umd.edu/lib/jquery-1.8.0.min.js"></script> <script type="text/javascript"> $(document).ready(function() { draw_frame(); }); </script> </head> <body> <div class="center" id="wrap"> <div> <div class="SubNav"> <br /> <p><font size=2 px><a href="http://stick.ischool.umd.edu/index.htm">Home</a> &gt; <a href="http://stick.ischool.umd.edu/details.html">Details</a>&gt; <a href="http://stick.ischool.umd.edu/data_analysis_and_visualization.html">Data Analysis and Visualization </a> </font></p> <p> </p> <br /> </div> <p></p> <h2><font color="#006699">Title</font></h2>\n') 

    for line in lines:
        if "C:\Users\Jia Sun" in line:
            m=re.search('(C:\\\Users.*).*?"',line)
            location = m.group(1)
            location = location.split("/")[-1].lower()

            if location not in trajectory_hash.keys():
                print "ERROR: " + location + " not in trajectory hash keys"
                #sys.exit(0)
            else:
                line = re.sub("<script type.*</script>", trajectory_hash[location], line)

            fout.write(line)
        else:
            fout.write(line)

    
    fout.write('</div></div></body></html>')

    fout.close()



