# # Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        num = nums1 + nums2
        numSorted = sorted(num)
        
        mid = len(numSorted) // 2
        res = (numSorted[mid] + numSorted[~mid])
        
        return res / 2
    
test = Solution()
print(test.findMedianSortedArrays([1,3], [2,4])) # Testing by calling function
    
    
# # nums1.length == m
# # nums2.length == n
# # 0 <= m <= 1000
# # 0 <= n <= 1000
# # 1 <= m + n <= 2000
# # -106 <= nums1[i], nums2[i] <= 106
