#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# THIS method check if all list values are integer
def getRepeatedNetworkTraffic(packet):
    try:
        # CHECK if value entered correctly
        if all(isinstance(x, int) for x in packet):
            print('you entered integer values')
        else:
            print('try again with integer values')

        return None
    except:
        print('error occured try again')
        return None


if __name__ == '__main__':

    packet = input("enter packet values in form of list [x, y, z, ...]: ")
    getRepeatedNetworkTraffic(packet)
