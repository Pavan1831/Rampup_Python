def longestValidParentheses(s):
    stack = []
    max_length = 0
    start = -1

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if not stack:
                start = i
            else:
                stack.pop()
                if not stack:
                    max_length = max(max_length, i - start)
                else:
                    max_length = max(max_length, i - stack[-1])

    return max_length

s = ")()()(()"
result = longestValidParentheses(s)
print(result)