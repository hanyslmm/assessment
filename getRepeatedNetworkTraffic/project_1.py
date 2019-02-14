#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# THIS method check if all list values are integer
def getRepeatedNetworkTraffic(packet_list):
    try:
        # CHECK if value entered correctly using isinstance function
        if all(isinstance(x, int) for x in packet_list):
            print('you entered integer values')
        else:
            print('try again with integer values')

        return packet_list
    except:
        print('error occured in getRepeatedNetworkTraffic method try again')
        return None


if __name__ == '__main__':

    packet = input("enter packet values seperated by space 1 2 3 : ")
    packet_list = packet.split()

    packet_list = int(packet_list)
    print (type(packet_list))

    x = getRepeatedNetworkTraffic(packet_list)
    print (x)
