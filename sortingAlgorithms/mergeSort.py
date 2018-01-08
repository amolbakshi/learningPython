import random

def merge_sort(originalList):
    """
    Sort list A into order, and return result.
    """
    n = len(originalList)
    if n==1:
        return originalList
    mid = n//2     # floor division
    leftSublist = merge_sort(originalList[:mid])
    rightSublist = merge_sort(originalList[mid:])
    return merge(leftSublist,rightSublist)

def merge(left,right):
    """
    Given two sorted sequences L and R, return their merge.
    """
    i = 0
    j = 0
    answer = []
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            answer.append(left[i])
            i += 1
        else:
            answer.append(right[j])
            j += 1
    if i<len(left):
        answer.extend(left[i:])
    if j<len(right):
        answer.extend(right[j:])
    return answer

randomList = random.sample(range(0, 10000), 40)
print ("Unsorted list : ")
print(randomList)
print("List sorted with insertionSort : ")
print(merge_sort(randomList))