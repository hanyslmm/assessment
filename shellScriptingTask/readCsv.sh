#!/bin/bash       
#title           :reasCsb.sh
#description     :This script to read csv file.
#author		 :Hany Salama
#date            :20190315
#version         :0.1
#usage		 :bash mkscript.sh file.csv
#=========================================================================
echo "hello $(whoami)"
echo "running this script in $(date +%F)"
OLDIFS=$IFS
while read Name Age PhoneNumber Email Salary Department CountryCode CountryCode
 do
	#echo -e "\e[1;33m$Age \
	#========================\e[0m\n\"
	echo "hello"
 done < $1

IFS=$OLDIFS
