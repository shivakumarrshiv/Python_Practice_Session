class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = -1
        last = -1
        
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        
        return [first, last]
            