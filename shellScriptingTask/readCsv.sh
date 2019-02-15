#!/bin/bash       
#title           :reasCsb.sh
#description     :This script to read csv file.
#author		 :Hany Salama
#date            :20190315
#version         :0.1
#=========================================================================
echo "hello $(whoami)"
echo "running this script in $(date +%F)"
OLDIFS=$IFS
while read Name Age PhoneNumber Email Salary Department CountryCode CountryCode
 do
	echo -e "Name : $Name"
	echo "========================"
	echo "Age : $Age"
	echo "hello there"
 done < $1

IFS=$OLDIFS
