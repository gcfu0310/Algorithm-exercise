class Solution:
    def isValid(self, s: str) -> bool:
        path = []
        mapping = {
            ']':'[',
            ')':'(',
            '}':'{'
        }
        # 字符串是奇数，一定是无效
        if len(s)%2==1:
            return False
        else:
        # 遍历字符串中所有括号
            for k in s:
                # 如果是右括号
                if k in mapping:
                    # 如果path非空，将栈的顶部弹出
                    if path:
                        top = path.pop()
                    else:
                        # 如果path是空的且当前是右括号，一定无效
                        return False
                    # 弹出的字符若与右括号不必配，一定无效
                    if top != mapping[k]:
                        return False
                else:
                    # 左括号就添加进栈中
                    path.append(k)
            # 检查栈是否封闭
            return len(path)==0



