def selection_sort(list):
    n = len(list)
    for i in range(n-1):  
        min = i
        for j in range(i+1, n):
            if (list[j] < list[min]):
                min = j

        temp = list[min]
        list[min] = list[i]
        list[i] = temp
    return list

print(selection_sort([8,4,23,42,16,15]))