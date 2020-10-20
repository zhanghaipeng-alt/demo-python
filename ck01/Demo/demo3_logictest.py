# if 表达式：
#     执行于语句
# 判断输入是否能被3和7 整除
# str = input()
#
# if str.isdigit() or str.startswith('-') or str[1:].isdigit():
#     str = int(str)
#     if str > 0:
#         if str%3 == 0 and str%7 == 0:
#             print(f'{str}是可以同时被7和3整除的数字！')
#         else:
#             print(f'{str}不能被3和7整除')
#     else:
#         print(f'{str}是负数')
# else:
#     print(f'{str}是非数字')

#使用if else 输出月份
# month = input('请输入月份：')
#
# if month.isdigit():
#     month = int(month)
#     if month in range(1,13):
#         if month in [1,3,5,7,8,10,12]:
#             print(f'{month}月有31天！')
#         elif month in [4,6,9,11]:
#             print(f'{month}月有30天')
#         else:
#             print(f'{month}月平年有28天，闰年有29天')
#     else:
#         print('请输入1-12')
# else:
#     print('请输入整数！')


# for循环 for x in y:
# y是序列或集合元素类型，如string 类型，元组，列表。

#1.次数较少 且可以列出
# for i in 'hello world':
#     print(i, end=',')

#2.打印每个数的平方[1,2,3,5,9]
# for x in [1, 2, 3, 5, 9, 4]:
#     print(f'{x}的平方为{pow(x,2)}', end='  ')

#3.输入一行字符，统计个数
# str1 = input('输入字符串：')
# number = 0
# num_letter = 0
# num_enter = 0
# num_other = 0
# for i in str1:
#     if i.isdigit():
#         number += 1
#     elif i.isalpha():
#         num_letter += 1
#     elif i.isspace():
#         num_enter += 1
#     else:
#         num_other += 1
# print(f'共有数字{number}个，英文字符{num_letter}个，空格{num_enter}个，其它字符{num_other}个')


#4.循环中的步长和顺序  for i in range(a,b,2) a:边界包含。b:下边界不包含  2：步长，如果是-1  表示倒序
# 100以内偶数 倒序
# for i in range(100, -1, -2):
#     print(i)

#枚举循环：for …… in enumerate seq（） 适用于同时需要索引和值
# list1 = ['OPPO','VIVO','apple','三星','MI','MEIZU','huawei']
# for x,y in enumerate(list1):
#     print(f'销量排名第{x+1}的品牌是{y}')

#1000内的水仙花数
# for i in range(100,1000):
#     baiwie = i//100
#     shiwei = i%100//10
#     gewei = i%10
#
#     if pow(gewei,3) + pow(shiwei,3) + pow(baiwie,3) ==i:
#         print(f'{i}是水仙花数')

#100以内的质数
# for m in range(2, 101):
#     for n in range(2, m):
#         if m % n == 0:
#             break
#     else:
#         print(f'{m}是质数！')

# 矩形方阵
# a = 9
# b = 9

# for i in range(1,a):
#     for j in range(1, b):
#         print('*', end='  ')
#     print('\n')

#空心方阵
# for i in range(1,a+1):
#     if i ==1 or i ==a:
#         for j in range(1, b+1):
#             print('*', end=' ')
#         print('\n')
#     else:
#         for j in range(1,b+1):
#             if j==1 or j==b:
#                 print('*',end=' ')
#
#             else:
#                 print(' ',end=' ')
#
#         print('\n')
# for i in range(0,a):
#     for j in range(0,b):
#         if i == 0 or i == a-1 or j == 0 or j == b-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print('')

##给定一个字符串，找出第一个不重复的字符

# str = input("输入字符串")
#
# for i in str:
#     if str.count(i) == 1:
#         print(f'第一个不重复的字母是{i},在字符串的第{str.find(i)+1}位')
#         break

## 1000以内的完数
# a = 10000
# for i in range(1,a+1):
#     count = 0
#     for j in range(1, i):
#         if i % j == 0:
#             count = count + j
#             # print(f'count={count}')
#     if i == count:
#         print(f'{i}是完备数')
