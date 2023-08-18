#功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
#只需要考虑2和奇数因子
#当检查到超过n的平方根时，就可以结束循环了，因为剩下的因子一定是大于n的平方根的，而它们的对应的另一个因子一定小于n的平方根
import numpy as np
n=int(input())
result=[]
while n%2==0:
    result.append(2)
    n=int(n/2)
i=3
while i<=np.sqrt(n):
    print(i)
    if n%i==0:
        result.append(i)
        n=int(n/i)
    else:
        i=i+2
if n>2:
    result.append(n)
print(" ".join(str(i) for i in result))