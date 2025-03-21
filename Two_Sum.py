class Solution:
    def twoSUm(self, num : list[int], target:int)->list[int]:
        n = len(num)
        for i in range(n):
            for j in range(i+1,n):
                if num[i]+num[j]== target:
                    return (i,j)
                
n=list(map(int, input("Enter the numbers seprated by space").split()))
target = int(input("Enter the target value : "))
data = Solution()
print(data.twoSUm(n,target))