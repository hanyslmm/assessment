#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# THIS method remove Duplicate values from list
def removeDuplicates(requests):
    try:
        # CONVERT list to set
        requests = set(requests)
        # requests = list(requests)
        return requests

    except:
        print('error occured in getRepeatedNetworkTraffic method try again')


if __name__ == '__main__':
    # MAIN program if user run this script directly
    requests = input("enter request values seperated by space 1 2 3 : ")
    requests = requests.split()
    result = removeDuplicates(requests)
    print (result)
