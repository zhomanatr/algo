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

def merge_sort(seq):
    if len(seq) == 1:
        return seq

    middle = len(seq) // 2

    left = merge_sort(seq[:middle])
    right = merge_sort(seq[middle:])

    return merge_method_2(left,right)



def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)

print(binary_search_recursive([1,5,6,10,12,14],1,0,6))
# print(merge_method_2([1,1],[2,3,4]))

def checkNum(index, params):
    seq,x = params

    return seq[index] >= x

def findFirstNum(seq, x):
    ans = lbinsearch(0, len(seq) - 1, checkNum, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans

def lbinsearch(l, r, check, params):
    while l < r:
        m = (l + r) // 2
        if checkNum(m, params):
            r = m
        else:
            l = m + 1
    return l

print(findFirstNum([1,2,3,4,5,5,6,6,6,8,9,10,11], 8))


class TreeNode:
    def __init__(self, value, root=None):
        self.value = value
        self.left = None
        self.right = None

        self.root = root


    # def add(self, value):
    #     # track current node (level)
    #     current_node = self
    #     # track parent node
    #     last_node = None
    #     # search the place to insert new node
    #     while current_node:
    #         last_node = current_node
    #
    #         if value > current_node.value:
    #             current_node = current_node.left
    #         elif value < current_node.value:
    #             current_node = current_node.right
    #         else:  # element already presented in tree
    #             return False
    #             # create new node and link it with parent
    #     new_node = TreeNode(value, last_node)
    #     if value > last_node.value:
    #         last_node.right = new_node
    #     else:
    #         last_node.left = new_node

    def insert(self, data):
        # Compare the new value with the parent node
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.value:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.value = data

    def searchElem(self, data):
        if self is None:
            return False
        elif self.value == data:
            return True
        elif self.value < data:
            self.right.searchElem(data)
        elif self.value > data:
            self.left.searchElem(data)

    # def findval(self, word):
    #     if self.data.startswith(word):
    #         print(f"{self.data} is found!")
    #     elif self.left is not None:
    #         return self.left.findval(word)
    #     elif self.right is not None:
    #         return self.right.findval(word)
    #     else:
    #         return print("Not found!")


root = TreeNode(10)
root.insert(5)
root.insert(7)
root.insert(6)
root.insert(8)
root.insert(4)

print(root.searchElem(5))

# root = TreeNode(10)
# root.add(9)
# root.add(8)

# tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.right = TreeNode(3)
# tree.left.left = TreeNode(4)
# tree.left.right = TreeNode(5)


# Выводит родителя до всех его потомков
def pre_order(node): # Прямой
    if node:
        print(node.value) # сначала выводим родителя
        pre_order(node.left)
        pre_order(node.right)


# Выводит потомков, а затем родителя
def post_order(node): # обратный
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)



# выводит левого потомка, затем родителя, затем правого потомка
def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)


a = 4

print(a) if a > 5 else print(1)


def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)


def selection_sort(nums):
    # значение i соответствует тому, сколько значений было отсортировано
    for i in range(len(nums)):
        # Мы предполагаем, что первый элемент несортированного сегмента является наименьшим
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Поменять местами значения самого низкого несортированного элемента с первым несортированным
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
# Проверяем, что это работает
random_list_of_nums = [12, 8, 3, 20, 11]
selection_sort(random_list_of_nums)
print(random_list_of_nums)


A = ['AA', 'BB', 'CCC', 'D']
A.sort(key=lambda x: len(x),reverse=True)
print(A)
