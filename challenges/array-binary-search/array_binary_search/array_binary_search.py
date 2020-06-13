def BinarySearch(arr, key):
    """Func takes in 2 parameters: a sorted array and the search key, and returns the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

    Args:
        arr ([list]): a list of integers
        key ([int]): innteger value 
    """
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