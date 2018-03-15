def longestValidParentheses(s):
        """
        :type s: str
        :rtype: int
        """
       
        stack = []
        n = len(s)
        maxlen = 0
        stack.append(-1)
        print(stack)
        for i in range(n):
            #if  stack[len(stack) - 1] == -1 or s[stack[len(stack) - 1]] == ')':
            #    stack.append(i)
            #    print(stack)
            if stack[len(stack) - 1] != -1 and s[i] == ')' and s[stack[len(stack) - 1]] == '(':
                stack.pop()
                print(stack)
                tmplen = i - stack[len(stack) - 1]
                print("tmp:", tmplen)
                if maxlen < tmplen: maxlen = tmplen
            else: stack.append(i)
        return maxlen

s = ")()())()()("
print(longestValidParentheses(s))