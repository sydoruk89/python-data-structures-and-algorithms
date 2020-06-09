# Array Shift 
def insertShiftArray(arr, el):
    index = 0
    if len(arr) % 2 == 0:
        index = len(arr)//2
    else:
        index = len(arr) // 2 + 1
    new_arr = []
    for i in range(index):
        new_arr.append(arr[i])
    new_arr.append(el)
    for i in range(index, len(arr)):
        new_arr.append(arr[i])  
        print(i)  
    return new_arr

print(insertShiftArray([1, 2, 3, 4, 6, 7, 8, 9], 5))
