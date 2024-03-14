def printUnorderedPairs(listA, listB):
    for i in range(len(listA)):
        for j in range(len(listB)):
            for k in range(0,100000):
                print(str(listA[i]) + "," + str(listB[j]))