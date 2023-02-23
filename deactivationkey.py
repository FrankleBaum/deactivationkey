import numpy as np

#importing data from packet_base & packet_weight
packetBase = np.genfromtxt('packet_base.txt' , delimiter= ',' )
packetWeight = np.genfromtxt('packet_weight.txt' , delimiter= ',' )

#separating data into chunks of 8; Need 2D arrays should have 4096
packetBaseArray = packetBase.reshape(4096, 8)
packetWeightArray = packetWeight.reshape(4096, 8)

#multiplying packetBaseArray values by packetWeightArray values
packetMultipliedArray = np.multiply(packetBaseArray, packetWeightArray)

#find the minimum, maximum, and mean of each chunk
minpacketMultipliedArray = np.min(packetMultipliedArray, 1)
maxpacketMultipledArray = np.max(packetMultipliedArray, 1)
meanpacketMultipliedArray = np.mean(packetMultipliedArray, 1)

#for result for each chunk. equation is (max - mean) * min
resultArray = (maxpacketMultipledArray - meanpacketMultipliedArray) * minpacketMultipliedArray

#sum of all chunk results
sumResultArray = np.sum(resultArray)

#sum rounded down to nearest integer
roundedSumResultArray = np.floor(sumResultArray)

#remainder if rounded sum divided by 4096
remainderRoundedSumResultArray= np.remainder(roundedSumResultArray,4096)

#print answer
print (remainderRoundedSumResultArray)