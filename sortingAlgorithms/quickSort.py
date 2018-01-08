import random


def createPivotAndSort(list):
    pivotIndex = len(list)-1
    pivot = list[pivotIndex]
    print("Pivot choosen :"+str(pivot))
    for i in range(len(list)-1):
        if list[i] > pivot and i < pivotIndex:
            list[pivotIndex] = list[i]
            pivotIndex=i
            list[i]=pivot
        elif list[i] < pivot and i > pivotIndex:
            list[pivotIndex] = list[i]
            list[i] = list[pivotIndex+1]
            list[pivotIndex+1] = pivot
            pivotIndex=pivotIndex+1
    return list


randomList = random.sample(range(0, 10000), 20)
print ("Unsorted list : ")
print(randomList)
print("List sorted with insertionSort : ")
print(createPivotAndSort(randomList))