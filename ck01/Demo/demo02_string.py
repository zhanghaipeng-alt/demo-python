'''
拼接一个方法请求字符串
'''
# function_name = 'test_case01'
# case_name = '测试用例1'
# par_name = 'id=1'
# str1 = '''def {function_name}(self):
#     'case_name'
#     execute_case('par_name')
# '''.format(function_name=function_name, case_name=case_name, par_name=par_name)
#
# print(str1)

# 字符串的判断类型，所有字符串判断方法 都是以is开头的
# str1 = 'JIODJF384687OAodjfoajeonf'
# str2 = 'jfiashjfe9zhang子胡覅地方'
# str3 = 'FEJONAFOIDAOIF'
# str4 = 'fhjdianeinfw'
# str5 = 'Rdfaojenfidjfe'
# str6 = '86348264'
# print(str3.isupper())
# print(str4.islower())
# print(str5.istitle())
# print(str2.isalpha())
# print(str6.isdigit())
# print(str1.isalnum())

# 开头或结尾判断
a = 'jfeqmflemfo'
print(a.startswith('jf'))
print(a.endswith('kk'))

# 去掉字符串空格
# lstrip()去掉左边空格  rstrip()去掉后边空格  strip()去掉前后空格
b = ' adm in  '
print(b.lstrip())
print(b.rstrip())
print(b.strip())

# 字符串的查找，find(）和index()

# replace()替换

c = ' aaa hello world ppppapp'
print(c.replace(' ',','))

# 统计字符串出现的次数
print(c.count('a',0,5))