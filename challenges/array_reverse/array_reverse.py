def reverseArray_1(arr):
    return arr[::-1]

# Stretch goal
def reverseArray_2(arr):
    for i in range(len(arr)):
        arr[i], arr[-i-1] = arr[-i-1], arr[1]
    return arr
    