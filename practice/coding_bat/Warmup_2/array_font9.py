'''Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
'''
def array_front9(nums):
  is_nine = False
  for i in range(4):
    if nums[i] == 9:
      is_nine = True
    else:
      continue
  print(is_nine)
  return is_nine


array_front9([1, 2, 9, 3, 4])
array_front9([1, 2, 3, 4, 9])
array_front9([1, 2, 3, 4, 5])