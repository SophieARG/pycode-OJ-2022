stack = []
matched = {')': '(', ']': '[', '}': '{'}
for char in input():
    if char in matched:
        if stack and stack[-1] == matched[char]:
            stack.pop()
        else:
            print('no')
            break
    else:
        stack.append(char)
else:
    print('no' if stack else 'yes')
