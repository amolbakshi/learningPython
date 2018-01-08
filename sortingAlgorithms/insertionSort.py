import random

def intertionSort(randomList):
    for j in range(len(randomList)):
        key = randomList[j]
        # insert A[j] into sorted sequence A[0..j-1]
        i = j - 1
        while i > -1 and randomList[i] > key:
            randomList[i + 1] = randomList[i]
            i = i - 1
            randomList[i + 1] = key
    return randomList


randomList = random.sample(range(0, 10000), 20)
print ("Unsorted list : ")
print(randomList)
print("List sorted with insertionSort : ")
print(intertionSort(randomList))