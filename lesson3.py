# Создание собственного (мульти)множества

setsize = 10
myset = [[] for _ in range(setsize)]

def add(x):
    myset[x % setsize].append(x)

def find(x):
    for elem in myset[x % setsize]:
        if elem == x:
            return True
    return False

def delete(x):
    in_list = myset[x % setsize]
    for i in range(len(in_list)):
        if in_list[i] == x:
            in_list[i] = in_list[len(in_list) - 1]  # поставить на место найденного элемента последний
            in_list.pop()  # удалить последний элемент
            return
