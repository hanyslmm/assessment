
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import all modules
import csv
import numpy as np
import pandas as pd
import os, datetime
import re

file_AVG = "company_info/employess_age_average.txt"
file_IT = "company_info/IT_employess_count.txt"
file_SAL = "company_info/technology_salaries.txt"
file_INV = "company_info/employess_invalid_email.txt"
# GET current time ct and define file decoration variable
ct = datetime.datetime.now()
current_date = "Current Date is {}".format(ct.strftime("%Y-%m-%d %H:%M"))
last_line = "\n############################### \n \n"
line = "\n#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_# \n"

# GET csv file name default value Employees.csv
file = input("enter full file name : ")
if not file:
    file = "Employees.csv"

# READ file using csv liberary
with open('{}'.format(file)) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]}\
                        - {row[5]} - {row[6]} ')
            line_count += 1
    print(f'Processed {line_count} lines.')


# read csv file using pandas liberary, create DataFrame df
df = pd.read_csv('{}'.format(file))
# create variable counter count all rows in the csv
row_counter = df.shape[0]
print ("number of Employees is {}".format(row_counter))

choice = input(f'choose what program to run \n 1- Count IT \n \
2- Average Age \n 3- max and min Salary \n 4- check emails validation \n \
enter you choice in decimal number:   ')

# 1- Count IT
if choice == "1":
    # COUNT values of Department in the csv file
    value_count = df['Department'].value_counts()
    # PRINT IT value counts
    result = value_count.loc['IT']
    result = "Number of IT employees: {}".format(result)
    print (result)
    #= input("enter to write result to employess_age_average.txt")
    file = open(file_IT, "a")
    list = [line, result, line, current_date, last_line]
    for i in list:
        file.write(i)
    file.close()

# 2- Average Age
if choice == "2":
    # CONVERT age values from string to numerical values
    df.Age = pd.to_numeric(df.Age, errors='coerce')
    result = int(round(df['Age'].mean()))
    result = "Average age of employees: {}".format(result)
    print (result)
    #= input("enter to write result to employess_age_average.txt")
    file = open(file_AVG, "a")
    list = [line, result, line, current_date, last_line]
    for i in list:
        file.write(i)
    file.close()

# 3- max and min Salary
if choice == "3":
    # FIRST get max employee salary
    result = df['Salary'].max()
    ID = df['Salary'].idxmax()
    resultName = df.loc[ID, 'Name']
    result = "Max salary of employees is {} and employee name is {}!"\
                                                .format(result, resultName)
    print (result)
    #= input("enter to write result to employess_age_average.txt")
    file = open(file_SAL, "a")
    list = [line, result]
    for i in list:
        file.write(i)

    # THEN get min employee salary
    result = df['Salary'].min()
    ID = df['Salary'].idxmin()
    resultName = df.loc[ID, 'Name']
    result = "Min salary of employees is {} and employee name is {}!"\
                                                .format(result, resultName)
    print (result)
    #= input("enter to write result to employess_age_average.txt")
    file = open(file_SAL, "a")
    list = [line, result, line, current_date, last_line]
    for i in list:
        file.write(i)
    file.close()

# 4- check emails validation
if choice == "4":
    invalidList = [] # Append to list all invalid mail index
    rows = df.shape[0]
    rows = int(rows)
    # READ file line by line.
    i_row = 0
    while i_row < rows:
        test = df.loc[i_row, 'Email']
        if not re.search(r"[a-z0-9._+-]"+"[@a-z0-9_+-]"+"."+"com"+"."+"[a-z]", test):
            print("invalid mail {}".format(test))
            print (i_row)
            invalidList.append(i_row)
        i_row += 1
    print(invalidList)













print ("############# checks done!")
