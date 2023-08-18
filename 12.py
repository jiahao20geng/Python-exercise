#接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）
n=input()
result=[]
for i in range(len(n)):
    result.append(n[len(n)-1-i])
print("".join(str(i)for i in result))