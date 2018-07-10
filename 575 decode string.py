class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        def peekStack(stack):
            if stack:
                return stack[-1]
            else:
                return None


        recordStack = []
        reverseStack = []

        for char in s:
            if char != "]":
                recordStack.append(char)
            else:
                cur = recordStack.pop()
                while cur != "[":
                    reverseStack.append(cur)
                    cur = recordStack.pop()
                if cur == "[":
                    temp = ""
                    while reverseStack:
                        temp += reverseStack.pop()

                coef = ""
                while peekStack(recordStack) and peekStack(recordStack).isnumeric():
                    cur = recordStack.pop()
                    coef = cur + coef

                if coef != "":
                    concat = ""
                    for i in range(int(coef)):
                        concat += temp
                    recordStack.append(concat)
                else:
                    recordStack.append(temp)


        while recordStack:
            reverseStack.append(recordStack.pop())
        
        res = ""
        while reverseStack:
            res += reverseStack.pop()

        return res

print(Solution().expressionExpand("2[0[ab]5[0[abc]xy]uw]1[k]7[17[5[a]bcd]eok]1[haha]2[heihie]4[nihao]3[12[bc]4[t]]"))
