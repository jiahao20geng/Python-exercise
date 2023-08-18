"""
描述

实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。

数据范围：输入的字符串长度满足 
1
≤
n
≤
20
 
1≤n≤20  ，保证输入的字符串中仅出现小写字母
输入描述：

字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。
输出描述：

删除字符串中出现次数最少的字符后的字符串。

"""

n=input()
num={}
for i in n:
    num[i]=n.count(i)
a=min(list(num.values()))
letter=[]
for i,j in num.items():
    if j==a:
        letter.append(i)
for i in letter:
    n=n.replace(i,"")
print(n)
