# Interactor

# code = int(input())
# interactor = int(input())
# checker = int(input())
#
# if interactor == 0:
#     if code != 0:
#         print(3)
#     else:
#         print(checker)
# elif interactor == 1:
#     print(checker)
# elif interactor == 4:
#     if code != 0:
#         print(3)
#     else:
#         print(4)
# elif interactor == 6:
#     print(0)
# elif interactor == 7:
#     print(1)
# else:
#     print(interactor)


# Кольцевая линия

# params = list(map(int,input().split()))
# count = params[0]
# in_station = params[1]
# out_station = params[2]
#
# min_stations = 0
#
# if in_station < out_station:
#     if (out_station - in_station) - 1 > 0:
#         maybe_min1 = (out_station - in_station) - 1
#         maybe_min2 = (in_station - 1) +  (count - out_station)
#         min_stations = min(maybe_min1, maybe_min2)
# else:
#     if (in_station - out_station) - 1 > 0:
#         maybe_min1 = (in_station - out_station) - 1
#         maybe_min2 = (out_station - 1) + (count - in_station)
#         min_stations = min(maybe_min1, maybe_min2)
#
# print(min_stations)

# Даты
params = list(map(int,input().split()))
a = params[0]
b = params[1]
c = params[2]

if 1969 < c < 2070:
    if 0 < a < 13 and 0 < b < 13:
        print(0)
    else:
        print(1)
elif 1969 < b < 2070:
    if 0 < a < 13 and 0 < c < 13:
        print(0)
    else:
        print(1)
else:
    if 0 < b < 13 and 0 < c < 13:
        print(0)
    else:
        print(1)



print(0 < a < 13)