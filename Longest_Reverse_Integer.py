class Solution:
    def reverse(self, x : int)->int:
        if x == 0:
            return 0
        if x<0:
            temp = -(x)
        elif x>0:
            temp = x
        reverse = 0
        
        while temp>0: #123
            last = temp%10
            reverse = reverse*10 +last
            temp = temp//10

        if reverse > 2**31 - 1:
            return 0
        
        if x>0:
            return reverse
        else:
            return -reverse 

n = -125
data=Solution()
print(data.reverse(n))