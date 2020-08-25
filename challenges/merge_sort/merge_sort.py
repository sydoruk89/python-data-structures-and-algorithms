def merge_sort(new_list):
    n = len(new_list)
           
    if n > 1:
        mid = n//2
        left =  new_list[:mid]
        right = new_list[mid:]
        #sort the left side
        merge_sort(left)
        #sort the right side
        merge_sort(right)
        #merge the sorted left and right sides together
        merge(left, right, new_list)

def merge(left, right, new_list):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_list[k] = left[i]
            i += 1
        else:
            new_list[k] = right[j]
            j += 1
            
        k += 1
    # all the remaining values
    while i < len(left):
        new_list[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        new_list[k] = right[j]
        j += 1
        k += 1
