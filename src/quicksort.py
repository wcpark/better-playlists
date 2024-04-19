#!/usr/bin/python3

import random
import time


# Slides from class used as reference
# Function to swap position of elements
def swap(originalList, i, j):
    originalList[i], originalList[j] = originalList[j], originalList[i]


# Function to partition the list on the basis of pivot element
def partition(originalList, low, high):
    # Select the pivot element
    pivot = originalList[low][1]
    up = low
    down = high

    while up < down:
        while up <= high and originalList[up][1] <= pivot:
            up += 1
        while down >= low and originalList[down][1] > pivot:
            down -= 1
        if up < down:
            swap(originalList, up, down)
    swap(originalList, low, down)
    return down


def quickSort(originalList, low, high):
    if low < high:
        pivot = partition(originalList, low, high)
        quickSort(originalList, low, pivot - 1)
        quickSort(originalList, pivot + 1, high)


# Function to print elements of an list
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
