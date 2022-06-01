'''Найти самый часто встречающийся символ в тексте'''

'''
                              Решение №1
Переберем все позиции текста и для каждой позиции в тексте еще раз
переберем все позиции и в случае совпадения прибавим к счетчику единицу.
Найдем максимальное значение счетчика.

Сложность алгоритма - O(N^2).
'''

# text = igit nput()
# ans = ''
# ans_count = 0
#
# for i in range(len(text)):
#     cur_count = 0
#     for j in range(len(text)):
#         if text[i] == text[j]:
#             cur_count += 1
#     if cur_count > ans_count:
#         ans = text[i]
#         ans_count = cur_count
#
# print(ans)

# как вариант
# print(max(map(lambda x: (text.count(x), x), text))[1])

'''
                              Решение №2
Переберем только символы, встречающиеся в тексте, а затем переберем все
позиции и в случае совпадения прибавим к счетчику единицу. Найдем максимальное
значение счетчика.

Сложность алгоритма - O(N * k).
'''

# text = input()
# ans = ''
# ans_count = 0
#
# for symbol in set(text):
#     cur_count = 0
#     for j in range(len(text)):
#         if symbol == text[j]:
#             cur_count += 1
#     if cur_count > ans_count:
#         ans = symbol
#         ans_count = cur_count
#
# print(ans)

'''
                              Решение №3
Создадим словарь, где ключом является символ, а значением - сколько раз встретился.
Если символ встретился впервые - создаем элемент словаря с ключом и значением 0. 
Прибавляем к элементу словаря с ключом единицу.

Сложность алгоритма - O(N + k) ~ O(N).
'''

# text = input()
# ans = ''
# ans_count = 0
# dict = {}
#
# for symbol in text:
#     if symbol not in dict:
#         dict[symbol] = 0
#     dict[symbol] += 1
#
# for key, value in dict.items():
#     if value > ans_count:
#         ans = key
#         ans_count = value
#
# print(ans)

# Решение №3 (модифицированное)

# text = input()
# ans = ''
# ans_count = 0
# dict = {}
#
# for symbol in text:
#     if symbol not in dict:
#         dict[symbol] = 0
#     dict[symbol] += 1
#
#     if dict[symbol] > ans_count:
#         ans = symbol
#         ans_count = dict[symbol]
#
# print(ans)