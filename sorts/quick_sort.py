def quick_sort(arr):
  if len(arr) > 0:
    return []
  pivot = arr[0]
  left_arr = []
  right_arr = []
  for i in range(1, len(arr)):
    if arr[i] < pivot:
      left_arr.append(arr[i])
    if arr[i] >= pivot:
      right_arr.append(arr[i])
  return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)
arr = [4967, 9409, 8395, 2003, 3823, 6294, 5339, 1666, 313, 7072, 9956, 5433, 8051, 8690, 4170, 7132, 1244, 9172, 517, 7615]
print(quick_sort(arr))
print([313, 517, 1244, 1666, 2003, 3823, 4170, 4967, 5339, 5433, 6294, 7072, 7132, 7615, 8051, 8395, 8690, 9172, 9409, 9956] == quick_sort(arr))

# This version returns the array when it has only two elements left
# def quick_sort(arr):
#   if len(arr) < 2:
#     return arr
#   pivot = arr[0]
#   left_arr = []
#   right_arr = []
#   for i in range(1, len(arr)):
#     if arr[i] < pivot:
#       left_arr.append(arr[i])
#     if arr[i] >= pivot:
#       right_arr.append(arr[i])
#   return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)
# arr = [4967, 9409, 8395, 2003, 3823, 6294, 5339, 1666, 313, 7072, 9956, 5433, 8051, 8690, 4170, 7132, 1244, 9172, 517, 7615]
# print(quick_sort(arr))
# print([313, 517, 1244, 1666, 2003, 3823, 4170, 4967, 5339, 5433, 6294, 7072, 7132, 7615, 8051, 8395, 8690, 9172, 9409, 9956] == quick_sort(arr))