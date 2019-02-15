#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# THIS method check if all list values are integer
def getRepeatedNetworkTraffic(packet_list):
    try:
        # CHECK if value entered correctly integer inside a list
        if all(isinstance(x, int) for x in packet_list) \
                                                    and type(packet_list)==list:
            print('you entered correct values')
            result = dict()
            print (packet_list)
            # COUNTING loop
            for i in packet_list:
                # .get allows specify a default value 0 if the key doesn't exist
                result[i] = result.get(i, 0) + 1
            return result
        else:
            print('try again with integer values in form of List')
            return packet_list
    except:
        print('error occured in getRepeatedNetworkTraffic method try again')


if __name__ == '__main__':
    # MAIN program if user run this script directly
    packet = input("enter packet values seperated by space 1 2 3 : ")
    packet = packet.split()
    packet_list = []
    # CONVERT input values from string to integer
    for x in packet:
        packet_list.append(int(x))
    x = getRepeatedNetworkTraffic(packet_list)
    for k,v in x.items():
        print("id = {} repeated {} times".format(str(k), str(v)))
