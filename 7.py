#写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于 0.5 ,向上取整；小于 0.5 ，则向下取整。
n=float(input())
# if n-int(n)<0.5:
#     print(int(n))
# else:
#     print(int(n)+1)
print(int(n+0.5))