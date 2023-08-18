#输入n个整数，找出其中最小的k个整数并按升序输出
a=input()
b=input()
a1=a.split()
b1=b.split()
k=int(a1[1])
b1=list(map(int,b1))#将列表中的str转换为int
b1.sort()
print(" ".join(str(i)for i in b1[:k]))