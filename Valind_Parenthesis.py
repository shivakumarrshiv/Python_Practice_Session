class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(", "]":"[", "}":"{"}
        stack = []
        for char in s:
            if char in brackets:
                if len(stack)>0:
                    target = stack[len(stack)-1]
                    if target == brackets[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
         
                
char = input("Enter the Parenthiesis : ")
data = Solution()
print(data.isValid(char))