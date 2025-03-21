class Solution:
    def medianOfSortedArray(self, nums1:list[int], nums2:list[int])->int:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        median = 0
        if n%2 == 0:
            median = (nums1[n//2-1]+nums1[n//2])/2
        else:
            median = nums1[n//2]
        return median

nums1 = list(map(int, input("Enter first sorted array: ").split()))
nums2 = list(map(int, input("Enter second sorted array: ").split()))
data = Solution()
print(data.medianOfSortedArray(nums1, nums2))