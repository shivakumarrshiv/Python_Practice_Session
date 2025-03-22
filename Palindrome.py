class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse = 0
        temp = x
        while temp > 0:
            last = temp % 10
            reverse = reverse * 10 + last
            temp = temp // 10

        return reverse == x
