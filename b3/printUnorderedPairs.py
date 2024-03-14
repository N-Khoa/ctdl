def printUnorderedPairs(list):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            print(list[i] + "," + list[j])