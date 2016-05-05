#!/bin/sh
# usage:
# ./spell_check.sh <file>

# should be run on the:
#   centrale/core/src/com/nuova/centrale/resources/text/pre-process/centrale.definitions
#   xmls which have <fsm tag in model/specific path

# For running this script against the fsm files,
# cd model/specific
# grep -rl '<fsm ' * > files 
# for i in `cat files`
# do
#        echo $i >> out3;
#        grep -n 'message=' $i >> out3;
# done;
# ./spell_check.sh out3

rm out out1 out2
cut -d "=" -f 2 $1 | sed 's/\\n/ /g' | sed 's/<[^>]*>/ /g'| sed 's///g' > out 
cat out | aspell -a --personal="`pwd`/.aspell.en.pws"| grep '^&' > out1 
cat out1 | cut -d " " -f 2 | sort | uniq > out2
cat out2



