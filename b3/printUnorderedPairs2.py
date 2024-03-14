def printUnorderedPairs(listA, listB):
    for i in range(len(listA)):
        for j in range(len(listB)):
            if listA[i] < listB[j]:
                print(str(listA[i]) + "," + str(listB[j]))