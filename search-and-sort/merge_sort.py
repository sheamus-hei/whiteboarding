# source: https://www.geeksforgeeks.org/merge-sort/

def merge_sort(nums): 
  if len(nums) > 1: 
    mid = len(nums)//2
    left = nums[:mid] 
    right = nums[mid:]
    merge_sort(left) 
    merge_sort(right) 

    i = j = k = 0
      
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            nums[k] = left[i] 
            i+=1
        else: 
            nums[k] = right[j] 
            j+=1
        k+=1

    while i < len(left): 
        nums[k] = left[i] 
        i+=1
        k+=1
      
    while j < len(right): 
        nums[k] = right[j] 
        j+=1
        k+=1

nums = [5,2,3,6,84,9,8]
merge_sort(nums)
print(nums)
# -> [2, 3, 5, 6, 8, 9, 84]

# works on other sortable data types
words = ["banana", "apple", "grape", "orange"]
merge_sort(words)
print(words)
# -> ['apple', 'banana', 'grape', 'orange']