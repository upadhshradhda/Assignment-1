# question-1
def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []  

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)


# Question-2
def remove_element(nums, val):
    k = 0 
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [3, 2, 2, 3]
val = 3
result = remove_element(nums, val)
print("Output:", result, ", nums =", nums[:result]+ ["_"])


# Question-3
def Insertarr(nums, target):
    i = 0
    j= len(nums) - 1

    while i <= j:
        mid = (i + j) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            i = mid + 1
        else:
           j= mid - 1
    return i

nums = [1, 3, 5,6]
target = 5
index = Insertarr(nums, target)
print(index)  


# Question-4
def sumOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    digits.insert(0, 1)
    return digits
digits = [1,2,3]
result = sumOne(digits)
print(result) 


# Question-5
def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    for i in range(m + n - 1, -1, -1):
        if p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
        elif p2 >= 0:
            nums1[i] = nums2[p2]
            p2 -= 1
nums1 = [1, 2,3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  


# Question-6
def Duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
nums = [1, 2, 3,1]
result = Duplicate(nums)
print(result)  
  

# Question-7
def moveZeroe(nums):
    left = 0 
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[left] = nums[i]
            left += 1
    while left < len(nums):
        nums[left] = 0
        left += 1
nums = [0, 1, 0, 3, 12]
moveZeroe(nums)
print(nums)  


# Question-8
def ErrorNums(nums):
    n = len(nums)
    num_count = [0] * (n + 1)
    duplicate = 0
    missing = 0

    for num in nums:
        num_count[num] += 1

    for i in range(1, n + 1):
        if num_count[i] == 0:
            missing = i
        elif num_count[i] == 2:
            duplicate = i
    return [duplicate, missing]

nums = [1, 2, 2, 4]
result = ErrorNums(nums)
print(result)

 
 
 
