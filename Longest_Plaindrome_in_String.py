class Solution:
    def LongestPalindrome(self, s:str) ->str:
        n = len(s)
        res = ""
        for i in range(n):
            for j in range(i,n):
                temp = s[i:j+1]
                if temp == temp[::-1] and len(temp)>len(res):
                    res = temp
        return res

user = input("Enter the Data : ")
data = Solution()
print(data.LongestPalindrome(user))