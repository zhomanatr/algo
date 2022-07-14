def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    elem = seq[0]
    left = list(filter(lambda x: x < elem, seq))
    center = [i for i in seq if i == elem]
    right = list(filter(lambda x: x > elem, seq))

    return quick_sort(left) + center + quick_sort(right)


# Слияние двух списков (моя реализация)
def merge_method(seq1, seq2):
    i = 0
    j = 0
    merged_seq = []
    while i < len(seq1) and j < len(seq2):
        if seq1[i] < seq2[j]:
            merged_seq += [seq1[i]]
            i += 1
        else:
            merged_seq += [seq2[j]]
            j += 1

    if i == len(seq1) and j != len(seq2):
        while j < len(seq2):
            merged_seq += [seq2[j]]
            j += 1
    elif j == len(seq2) and i != len(seq1):
        while i < len(seq1):
            merged_seq += [seq1[i]]
            i += 1

    return merged_seq

def merge_method_2(seq1, seq2):
    i = 0
    j = 0
    merged_seq = []
    while i < len(seq1) and j < len(seq2):
        if seq1[i] < seq2[j]:
            merged_seq += [seq1[i]]
            i += 1
        else:
            merged_seq += [seq2[j]]
            j += 1

    while j < len(seq2):
        merged_seq += [seq2[j]]
        j += 1

    while i < len(seq1):
        merged_seq += [seq1[i]]
        i += 1

    return merged_seq

print(merge_method_2([1,1],[2,3,4]))