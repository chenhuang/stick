#/usr/bin/bash

for name in `cat /Users/chhuang/stick/entries_chr`; do
rm -rf '/Users/chhuang/stick/0606/txt/'$name &&
mkdir '/Users/chhuang/stick/0606/txt/'$name && 
python '/Users/chhuang/stick/codes/articleExtractor_chr.py' '/Users/chhuang/stick/0606/raw/'$name'/*' $name '/Users/chhuang/stick/0606/meta-data/'$name '/Users/chhuang/stick/0606/txt/'$name &&
rm -rf '/Users/chhuang/stick/0606/txt/'$name'_1' &&
mkdir '/Users/chhuang/stick/0606/txt/'$name'_1' && 
python /Users/chhuang/stick/0408/code/remove_duplicates.py '/Users/chhuang/stick/0606/txt/'$name'/*' '/Users/chhuang/stick/0606/meta-data/'$name &&
for i in `cut -f1 /Users/chhuang/stick/0606/meta-data/$name\_1`; do cp '/Users/chhuang/stick/0606/txt/'$name'/'$i'.txt' '/Users/chhuang/stick/0606/txt/'$name'_1/'; done &&
rm -rf '/Users/chhuang/stick/0606/ner/'$name && 
mkdir '/Users/chhuang/stick/0606/ner/'$name && 
bash /Users/chhuang/stick/0408/ner_run.sh '/Users/chhuang/stick/0606/txt/'$name'_1' '/Users/chhuang/stick/0606/ner/'$name &&
/Users/chhuang/stick/0408/code/organization_extractor.py '/Users/chhuang/stick/0606/ner/'$name'/*' '/Users/chhuang/stick/0606/orgs/'$name; #&&
#python /Users/chhuang/stick/codes/clean_organizations.py /Users/chhuang/stick/0408/Org_replace_list.txt '/Users/chhuang/stick/0606/orgs/'$name &&
#python /Users/chhuang/stick/0408/code/build_DF.py '/Users/chhuang/stick/0408/Org_replace_list.txt' '/Users/chhuang/stick/0606/orgs/'$name'_1' '/Users/chhuang/stick/0606/orgs/'$name'_2' '/Users/chhuang/stick/0606/txt/'$name'_1' &&
#python /Users/chhuang/stick/0408/code/join.py '/Users/chhuang/stick/0606/meta-data/'$name'_1' '/Users/chhuang/stick/0606/orgs/'$name'_2' '/Users/chhuang/stick/0606/id_org/'$name;
done;
#bash /Users/chhuang/stick/merge.sh
#python /Users/chhuang/stick/codes/build_netowrk.py


