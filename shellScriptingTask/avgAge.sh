#!/bin/bash
#title           :avgAge.sh
#description     :This script to read csv file.
#author		 :Hany Salama
#date            :20190315
#version         :0.1
#usage		 :bash avgAge.sh file.csv
#tasks		 :get average employees age and write current date and the result into ‘employess_age_average.txt’
# file under company_info directory.
#=========================================================================
echo "hello $(whoami)"
echo "running this script in $(date +%F)"
DATE=$(date +%d-%m-%Y)
FILE=employess_age_average.txt
# Create the file or change it's modification date
touch company_info/$FILE
# INPUT=Employees.csv
OLDIFS=$IFS
IFS=","
COUNTER=0
SUMAGE=0
# [ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read Name Age PhoneNumber Email Salary Department CountryCode
do
	if [ $Age = "Age" ]
	then
		echo $Age
	else
		echo $Age
		SUMAGE=$(( SUMAGE + Age ))
		COUNTER=$((COUNTER+1))
	fi
done < $1
AVERAGE=$(( SUMAGE / COUNTER ))
echo $AVERAGE
echo "Current Date is $DATE " >> company_info/$FILE
echo "==================================" >> company_info/$FILE
echo "Average age of employees: $AVERAGE " >> company_info/$FILE
echo "==================================" >> company_info/$FILE
echo "##################################" >> company_info/$FILE
echo "############### Done check employess_age_average.txt inside company_info directory"
IFS=$OLDIFS
