#!/usr/bin/python3

import random
import time


# Function to swap position of elements
def swap(originalList, i, j):
    originalList[i], originalList[j] = originalList[j], originalList[i]


# Function to perform three-way partitioning on list; three-way partitioning was selected to
# deal with worst-case of many duplicate elements leading to RecursionError
def partition(originalList, low, high):
    # Randomly select the pivot element to minimize chance of worst-case
    pivot_index = random.randint(low, high)
    swap(originalList, low, pivot_index)
    pivot = originalList[low][1]

    # Pointers for three-way partitioning, dividing list into three regions:
    # elements less than pivot, equal to pivot, and greater than pivot
    lowPtr = low
    highPtr = high
    currentIndex = low

    while currentIndex <= highPtr:
        if originalList[currentIndex][1] < pivot:
            swap(originalList, currentIndex, lowPtr)
            lowPtr += 1
            currentIndex += 1
        elif originalList[currentIndex][1] > pivot:
            swap(originalList, currentIndex, highPtr)
            highPtr -= 1
        else:
            currentIndex += 1

    return lowPtr, highPtr


def quickSort(originalList, low, high):
    if low < high:
        leftPartition, rightPartition = partition(originalList, low, high)
        quickSort(originalList, low, leftPartition - 1)
        quickSort(originalList, rightPartition + 1, high)


# Function to print elements of a list
def printList(originalList):
    for i in originalList:
        print(i, end=" ")


def main():
    # Example use

    # Generate 100,000 tuples list for testing using list comprehension
    originalList = [(i, random.uniform(0, 1)) for i in range(1, 100001)]

    start_time = time.time()
    quickSort(originalList, 0, len(originalList) - 1)
    end_time = time.time()

    sort_time = end_time - start_time

    print("Sorted list: ", end="")
    printList(originalList)
    print("Time taken for quick sort:", sort_time, "seconds")


if __name__ == "__main__":
    main()
