
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import all modules
import csv
import numpy as np
import pandas as pd
import os, datetime

file_AVG = "company_info/employess_age_average.txt"
file_IT = "company_info/IT_employess_count.txt"

# GET current time ct and define file decoration variable
ct = datetime.datetime.now()
current_date = ct.strftime("%Y-%m-%d %H:%M")
last_line = "\n###############################\n"
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
2- Average Age \n enter you choice in decimal number:   ')

if choice == "1":
    # COUNT values of Department in the csv file
    value_count = df['Department'].value_counts()
    # PRINT IT value counts
    result = value_count.loc['IT']
    result = "Number of IT employees: {}".format(result)
    #= input("enter to write result to employess_age_average.txt")
    file = open(file_IT, "a")
    file.write(line)
    file.write(result)
    file.write(line)
    file.write("Current Date is {}".format(current_date))
    file.write(last_line)
    file.close()

if choice == "2":
    # CONVERT age values from string to numerical values
    df.Age = pd.to_numeric(df.Age, errors='coerce')
    # PRINT average age value
    result = int(round(df['Age'].mean()))
    result = "Average age of employees: {}".format(result)
    #= input("enter to write result to employess_age_average.txt")
    file = open(file_AVG, "a")
    file.write(line)
    file.write(result)
    file.write(line)
    file.write("Current Date is {}".format(current_date))
    file.write(last_line)
    file.close()
