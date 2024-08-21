def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range (1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    sorted_arr = []
    for i in range (len(arr)):
        index = findSmallest(arr)
        sorted_arr.append(arr.pop(index))
    print(sorted_arr)

array = [133,56,78,22,109]
selectionSort(array)