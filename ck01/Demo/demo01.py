#
# a = [1, 2, 3]
# b = [1, 2, 3]
#
# print(a == b)
# print(a is b)

# python中的连续赋值和互换赋值

# a=b=c=d=9
#
# print(a,b,c,d)
#
# e = 10
# f = 20
#
# e,f = f,e
# print(e,f)

#成员运算符in,  not in a in B:判断a集合是否在b集合中，返回bool值
# print('e' in 'hello')
#
# print(2 in [1,2,3])
#
# print(4 in (1,2,3))


#string 操作
# 字符串换行：使用''''''，可以输出带格式
# a = '''
#     你是个SB！
#         到积分
#             发毒奶粉
# '''
#
# print(a)

# 转义符:用特殊符号表示一些不能直接输入的字符
# 换行符 \n  \t
# b = 'dfaijijfa\\n'
# print(b)
#
# # 还原字符串
# c = r'I\'m ok'
# print(c)

#
# d = '''Bad said:
# I'm Ok.
# '''
#
# print(d)
#
# print(r"div[@id='goodietm']\a")
#
# print(r'Bad Said "I\'m OK"')

# 字符串的常用方法
# 三种拼接字符串的方法

# name = 'zhanghaipeng'
# card_id = 3456
# money = 5000.567
# data = '2020-09-30'
# source1 = '尊敬的%s: 您尾号为%d的账户%s收到入账%s，请查收！' %(name, card_id, data, money)
# 1.字符串的格式化输出
# print(source)

# 2.format函数（官方推荐方式）
# source2 = '尊敬的{name}：您尾号为{card_id}的账户{data}收到入账{money}，请查收'.format(
# #     name=name, card_id=card_id, data=data, money=money)
# # print(source2)

# 3.使用小写f 这是Python3支持的写法;在变量中还进行处理，引用对象等，money取两位小数
# source3 = f'尊敬的{name}：您尾号{card_id}的账户{data}收到入账{money:.2f}，请查收！'
# print(source3)


# 字符串的索引和切片
# str = 'zhanghaipeng is good man'
# print(len(str))
#
# # 按索引取值
# print(str[9])
# print(str[::2])
#
# # 字符串的翻转
# print(str[::-1])

# 字符串的拼接和切割 join() split()
# request = r'https://api.fclassroom.com/ud-api-student/api/v1/notebook/detail?studentId=4068368&schoolId=2000&dmQuestSourceId&options=ABCDEFG&paperQuestionIds=27237178&jkQuestionIds'
# # 分隔出请求部分和参数部分
# li = request.split('?')
# host = li[0]
# par = li[1]
# key = par.split('&')
#
# print(key)

# 拼接
# new_par = '&'.join(key) #参数部分
#
# request1 = f'{host}?{new_par}'
# request2 = '{host}?{new_par}'.format(host=host,new_par=new_par)
# request3 = '?'.join(li)
#
#
# print(request3)
