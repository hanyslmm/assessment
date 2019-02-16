#!/bin/bash
#title           :avgAge.sh
#description     :This script to read csv file.
#author		 :Hany Salama
#date            :20190315
#version         :0.1
#usage		 :bash avgAge.sh file.csv
#tasks		 :Write a bash script to combine both CountryCode and PhoneNumber with
# a - and add a + before country code like +countrycode-phonenumber and remove
# country codes from the csv file.
#=========================================================================
echo "hello $(whoami)"
echo "running this script in $(date +%F)"
FILE=$1
OLDIFS=$IFS
IFS=","
DATE=$(date +%d-%m-%Y)
# awk -F"," '{ printf "%-10s %s\n", $1, $2 }' $FILE
CODE=()
PHONE=()
# [ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read Name Age PhoneNumber Email Salary Department CountryCode
do
	CODE+=$CountryCode
	PHONE+=$PhoneNumber
done < $1
echo $CODE
IFS=$OLDIFS
