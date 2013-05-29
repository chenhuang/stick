#/usr/bin/bash

for name in `cat /Users/chhuang/stick/entries_pr`; do
rm -rf '/Users/chhuang/stick/0523/txt/prnewswire/'$name &&
mkdir '/Users/chhuang/stick/0523/txt/prnewswire/'$name && 
/Users/chhuang/stick/codes/articleExtractor_pr.py '/Users/chhuang/stick/0523/raw/prnewswire/'$name'/*' $name '/Users/chhuang/stick/0523/meta-data/prnewswire/'$name '/Users/chhuang/stick/0523/txt/prnewswire/'$name &&
rm -rf '/Users/chhuang/stick/0523/txt/prnewswire/'$name'_1' &&
mkdir '/Users/chhuang/stick/0523/txt/prnewswire/'$name'_1' && 
python /Users/chhuang/stick/0408/code/remove_duplicates.py '/Users/chhuang/stick/0523/txt/prnewswire/'$name'/*' '/Users/chhuang/stick/0523/meta-data/prnewswire/'$name &&
for i in `cut -f1 /Users/chhuang/stick/0523/meta-data/prnewswire/$name\_1`; do cp '/Users/chhuang/stick/0523/txt/prnewswire/'$name'/'$i'.txt' '/Users/chhuang/stick/0523/txt/prnewswire/'$name'_1/'; done &&
rm -rf '/Users/chhuang/stick/0523/ner/prnewswire/'$name && 
mkdir '/Users/chhuang/stick/0523/ner/prnewswire/'$name && 
bash /Users/chhuang/stick/0408/ner_run.sh '/Users/chhuang/stick/0523/txt/prnewswire/'$name'_1' '/Users/chhuang/stick/0523/ner/prnewswire/'$name &&
/Users/chhuang/stick/0408/code/organization_extractor.py '/Users/chhuang/stick/0523/ner/prnewswire/'$name'/*' '/Users/chhuang/stick/0523/orgs/prnewswire/'$name;# &&
#python /Users/chhuang/stick/codes/clean_organizations.py /Users/chhuang/stick/0408/Org_replace_list.txt '/Users/chhuang/stick/0523/orgs/'$name &&
#python /Users/chhuang/stick/0408/code/build_DF.py '/Users/chhuang/stick/0408/Org_replace_list.txt' '/Users/chhuang/stick/0523/orgs/'$name'_1' '/Users/chhuang/stick/0523/orgs/'$name'_2' '/Users/chhuang/stick/0523/txt/'$name'_1' &&
#python /Users/chhuang/stick/0408/code/join.py '/Users/chhuang/stick/0523/meta-data/'$name'_1' '/Users/chhuang/stick/0523/orgs/'$name'_2' '/Users/chhuang/stick/0523/id_org/'$name;
done;
#bash /Users/chhuang/stick/merge.sh
#python /Users/chhuang/stick/codes/build_netowrk.py


