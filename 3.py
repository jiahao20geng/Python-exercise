import numpy as np
#明明生成了N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。
#输入：第一行先输入随机整数的个数 N 。 接下来的 N 行每行输入一个整数，代表生成的随机数。

#输出：输出多行，表示输入数据处理后的结果

N=int(input())
a=[]
for i in range(N):
    b=int(input())
    a.append(b)
a=list(set(a))
a.sort#(reverse=True)#默认从小到大排序，加reverse则为从大到小排序
for i in a:
    print(i)
