#!/usr/bin/python
# Import needed modulea
import os
import sys
import subprocess

# Ask the user for long path input
longPath = input("enter the long path to your script between double quotes:")

# Set up the echo command and direct the output to a pipe
p1 = subprocess.Popen(['ping', '-c 2', host], stdout=subprocess.PIPE)

# Run the command
output = p1.communicate()[0]

print output
longPath = input("enter the long path to your script between double quotes:")
longPath = "cd {}".format(longPath)
simplePath = input("enter a unique shorcut:")
print (longPath)
print (simplePath)
os.system("alias {}={}".format(simplePath, longPath))


https://stackoverflow.com/questions/21406887/subprocess-changing-directory
