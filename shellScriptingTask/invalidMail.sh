#!/bin/bash
#title           :avgAge.sh
#description     :This script to read csv file.
#author		 :Hany Salama
#date            :20190315
#version         :0.1
#usage		 :bash avgAge.sh file.csv
#tasks		 :get max, min salary for Technology department and write current date
# and the result with employee name into ‘technology_salaries.txt’ file under company_info directory.
#=========================================================================
echo "hello $(whoami)"
echo "running this script in $(date +%F)"
DATE=$(date +%d-%m-%Y)
FILE=employess_invalid_email.txt
# Create the file or change it's modification date
touch company_info/$FILE
# INPUT=Employees.csv
OLDIFS=$IFS
IFS=","
echo "==================================" >> company_info/$FILE
echo "Current Date is $DATE " >> company_info/$FILE
echo "==================================" >> company_info/$FILE
# [ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read Name Age PhoneNumber Email Salary Department CountryCode CountryCode
do
if ! [[ $Name == "Name" ]]
then
	if [[ "$Email" =~ ^[[:alpha:]0-9._+-]+@[[:alpha:]0-9]+\.+[[:alpha:]]+\.+[[:alpha:]] ]]
	then
		if ! [[ ${Email:0:1} == [[:digit:]]* ]]
		then
			if ! [[ ${Email:0:1} == [._+-]* ]]
			then
		    	echo "Email address $Email is valid."
			else
						echo "Email address $Email is invalidddd."
						echo "Email address for $Name whos age is $Age is invalid kindly check $Email ." >> company_info/$FILE
			fi
		else
		    echo "Email address $Email is invalid awy."
				echo "Email address for $Name whos age is $Age is invalid kindly check $Email ." >> company_info/$FILE

		fi
	else
			echo "Email address $Email is invalid gedan."
			echo "Email address for $Name whos age is $Age is invalid kindly check $Email ." >> company_info/$FILE

	fi
fi
done < $1
echo "##################################" >> company_info/$FILE
echo "############### Done check employess_invalid_email.txt inside company_info directory"
IFS=$OLDIFS
