# 回溯法
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dicts = {
            '2':["a","b","c"],
            '3':["d","e","f"],
            '4':["g","h","i"],
            '5':["j","k","l"],
            '6':["m","n","o"],
            '7':["p","q","r","s"],
            '8':["t","u","v"],
            '9':["w","x","y","z"]
        }
        combinations = []
        combination = []
        def back(index:int):
            if index == len(digits):
                combinations.append(''.join(combination))
            else:
                digit = digits[index]
                for letter in dicts[digit]:
                    combination.append(letter)
                    back(index+1)
                    combination.pop()
        back(0)
        return combinations
    
# 迭代扩展法
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
        }
        ans = d[digits[0]]
        if len(digits) == 1:
            return ans
        for n in digits[1:]:
            ans = [a + b for a in ans for b in d[n]]
        return ans