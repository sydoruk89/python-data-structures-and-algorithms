def BinarySearch(arr, key):
    l = 0
    h = len(arr) - 1
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            h = mid - 1
        else:
            l = mid + 1
    return -1

print(BinarySearch([1,5,15,23,34,51], 23))