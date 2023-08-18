import sys
n=sys.stdin.readline().split()
a0=int(n[0])


for i in range(len(n)):
    if int(n[i])==n[0]:
        flag1=1
    else:
        flag1=0
        break

for i in range(1,len(n)-1):
    if int(n[i+1])//int(n[i])==int(n[1])//int(n[0]):
        flag2=1
    else:
        flag2=0
        break

for i in range(2,len(n)):
    if int(n[2])//int(n[0])==int(n[i])//int(n[i-2]):
        flag3=1
    else:
        flag3=0
        break

for i in range(2,len(n)-1):
    if int(n[i])//(int(n[i-1])*int(n[i-2]))==int(n[2])//(int(n[1])*int(n[0])):
        flag4=1
    else:
        flag4=0
        break

if flag1:
    #print("flag1")
    print(a0)
elif flag2:
    #print("flag2")
    print(int(n[-1])*(int(n[-1])//int(n[-2])))
elif flag3:
    #print("flag3")
    print(int(n[2])//int(n[0])*int(n[-2]))
elif flag4:
    print(int(n[2])//(int(n[1])*int(n[0]))*(int(n[-1])*int(n[-2])))
else:
    print("wrong")
