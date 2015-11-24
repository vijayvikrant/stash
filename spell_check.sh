#!/bin/sh
# usage:
# ./spell_check.sh <file>
cut -d "=" -f 2 $1 | sed 's/\\n/ /g' | sed 's/<[^>]*>/ /g'| sed 's///g' > out 
cat out | aspell -a | grep '^&' > out1 
cat out1 | cut -d " " -f 2 | sort | uniq > out2


# For running this script against the fsm files,
# cd perfocarta/model/specific
# grep -rl '<fsm ' * > files 
# for i in `cat files`
# do
#        echo $i >> out3;
#        grep -n 'message=' $i >> out3;
# done;
# ./spell_check.sh out3
