#!/bin/sh
grep -rl '<fsm ' * > files
for i in `cat files`
do
       echo $i >> out3;
       grep -n 'message=' $i >> out3;
done;
