
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import all modules
import csv
import numpy as np
import pandas as pd

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

# COUNT frequency of values of Department in the csv file
value_count = df['Department'].value_counts()

# PRINT IT value counts
print ()
