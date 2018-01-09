import random


def swapElements(sublist,start,stop):
        pivotIndex = stop
        pivot = sublist[pivotIndex]
        print("Pivot choosen :"+str(pivot))
        for i in range(start,stop):
            if sublist[i] > pivot and i < pivotIndex:
                sublist[pivotIndex] = sublist[i]
                pivotIndex=i
                sublist[i]=pivot
            elif sublist[i] < pivot and i > pivotIndex:
                sublist[pivotIndex] = sublist[i]
                sublist[i] = sublist[pivotIndex+1]
                sublist[pivotIndex+1] = pivot
                pivotIndex=pivotIndex+1
        return pivotIndex


def quickSort(list,start,stop):
    if (start < stop):
        index=swapElements(list,start,stop)
        quickSort(list,start,index-1)
        quickSort(list,index+1,stop)
    else:
        return

randomList = random.sample(range(0, 10000), 60)
print ("Unsorted list : ")
print(randomList)
print("List sorted with quick sort : ")
quickSort(randomList,0,len(randomList)-1)
print(randomList)