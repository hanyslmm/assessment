#!/bin/bash
OLDIFS=$IFS
IFS=","
while read Name Age
 do
	echo -e "\e[1;33m$Name \
	========================\e[0m\n\"
 done < $1
IFS=$OLDIFS
