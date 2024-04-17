#!/usr/bin/python3

import time


# Slides from class used as reference
# Function to swap position of elements
def swap(originalArray, i, j):
    originalArray[i], originalArray[j] = originalArray[j], originalArray[i]


# Function to partition the array on the basis of pivot element
def partition(originalArray, low, high):
    # Select the pivot element
    pivot = originalArray[low]
    up = low
    down = high

    while up < down:
        for j in range(up, high):
            if originalArray[j] > pivot:
                break
            up += 1
        for j in range(high, low, -1):
            if originalArray[j] < pivot:
                break
            down -= 1
        if up < down:
            swap(originalArray, up, down)
    swap(originalArray, low, down)
    return down


def quickSort(originalArray, low, high):
    if low < high:
        pivot = partition(originalArray, low, high)
        quickSort(originalArray, low, pivot - 1)
        quickSort(originalArray, pivot + 1, high)


# Function to print elements of an array
def printArray(originalArray):
    for i in originalArray:
        print(i, end=" ")


def main():
    # Example use
    data = [0.39, 6.13, 22.89, 3.14, 0.12, 5.73, 1.00]

    start_time = time.time()
    quickSort(data, 0, len(data) - 1)
    end_time = time.time()

    sort_time = end_time - start_time

    print("Time taken for quick sort:", sort_time, "seconds")
    print("Sorted array: ", end="")
    printArray(data)


if __name__ == "__main__":
    main()
