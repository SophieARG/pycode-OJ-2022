allchars = ''.join((chr(n) for n in range(65, 91))) * 2
print(''.join((allchars[ord(char) - 62] for char in input())))
