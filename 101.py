#输入整型数组和排序标识，对其元素按照升序或降序进行排序
n=int(input())
num=input().split()
order=int(input())
result=[]
num=list(map(int,num))
if order==0:
    num.sort()
else:
    num.sort(reverse=True)
print(" ".join(str(i)for i in num))
    