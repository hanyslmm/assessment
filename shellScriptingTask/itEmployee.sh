#!/bin/bash       
#title           :countEmployee.sh
#description     :This script to read csv file.
#author		 :Hany Salama
#date            :20190315
#version         :0.1
#usage		 :bash countEmployee.sh file.csv
#=========================================================================
echo "hello $(whoami)"
echo "running this script in $(date +%F)"

INPUT=Employees.csv
OLDIFS=$IFS
IFS=","
COUNTER=0
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read Name Age PhoneNumber Email Salary Department CountryCode CountryCode
do
	echo "DOB : $Department"
	#echo "===================="
	if [ "$Department" == "IT" ]
	then
		COUNTER=$((COUNTER+1))
	fi

done < $INPUT
echo "=================================="
echo "Number of Employees: $COUNTER "
IFS=$OLDIFS
