from repeatFun import getRepeatedNetworkTraffic

packets =[1,2,3,4,1,2,2,2,3,4,5]
result = getRepeatedNetworkTraffic(packets)
for k,v in result.items():
    print("id = {} repeated {} times".format(str(k), str(v)))
