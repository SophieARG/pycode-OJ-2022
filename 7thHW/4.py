digits = set('0123456789')
while True:
    try:
        chars = input() + ' '
        nums = ['']
        for char in chars:
            if char in digits:
                nums[-1] += char
            elif char == '.':
                nums.append('')
            else:
                if len(nums) == 4:
                    for num in nums:
                        if not (num and (num[0] != '0' or num == '0') and int(num) < 256):
                            break
                    else:
                        print('.'.join(nums))
                nums.clear()
                nums.append('')
    except EOFError:
        break
