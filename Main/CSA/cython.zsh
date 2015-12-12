#!/bin/bash
file=`basename -s .py $1`
cython --embed -o ${file}.c $1
gcc -Os -I /usr/include/python2.7 -o trip ${file}.c -lpython2.7 -lpthread -lm -lutil -ldl
#time ./trip
time ./trip > /dev/null
