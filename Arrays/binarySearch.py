def binary_seacrh(list, item):
    low = 0
    high = len(list)
    count = 0

    while low <= high:
        count += 1
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            print('target: ', guess, 'In steps: ', count)
            return guess
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1        
            

binary_seacrh([1,4,8,9,12], 12)
