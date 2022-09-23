# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums):
        nums.sort()
        
        list1 = nums
        iden = set(nums)
        
        if len(list1) != len(iden):
            return True
        else:
            return False
        
test = Solution()
print(test.containsDuplicate([1, 2, 3, 1, 5, 2, 1])) # Testing by calling function

 