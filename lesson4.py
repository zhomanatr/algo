# Сортировка подсчетом
def countSort(seq):
    minVal = min(seq)
    maxVal = max(seq)
    k = maxVal - minVal + 1
    count = [0] * k
    for num in seq:
        count[num - minVal] += 1
    seqPos = 0
    for val in range(k):
        for i in range(count[val]):
            seq[seqPos] = val + minVal
            seqPos += 1


# Будут ли одинаковы 2 числа, если поменять местами их цифры
def isDigitPermutation(x, y):
    def countDigits(num):
        digits = [0] * 10
        while num > 0:
            lastNum = num % 10
            digits[lastNum] += 1
            num //= 10
        return digits

    num1 = countDigits(x)
    num2 = countDigits(y)

    for digit in range(10):
        if num1[digit] != num2[digit]:
            return False
    return True

    # or return num1 == num2

# Задача с ладьями, которые могут бить друг друга
def countBeatingRooks(rookcoords):
    def addRook(roworcol, key):
        if key not in roworcol:
            roworcol[key] = 0
        roworcol[key] += 1

    def countPairs(roworcol):
        pairs = 0
        for key in roworcol:
            pairs += roworcol[key] - 1
        return pairs

    rooksInRow = {}
    rooksInCol = {}

    for row, col in rookcoords:
        addRook(rooksInRow, row)
        addRook(rooksInCol, col)
    return countPairs(rooksInRow) + countPairs(rooksInCol)

# Вывести гистограмму
def printChart(text):
    symDict = {}
    maxSymCount = 0
    for key in text:
        if key not in symDict:
            symDict[key] = 0
        symDict[key] += 1
        maxSymCount = max(maxSymCount, symDict[key])  # можно максимум искать сразу так в одном проходе

    sortedUniqSyms = sorted(symDict.keys())
    for row in range(maxSymCount, 0, -1):
        for sym in sortedUniqSyms:
            if symDict[sym] >= row:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sortedUniqSyms))


# Отсортировать слова в списке
def sortWords(words):
    SymsDict = {}
    for word in words:
        sortedWord = ''.join(sorted(word))
        if sortedWord not in SymsDict:
            SymsDict[sortedWord] = []
        SymsDict[sortedWord].append(word)

    outputList = []
    for key in SymsDict:
        outputList.append(SymsDict[key])

    return outputList

a = sortWords(['joma','mama','ajom','amam','rrrr'])
