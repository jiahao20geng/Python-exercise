#•输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；
#•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
#输入：连续输入字符串(每个字符串长度小于等于100)


#输出：依次输出所有分割后的长度为8的新字符串
a=input()
N=len(a)
n=int(N/8)
for i in range(n):
    b=i*8
    print(a[b:b+8])
residual=N%8
zero="0"*(8-residual)
last=a[-residual:]
if residual!=0:
    print("".join([last,zero]))
