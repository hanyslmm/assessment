#!/usr/bin/python
import os
import sys

longPath = input("enter the long path to your script between double quotes:")
longPath = "cd {}".format(longPath)
simplePath = input("enter a unique shorcut:")
print (longPath)
print (simplePath)
os.system("alias {}={}".format(simplePath, longPath))
