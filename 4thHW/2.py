words, pool = {}, {}
while True:
    try:
        word = input()
        for i in range(1, len(word) + 1):
            pre = word[:i]
            if pre in pool:
                if pool[pre] is not None:
                    _i, _word = pool[pre]
                    pool[pre] = None
                    newi = _i + 1
                    newpre = _word[:newi]
                    pool[newpre] = (newi, _word) if newi < len(_word) else None
                    words[_word] = newpre
            else:
                pool[pre] = (i, word)
                words[word] = pre
                break
        else:
            words[word] = word
    except EOFError:
        break
for word, pre in words.items():
    print(word, pre)
