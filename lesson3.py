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


# Найти в списке 2 различных числа, сумма которых равна х
def a_plus_b(nums, x):
   prevNums = set()

   for num in nums:
      if (x - num) in prevNums:
         return num, x - num
      prevNums.add(num)

   return 0, 0

#

def wordsInDict(dictionary, text):
   words = set(dictionary)

   for word in dictionary:
      for pos in range(len(word)):
         words.add(words[:pos] + words[pos + 1:])
   ans = []

   for word in text:
      ans.append(word in words)

   return ans

