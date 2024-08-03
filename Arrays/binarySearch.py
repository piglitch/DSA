def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            print('Got it! Index number: ', mid)
            return
        if guess > target: 
            high = mid - 1
        else:
            low = mid + 1     
    print("Target does not exist in this array.")    
    return

arr = [1,4,8,10,67,88]    
target = 90
binary_search(arr, target)