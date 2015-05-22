#!/bin/bash 
testresult=./test_result 
time_stamp=$(date +%Y_%m_%d_%H_%M_%S)
current_testcase=${PWD##*/} 
printf '%s\n' "$current_testcase"
mkdir -p ${testresult}/${time_stamp}
if [ "$1" != "" ]; then
    nu=$1
else
    nu=1
fi


for (( i=1; i<=$nu; i=i+1 ))
do
	testcase=$current_testcase
	nosetests -v -s --with-xunit --xunit-file=${testresult}/${time_stamp}/${testcase}-${i}.xml
done
