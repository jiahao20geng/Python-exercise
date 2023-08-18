#输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。保证输入的整数最后一位不是0
n=input()
result=[]
for i in range(len(n)):
    if n[len(n)-i-1] not in result:
        result.append(n[len(n)-i-1])
print("".join(str(i)for i in result))
