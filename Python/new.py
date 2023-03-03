# v = input()
# a = int(v[0])
# b = int(v[1])
# c = int(v[2])
# d = int(v[3])
# e = int(v[4])
# f = int(v[5])
#
# if a + b + c == d + e + f:
#     print('Счастливый')
# else:
#     print("Обычный")
#########################################
# print("Введите начальное число")
# a = int(input())
# print("Введите какое кол-во нечетных чисел хотите получить")
# dec = int(input())
#
# while dec > 0:
#     if a % 2 == 1:
#         print(a)
#         a += 1
#         dec -= 1
#     else:
#         a += 1
#########################################
# a = '*'
# g = 7
# i = 0
# print(i % 2)
# re = 1
# while 0 < g <= 7:
#     print(" " * g, a * re)
#     g -= 1
#     re += 1
#########################################
# a = int(input())
# b = int(input())
# v = 0
# while a != b + 1:
#     v += a
#     a = a + 1
# print("\n", v)
# считает сумму введеных значений
# SUM = 0
# while True:
#     x = int(input())
#     if x != 0:
#         SUM += x
#     else:
#         print(SUM)
#         exit(False)
#########################################
# В Институте биоинформатики между информатиками и биологами устраивается соревнование. Победителям соревнования достанется большой и вкусный пирог. В команде биологов
# a
# a человек, а в команде информатиков —
# b
# b человек.
#
# Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.
#
# Напишите программу, которая помогает найти это число.
# Программа должна считывать размеры команд (два положительных целых числа
# a и b, каждое число вводится на отдельной строке) и выводить наименьшее число
# d, которое делится на оба этих числа без остатка.

# a = int(input())
# b = int(input())
# d = min(a, b)
# while d % a != 0 or d % b != 0:
#     d += 1
# print(d)
# d = ""
#########################################
# while True:
#     a = int(input())
#     if a < 10:
#         continue
#     elif a > 100:
#         break
#     else:
#         d = d + str(a) + '\n'
# print(d)
#########################################
# a = int(input())
# b = int(input())
# x = int(input())
# y = int(input())
# for i in range(x, y + 1):
#     print('\t', i, '\t', end='')
# print()
# for j in range(a, b + 1):
#     print(j, end='\t')
#     for k in range(x, y + 1):
#         print(k * j, end='\t')
#     print()
#########################################
# a, b = (int(i) for i in input().split())
# s=0
# n=0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         s += i
#         n+=1
# print(s/n)
##########################################
# a = input()
# a = a.lower()
# print((a.count('c')+a.count('g'))/len(a)*100)
##########################################
# s = 'abcdefghijk'
# print(s[3:6])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-3:])
# print(s[:-6])
# print(s[-1:-10:-2])
###########################################
# a = input()
# i = 0
# count = 1
# while i <= len(a)-1:
#     if i != len(a)-1:
#         if a[i] == a[(i + 1)]:
#             count += 1
#         else:
#             print(a[i], count, sep='', end='')
#             count = 1
#         i += 1
#     else:
#         print(a[i], count, sep='')
#         break
###########################################
# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# print(students)
###########################################
# a = [int(i) for i in input().split()]
# if len(a) != 1:
#     for i in range(len(a)):
#         if i == len(a)-1:
#             print(a[i-1]+a[i-i], end=' ')
#         else:
#             print(a[i-1]+a[i+1], end=' ')
# else:
#     print(a[0])
###########################################
# a = [int(j) for j in input().split()]
# i = min(a)
# while i <= max(a):
#     if a.count(i) > 1:
#         print(i, end=' ')
#     i += 1
###########################################
# a = [int(i) for i in input().split()]
# print(a)
# s = 0
# s2 = 0
# while True:
#     a = int(input())
#     if a != 0:
#         s += a
#         s2 += a*a
#         if s == 0:
#             print(s2)
#             break
#     elif a == 0 and s == 0:
#         print(a)
#         break
#######################################
# a = []
# b = int(input())
# if b == 0:
#     print(b)
# while len(a) <= b-1:
#     for i in range(b+1):
#         if i > 0:
#             for j in range(i):
#                 if len(a) <= b-1:
#                     a.append(i)
#                     print(i, end=' ')
#                 j += 1
#         i += 1
#######################################
# a, b = [int(i) for i in input().split()], [int(i) for i in input().split()]
# c = []
# if a.count(b[0]) > 0:
#     i = a.index(b[0])
#     for j in range(len(a)):
#         if a[j] == b[0]:
#             c.append(j)
#     print(*c)
# else:
#     print("Отсутствует")
######################################
# t = ""
# n = []
# while True:
#     t = input()
#     if t == 'end':
#         for i in range(len(n)):
#             for j in range(len(n[0])):
#                 if i == len(n) - 1 and len(n[0])-1 == j and i >= 0:
#                     print(n[i - 1][j] + n[0][j] + n[i][j - 1] + n[i][0])
#                     print(t)
#                     exit()
#                 elif i == len(n) - 1:
#                     print(n[i - 1][j] + n[0][j] + n[i][j - 1] + n[i][j + 1], end=' ')
#                 elif j == len(n[0]) - 1:
#                     print(n[i - 1][j] + n[i + 1][j] + n[i][j - 1] + n[i][0], end=' ')
#                 else:
#                     print(n[i - 1][j] + n[i + 1][j] + n[i][j - 1] + n[i][j + 1], end=' ')
#             print()
#     else:
#         n.append([int(i) for i in t.split()])
#######################################################
# n = int(input())
# a = [[0 for i in range(n)] for j in range(n)]
# count = 1
# d = len(a)
# c = 0
# print("Длинна=", d, '\n', 'Range=', range(len(a)))
# for i in range(c, d):
#     if d-c == 1:
#         a[c][c] = count
#         break
#     for j in range(c, d):  # вправо
#         if j == d - 1:
#             for ij in range(c, d):  # вниз
#                 if ij == d - 1:
#                     for jj in range(c, d+1):  # влево
#                         if jj == c:
#                             continue
#                         elif jj == d:
#                             for k in range(c, d+1):  # вверх
#                                 if k == c:
#                                     continue
#                                 elif c < k < d:
#                                     a[-k][-jj+n] = count
#                                     count += 1
#                                 else:
#                                     c += 1
#                                     d -= 1
#                         else:
#                             a[ij][(-jj)] = count
#                             count += 1
#                 else:
#                     a[ij][j] = count
#                     count += 1
#         else:
#             a[i][j] = count
#             count += 1
# for i in range(len(a)):
#     for j in range(len(a)):
#         print(a[i][j], end=' ')
#     print()
##################################################
# def functian(x):
#     if x <= -2:
#         print(1 - ((x + 2) ** 2))
#     if -2 < x <= 2:
#         print(-(x / 2))
#     if x > 2:
#         print((x - 2) ** 2 + 1)
# functian(input())
#################################################
# l = [0, 0, 0]
# def modify_list(l):
#     while True:
#         for i in range(1,10,2):
#             if l.count(i)>0:
#                 l.remove(i)
#                 break
#             else:
#                 continue
#         if i == 9 and l.count(i) == 0:
#             for i in l:
#                 l.insert(l.index(i), i//2)
#                 l.remove(i)
#             break
# modify_list(l)
# print(l)
#################################################

# def update_dictionary(d, key, value):
#    if key in d:
#        d[key].append(value)
#    else:
#        if 2*key in d:
#            d[2*key].append(value)
#        else:
#            d[2*key] = [value]
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)  # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)  # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)  # {2: [-1, -2, -3]}
##############################################
# n=''
# n = str(input())
# m = []
# m.append([str(s.lower()) for s in n.split()]) 
# d = {}
# li, lj = len(m), len(m[0])
# for i in range(li):
#     for j in range(lj):
#         p = m[i][j]
#         if p in d:
#             d[p]+=1
#         else:
#             d[p] = 1
# for key,value in d.items():
#     print(key,value)
#############################################
# d={}
# k=[]
# n=int(input())
# for i in range(n):
#     x = int(input())
#     k.append(x)
# for j in range(0,len(k)):
#     key=k[j]
#     if  key in d:
#         print(d[key])
#     elif key not in d:
#         p = k[j]
#         d[key]=f(p)
#         print(d.get(key))
#################################################
# with open ('text.txt') as inf:
#     s = inf.readline()
#     print(s)
#     m, y, sd = '','',''
#     for i in range(len(s)):
#         if s[i]< 'A':
#             if i < len(s)-1:
#                 m += s[i]
#                 if s[i+1]>= 'A':
#                     sd += int(m)*y
#                     # print(int(m)*y,end='')
#                     m, y = '',''
#             else:
#                 m += s[i]
#                 sd += int(m)*y
#                 # print(int(m)*y)
#         else:
#             y += s[i]
# with open('text2.txt', 'w') as ind:
#     ind.write(str(sd))
#############################################
# import math
# print(2*math.pi*(float(input())))
#############################################
# a,b,c = (int(input()) for i in range(3))    # ввод используя range
a = 'fffrrfsfsadw'
print(a[-4:])