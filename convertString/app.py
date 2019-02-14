#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# THIS method check rearrange string
def convert(text, nRows):
    # IF only one row
    if nRows == 1:
        print(text)
        return

    # FIND length of text
    length = len(text)

    # Create an array of strings for all nRows
    array = ["" for x in range(nRows)]

    # SET inital value to row = 0 to index row number
    row = 0

    for i in range(length):

        # APPEND current character to current rows
        array[row] += text[i]

        # IF reached last row change direction to up
        if row == nRows - 1:
            up = True

        # IF reached first row change direction to down
        elif row == 0:
            up = False
		# If direction is up decrement, else increment
        if up:
            row -= 1
        else:
            row += 1
	# PRINT the result each row by row
    for i in range(nRows):
        print(array[i], end = "")
    print("")
if __name__ == '__main__':
    # MAIN program if user run this script directly
    text = input("enter the string to ZigZag: ")
    nRows = input("enter number of rows: ")
    nRows = int(nRows)
    # CALLING convert method
    convert(text, nRows)
