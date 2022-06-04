# Моя реализация
def find2Max(seq):
    ans1 = seq[0]
    ans2 = seq[0]
    for i in range(1,len(seq)):
        if seq[i] > ans1:
            ans2 = ans1
            ans1 = seq[i]
    return (ans1, ans2)

# Реализация учителя
def find2Max_ya(seq):
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])

    for i in range(2, len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]

    return (max1, max2)

# Моя реализация
def findMinEven(seq):
    ans = seq[0]

    for i in range(1, len(seq)):
        if seq[i] % 2 == 0 and seq[i] < ans:
            ans = seq[i]

    if ans % 2 == 0:
        return ans
    else:
        return -1

# Реализация учителя
def findMinEven_ya(seq):
    ans = -1
    flag = False

    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (not flag or seq[i] < ans):
            ans = seq[i]
            flag = True
    return ans

# Реализация учителя
def printMinWords(text):
    minLen = len(text[0])

    for word in text:
        if len(word) < minLen:
            minLen = len(word)
    ans = []
    for word in text:
        if len(word) == minLen:
            ans.append(word)
    return ' '.join(ans)


# Моя реализация
def reduceStr(text):
    reducedStr = []
    symbol_count = 0
    cur_symbol = text[0]

    for symbol in text:
        if symbol == cur_symbol:
            symbol_count += 1
        else:
            if symbol_count == 1:
                reducedStr.append(cur_symbol)
                cur_symbol = symbol
                symbol_count = 1
            else:
                reducedStr.append(cur_symbol + str(symbol_count))
                cur_symbol = symbol
                symbol_count = 1

    reducedStr.append(cur_symbol + str(symbol_count) if symbol_count > 1 else '')

    return ''.join(reducedStr)


# Реализация учителя
# собираем просто символы из текста
def collectSymbols(text):
    lastSym = text[0]
    ans = []

    for i in range(len(text)):
        if text[i] != lastSym:
            ans.append(lastSym)
            lastSym = text[i]
    ans.append(lastSym)
    return ''.join(ans)

# Собираем символы с их кол-вом
def collectSymWithCnt(text):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    lastSym = text[0]
    lastPos = 0
    ans = []

    for i in range(len(text)):
        if text[i] != lastSym:
            ans.append(pack(text[lastPos], i - lastPos))
            lastSym = text[i]
            lastPos = i

    ans.append(pack(text[lastPos], len(text) - lastPos))

    return ''.join(ans)

a = collectSymWithCnt('AAAAABBBBBBCDDDDDDAAAAABBBBB')
print(a)