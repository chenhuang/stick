#!/usr/bin/bash

cat /Users/chhuang/stick/0504/meta-data/*_1 > /Users/chhuang/stick/0504/MOOC_metadata
cat /Users/chhuang/stick/0504/id_org/* | sort | uniq | sort -nr -k2 -t"	" > /Users/chhuang/stick/0504/MOOC_ID_Org
