class Solution:
    def longestSubString(self, s:str)->str:
        start = 0
        max = 0

        for end in range(len(s)):
            for i in range(start,end):
                if s[i] == s[end]:
                    start = i+1
                    break
            current = end - start + 1
            if current > max:
                max = current
        return max
    
s = input()
data = Solution()
print(data.longestSubString(s))
