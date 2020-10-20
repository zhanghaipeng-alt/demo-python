# 元组：值不能改变。
# 定义方式 a = (1,2,3)
# t = (2, 5, 6, 2, 8, 0, 54, 32, 'a', 8.9, '中国')
# # 分片
# print(t[2:12:1])
#
# # 倒序
# print(t[::-1])
#
# # 索引
# print(t.index('中国'))
#
# # 计数 元素出现的次数
# print(t.count(2))

data = ((1,'张三',4500.00),(2,'李四',7800.00),(3,'小黑',3599.00))
#循环打印所有员工信息
# for i in data:
#     for j in i:
#         print(j)

# 打印每个员工的工资
# count = 0
# for i in data:
#     count += i[-1]
# print(f'平均工资是{(count/len(data)):.2f}')

# 打印工资最高工资及员工姓名

data1 = (('技术部',(367,500,45)),
         ('人力资源部',(247,368,1280)),
         ('财务部',(87,100,24,50)))
# 统计出费用总额
# count = 0
# for a in data1:
#     for b in a[-1]:
#         count += b
# print(f'本月总的打车费用为 ￥{count}')

# count = 0
# for a in data1:
#     count += sum(a[-1])
# print(f'本月总的打车费用为 ￥{count}')

# 统计加班最少的部门
# total = 100000
# index = 0
# for x,y in enumerate(data1):
#     if sum(y[-1]) < total:
#         total = sum(y[-1])
#         index = x
# print(data1[index][0])


# B中元素落入A中区间的次数
# A = ((5,7),(18,20),(35,37),(56,58),(3,89),(1,87))
# # B = (6,15,47,57,86)
# #
# # count = 0
# # for i in A:
# #     for j in B:
# #         if j >= i[0] and j <= i[-1]:
# #             count +=1
# # print(count)


# 列表
# 列表的常用方法
# append extend
# list1 = ['fdop','合法你激活',[8.7,5]]
# list2 = [3,7,'fopd']
# list1.append(['fa',34])
# print(id(list2))
# list2.append(9)
# print(list2)
# print(id(list2))
#
# list2.extend([0])
# print(list2,id(list2))

# insert:在固定位置插入,第一个参数是索引位置
# list1 = [7,9,'for ',6,9,10]
# list1.insert(2,'pop')
# print(list1)

# pop函数，弹出list中的某些元素，不写参数则默认从最后一位
# list1 = [1,2,3,4,5,6,7]
# print(list1,id(list1))
#
# list1.pop()
# print(list1,id(list1))
#
# a = list1.pop(3)
# print(list1,id(list1))
# print(a)

# remove 删除：是按内容删除的。
# list1 = ['a','b','c','d','e','f']
# # print(list1,id(list1))
# # list1.remove('b')
# # print(list1,id(list1))
#
# for i in list1:
#     list1.remove(i)
# print(list1, id(list1)) #会报错，越界了，list不能一边循环一边删除操作 python3不会,
#
# #可以从后往前循环
# list2 = ['a', 'b', 'c', 'd', 'e', 'f']
# print(list2, id(list2))
# for i in list2[::-1]:
#     list2.remove(i)
# print(list2, id(list2))

#reverse：列表的翻转，相当于执行[::-1]，是没返回值的


#sort排序函数和系统函数sorted reverse=True 默认为false  true是倒序排列
# list1 = [3,2,7,9,2,5,8,0]
# # list1.sort(reverse=True)
# #
# # print(list1, id(list1))
#
# #系统内置的排序函数，带有返回值
# list2 = sorted(list1,reverse=True)
# print(list1,id(list1))
# print(list2,id(list2))


#列表去重
list1 = [3,4,8,1,2,3,4,6,8,2,5,4]





# 经典方法
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

# set方法
# list2 = set(list1)
# print(list2)

# 利用字典功能：先将list转成空字典，然后在转成list
list3 = list((dict.fromkeys(list1)).keys())
print(list3)







