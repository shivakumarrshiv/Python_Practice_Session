class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = [""]
        for i in range(len(digits)):  
            temp = []
            for j in range(len(result)):  
                for k in range(len(mapping[digits[i]])):  
                    temp.append(result[j] + mapping[digits[i]][k])  
            result = temp  
        
        return result