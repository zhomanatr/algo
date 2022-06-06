# Сортировка подсчетом
def countSort(seq):
    minVal = min(seq)
    maxVal = max(seq)
    k = maxVal - minVal + 1
    count = [0 for _ in range(k)]
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

# a = isDigitPermutation(2056,5026)
# print(a)
seq = [10,12,11,-1,5,6,3,5,10,11]
b = countSort(seq)
print(seq)