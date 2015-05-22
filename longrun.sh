#!/bin/bash 
testresult=/src/test_result 
time_stamp=$(date +%Y_%m_%d_%H_%M_%S)
mkdir -p ${testresult}/${time_stamp}
if [ "$1" != "" ]; then
    nu=$1
else
    nu=1
fi


for (( i=1; i<=$nu; i=i+1 ))
do

pushd ./testcase/wifi/ 
testcase=wifi
nosetests -v -s --with-xunit --xunit-file=${testresult}/${time_stamp}/${testcase}-${i}.xml
popd 

pushd ./testcase/bluetooth/ 
testcase=bluetooth
nosetests -v -s --with-xunit --xunit-file=${testresult}/${time_stamp}/${testcase}-${i}.xml
popd

pushd ./testcase/camera/
testcase=camera
nosetests -v -s --with-xunit --xunit-file=${testresult}/${time_stamp}/${testcase}-${i}.xml
popd

#pushd ./testcase/zsensors/
##nosetests -v -s
#popd

pushd ./testcase/lcd
testcase=lcd
nosetests -v -s --with-xunit --xunit-file=${testresult}/${time_stamp}/${testcase}-${i}.xml
popd

pushd ./testcase/sensors_simple/
testcase=sensors_simple
nosetests -v -s --with-xunit --xunit-file=${testresult}/${time_stamp}/${testcase}-${i}.xml
popd 

pushd ./testcase/audio/
testcase=audio
nosetests -v -s --with-xunit --xunit-file=${testresult}/${time_stamp}/${testcase}-${i}.xml
popd
done
