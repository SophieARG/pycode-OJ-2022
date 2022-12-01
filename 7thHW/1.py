from collections import deque
for i in range(int(input())):
    queue, stack = deque([]), []
    going = True
    for j in range(int(input())):
        cmd = input()
        if going:
            if cmd == 'pop':
                if stack:
                    queue.popleft()
                    stack.pop()
                else:
                    going = False
            else:
                num = cmd.split()[1]
                queue.append(num)
                stack.append(num)
    if going:
        print(' '.join(queue), ' '.join(stack), sep='\n')
    else:
        print('error\nerror')
