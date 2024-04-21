#!/usr/bin/python3

import random
import time


# Slides from class used as reference
# Merges two sublist of list, takes in list of tuples, where the first value is the playlist position and the second is the match percent
def merge(originalList, left, mid, right):
    # Create leftSublist ← originalList[left..mid] & rightSublist ← originalList[mid+1..right]
    n1 = mid - left + 1
    n2 = right - mid

    # Slicing to extract sublists from originalList
    leftSublist = originalList[left : left + n1]
    rightSublist = originalList[mid + 1 : mid + 1 + n2]

    # Merge the lists leftSublist and rightSublist into originalList
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        # Compare the second values in the tuple, the match percent
        if leftSublist[i][1] <= rightSublist[j][1]:
            originalList[k] = leftSublist[i]
            i += 1
        else:
            originalList[k] = rightSublist[j]
            j += 1
        k += 1

    # Append the remaining elements of leftSublist and rightSublist
    while i < n1:
        originalList[k] = leftSublist[i]
        i += 1
        k += 1

    while j < n2:
        originalList[k] = rightSublist[j]
        j += 1
        k += 1


def mergeSort(originalList, left, right):
    if left < right:
        # m is the point where the list is divided into two sublists
        mid = (left + right) // 2

        mergeSort(originalList, left, mid)
        mergeSort(originalList, mid + 1, right)

        # Merge the sorted sublists
        merge(originalList, left, mid, right)


def printList(list):
    for i in list:
        print(i, end=" ")
    print()

'''
def main():
    # Example use

    # Generate 100,000 tuples list for testing using list comprehension
    originalList = [(i, random.uniform(0, 1)) for i in range(1, 100001)]

    start_time = time.time()
    mergeSort(originalList, 0, len(originalList) - 1)
    end_time = time.time()

    sort_time = end_time - start_time

    print("Sorted list:")
    printList(originalList)
    print("Time taken for merge sort:", sort_time, "seconds")


if __name__ == "__main__":
    main()
'''