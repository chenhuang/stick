for i in `ls $1/*`; do name=`echo $i | awk 'BEGIN{FS="/"}{print $NF}END{}'`; echo $name; /Users/chhuang/stick/0408/stanford-ner-2013-04-04/ner.sh $i > $2/$name; done;

#for i in `ls $1/*`; do name=`echo $i | awk 'BEGIN{FS="/"}{print $NF}END{}'`; echo $name; done;


