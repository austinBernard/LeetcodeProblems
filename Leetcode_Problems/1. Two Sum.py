class Solution:
    def twoSum(self, nums, target):
                       
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            nums[i] = None
            if remaining in nums:
                return [i, nums.index(remaining)]

            
test = Solution()
print(test.twoSum([3, 2, 4], 6)) # output = [1,2]