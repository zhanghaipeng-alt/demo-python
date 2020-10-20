# Python字典的特性
# 特性1：字段的key值是以set集合形式存储的，key不重复！
# 特性2：key值的常用类型：string 整型
# 特性3：value值可以重复，并且可以是任何数据类型
# 特性4：Python2字典是无序的，Python3按照进入顺序排列，但是也是无序的

# dict1 = {'name':'tony','ege':36,'address':'beijing','salary':34000.00,'other':''}

# 取值
# 1.使用key值 []内添加正确的key值，但是如果key不存在则会报错
# print(dict1['name'])

# 2.使用get方法，也是直接获取key值，不同的是当可以不存在是系统返回none，不报错
# print(dict1.get('name1'))

# 赋值
# key不存在时：直接添加新的key
# dict1['sex'] = '男'
# print(dict1,id(dict1))
#
# # 当key存在时，改变value的值
# dict1['sex'] = '女'
# print(dict1,id(dict1))

# 删除：使用del
# 删除整个字典
# del dict1
# print(dict1)

# 删除字典中某一项
# del dict1['other']
# print(dict1)

# 字典的一些方法
# 1.取所有的value，Python3这个值是一个对象
# print(dict1.values())
# print(list(dict1.values()))

# 获取所有的key
# print(list(dict1.keys()))
# # 获取所有的value
# print(dict1.values())
#
# # 获取所有项
# print(dict1.items())
#
# # 弹出/删除
# dict1.pop('other')
# print(dict1)
#
# dict1.clear()
# print(dict1)


# 快速构建字典 通过一个列表构建
# name = ['zhangsan', 'lisi', 'xiaoming','zhangsan']
# dict2 = dict.fromkeys(name)
# print(dict2)

# 然后给其中的某一项赋值
# dict2['zhangsan'] = 8799
# print(dict2)

# 构建成的新字典会自动去重，利用这个功能可以实现list的去重
# print(list((dict.fromkeys(name)).keys()))

# 使用字典构建一个字符串
# list1 = []
# for key,value in dict1.items():
#     list1.append(f'{key}={value}')
# print(list1)
#
# str1 = ','.join(list1)
# print(str1)

# 练习1：计算打车费用
# charge = {'zhangsan':230,'lisi':45.0,'wangwu':980.0,'zhaoliu':76.3}
# charge1 = {'技术部':[23,56.55,90],'销售部':[350.0,45],'财务部':[35,98,43,120.0]}

# sum = 0
# for value in charge.values():
#     sum += value
# print(sum)
# print(sum(charge.values()))
# print(sum(list(charge.values())))
#
# # sum = 0
# # for value in charge1.values():
# #     for j in value:
# #         sum += j
# # print(sum)
#
# total = 0
# for value in charge1.values():
#     total += sum(value)
# print(total)
#
# 分别统计费用大于500 和小于500的人
# dic1 = {'张无忌':670.0, '谢逊':123.99, '赵敏': 340, '周芷若':990, '张三丰':1300, '杨逍':450}
# result = {}
# more = []
# less = []
#
# for name, fee in dic1.items():
#     if fee > 500.0:
#         more.append(name)
#     else:
#         less.append(name)
# result['报销费用大于500的'] = more
# result['报复费用小于500的'] = less
# print(result)

# 平均费用
# 打车最多的人
# max = 0
# max_name = ''
# avg = 0
# total = 0
#
# for name, fee in dic1.items():
#     total += fee
#     if fee > max:
#         max = fee
#         max_name = (list(dic1.keys()))[list(dic1.values()).index(fee)]
# # avg = '%.2f'%(total/len(dic1))
# avg = round(total/len(dic1), 2)
# print(avg, max_name)
# print(list(dic1.keys())[list(dic1.values())])

# data = {
#     'zhaomin':[87,67,90],
#     'chengdu':[100,65,94],
#     'shanghai':[75,89,99],
#     'yunnan':[40,37,89],
#     'zhengzhou':[100,59,77],
#     'wuhan':[98,49,82]
# }

# 求平均分不及格的人
# avg = 0
# for name,value in data.items():
#     avg = sum(value)/len(value)
#     if avg < 60:
#         print(name)

# 分别求出各科分数最高的人
# chinese = []
# math_list =[]
# english = []
#
# for s in data.values():
#     chinese.append(s[0])
#     math_list.append(s[1])
#     english.append(s[2])
#
# for key,value in data.items():
#     if value[0] == max(chinese):
#         print(f'语文学霸是{key}')
#     if value[1] == max(math_list):
#         print(f'数学学霸是{key}')
#     if value[2] == max(english):
#         print(f'英语学霸是{key}')
# print(chinese, math_list,english)

# 统计一篇文章单次出现的次数，取前五 以字典形式输出
# data = '''
# There are moments in life when you miss someone so much that you just want to pick them from your dreams and hug them for real! Dream what you want to dream;go where you want to go;be what you want to be,because you have only one life and one chance to do all the things you want to do.
#
# 　　May you have enough happiness to make you sweet,enough trials to make you strong,enough sorrow to keep you human,enough hope to make you happy? Always put yourself in others’shoes.If you feel that it hurts you,it probably hurts the other person, too.
#
# 　　The happiest of people don’t necessarily have the best of everything;they just make the most of everything that comes along their way.Happiness lies for those who cry,those who hurt, those who have searched,and those who have tried,for only they can appreciate the importance of people
#
# 　　who have touched their lives.Love begins with a smile,grows with a kiss and ends with a tear.The brightest future will always be based on a forgotten past, you can’t go on well in lifeuntil you let go of your past failures and heartaches.
# '''
# # 切割,判断英文单词
# words = []
# words_p = []
# words = data.split(' ')
#
# for w in words:
#     if w.isalpha():
#         words_p.append(w)
#     elif w[:-1].isalpha() and w[-1] in (',','.','?','!'):
#         words_p.append(w[0:-1])
#
#
# #去重
# words_sigle = []
# for w in words_p:
#     if w not in words_sigle:
#         words_sigle.append(w)
# # print(words_sigle)
# # 统计数量
# amount = []
# for w in words_sigle:
#     count = words_p.count(w)
#     amount.append((count,w))
# # print(amount)
# # 排序
# amount.sort(reverse=True)
# amount = amount[:5]
# # print(amount)
# # 组成字典
# dic = {}
# for w in amount:
#     dic[w[1]] = w[0]
# print(dic)
#

# 字典的排序（实际上字典是不能排序的，但是可以通过系统函数sorted 通过关键字进行排序）
# 按照分数排序:排序结果实际上是列表，key是排序规则 sources.items()——排序源,key=lambda x:x[1]——规则定义
sources = {'zh':36,'li':89,'chen':98,'liu':65}
target = sorted(sources.items(),key=lambda x:x[1],reverse=True)
print(type(target),target)
