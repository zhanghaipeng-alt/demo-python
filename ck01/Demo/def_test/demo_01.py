'''
def 函数名 （参数列表）：
    函数体
'''

# def my_method(a,b=[]):
# #     b.append(a)
# #     print(b)
# # my_method(0,['a','b'])
# # my_method(1)
# # my_method(2)
#
# def my_method(a,b=None):
#     if b is None:
#         b = []
#         b.append(a)
#         print(b)
# my_method(0)
# my_method(1)
# my_method(2)
#


# 不定长参数
# 单星号 * 没有名称的不定长参数.后面的参数是以列表形式存在
# 双星号 ** 带有别名的不定长参数.函数调用时参数需要添加名称，存储方式为字典
# def my_method(name,sex,age=9,*args):
#     print(name,sex,age)
#     print(args)
# my_method('张三','男',8,'三年级','秦皇岛')
#
# def my_method(name,sex,age=9,**kwargs):
#     print(name,sex,age)
#     print(kwargs)
# my_method('张三','男',8,classes='三年级',address='秦皇岛')

# 写一个函数，如果给的参数是字符串、列表、元组的长度是否大于5
# def is_more_than_five(a):
#     if isinstance(a,list) or isinstance(a,tuple) or isinstance(a,str):
#         if len(a) >5:
#             return True
#         else:
#             return False
#     else:
#         print('传参错误')
#         return None
#
# def count_str(a):
#     if isinstance(a, str):
#         dic = {}
#         count_alpha = 0
#         count_num = 0
#         count_space = 0
#         count_other = 0
#         # for i in a:
#         #     if i not in list1:
#         #         list1.append(i)
#         # print(list1)
#         for i in a:
#             if i.isalpha():
#                 count_alpha += 1
#             elif i.isdigit():
#                 count_num += 1
#             elif i.isspace():
#                 count_space += 1
#             else:
#                 count_other += 1
#         dic['字母'] = count_alpha
#         dic['数字'] = count_num
#         dic['空格'] = count_space
#         dic['其它'] = count_other
#         return dic
#     else:
#         print('请输入正确字符串')
#         return None
#
# def return_get(hostname,path=None,data=None):
#     url = 'http://{host}/'.format(host=hostname)
#
#     if path:
#         url += path
#     if data:
#         list1 = []
#         for key, value in data.items():
#             str1 = '{key}={value}'.format(key=key, value=value)
#             list1.append(str1)
#         url = url + '?' + '&'.join(list1)
#
#     return url
#
# url = return_get('www.cnblogs.com',path='psztswcbyy/p/9258579.html')
# print(url)


# 高阶函数：函数是可以嵌套，函数的参数是函数
# 一行代码实现按照字符串长度倒序排序
list1 = ['fue','df','feoi','fieow','uuu','fdojoahjf']

print(sorted(list1, key=len, reverse=True))


