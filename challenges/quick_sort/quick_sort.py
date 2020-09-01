def partition(input_list,left,right):
    low = left - 1
    pivot = input_list[right]
    for i in range(left, right):
        if input_list[i] <= pivot:
            low += 1
            swap(input_list, i, low)
    swap(input_list, right, low+1)
    return low+1

def swap(input_list, i, low):
    temp = input_list[i]
    input_list[i] = input_list[low]
    input_list[low] = temp    

def quickSort(input_list, left, right):
    if left < right:
        partition_index = partition(input_list,left,right)
        quickSort(input_list, left, partition_index - 1)
        quickSort(input_list, partition_index + 1, right)

m = [8,4,23,42,16,15]
quickSort(m, 0, len(m)-1)
print(m)