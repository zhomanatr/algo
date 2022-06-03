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

a = printMinWords(['aaaaaa', 'bb', 'bbb', 'ccc', 'dd'])
print(a)