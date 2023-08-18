"""
描述

输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。
数据范围：输入的字符串长度满足 
1
≤
n
≤
1000
 
1≤n≤1000 
输入描述：

输入一行字符串，可以有空格
输出描述：

统计其中英文字符，空格字符，数字字符，其他字符的个数
"""

n=input()
alpha=0
digit=0
space=0
other=0
for i in n:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        space+=1
    else:
        other+=1
print(alpha)
print(space)
print(digit)
print(other)