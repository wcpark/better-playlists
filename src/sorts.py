#!/usr/bin/python3


# Slides from class used as reference
# Merges two subarray of array
def merge(originalArray, left, mid, right):
    # Create leftSubarray ← originalArray[left..mid] & rightSubarray ← originalArray[mid+1..right]
    n1 = mid - left + 1
    n2 = right - mid

    # Slicing to extract subarrays from originalArray
    leftSubarray = originalArray[left : left + n1]
    rightSubarray = originalArray[mid + 1 : mid + 1 + n2]

    # Merge the arrays leftSubarray and rightSubarray into originalArray
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if leftSubarray[i] <= rightSubarray[j]:
            originalArray[k] = leftSubarray[i]
            i += 1
        else:
            originalArray[k] = rightSubarray[j]
            j += 1
        k += 1

    # Append the remaining elements of leftSubarray and rightSubarray
    while i < n1:
        originalArray[k] = leftSubarray[i]
        i += 1
        k += 1

    while j < n2:
        originalArray[k] = rightSubarray[j]
        j += 1
        k += 1


def mergeSort(originalArray, left, right):
    if left < right:
        # m is the point where the array is divided into two subarrays
        mid = (left + right) // 2

        mergeSort(originalArray, left, mid)
        mergeSort(originalArray, mid + 1, right)

        # Merge the sorted subarrays
        merge(originalArray, left, mid, right)


def printArray(array):
    for i in array:
        print(i, end=" ")
    print()


def main():
    originalArray = [8.6, 23.2, 6.73, 5.33, 0.72, 0.99]
    mergeSort(originalArray, 0, len(originalArray) - 1)
    print("Sorted array:")
    printArray(originalArray)


if __name__ == "__main__":
    main()
