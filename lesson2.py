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

a = find2Max_ya([2,3,3,5,1,5,2,3,1])
print(a)
