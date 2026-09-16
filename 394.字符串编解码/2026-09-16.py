class Solution:
    def decodeString(self, s: str) -> str:
        def decode(i):
            res = ""
            while i < len(s):
                if s[i].isalpha():
                    res += s[i]
                    i += 1
                elif s[i].isdigit():
                    num = 0
                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    
                    # 跳出循环，说明此时i指向'['
                    i+=1
                    sub,i = decode(i)
                    res += sub*num
                elif s[i]==']':
                    return res,i+1
            # 循环结束后，必须返回，否则最后的res将无法返回出
            return res,i
        res,_ = decode(0)
        return res