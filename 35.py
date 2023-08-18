"""
描述

蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
例如，当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11


输入描述：

输入正整数N（N不大于100）
输出描述：

输出一个N行的蛇形矩阵。
"""

n=int(input())
first=1
for i in range(n):
    result=[]
    first+=i
    answer=first
    for j in range(n-i):
        result.append(str(answer))
        answer+=j+i+2
    print(' '.join(result))
    

    