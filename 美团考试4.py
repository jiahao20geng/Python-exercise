import sys
import math
n=int(sys.stdin.readline())
a=sys.stdin.readline().split()

result=0
aa=[0 for _ in range(len(a))]
#print(aa)
for i in range(n-1):
    line=sys.stdin.readline().split()
    #print(a[int(line[0])-1])
    #print(a[int(line[1])-1])
    sqrt=math.sqrt((int(a[int(line[0])-1]))*(int(a[int(line[1])-1])))
    if int(sqrt)==sqrt and aa[int(line[0])-1]==0 and aa[int(line[1])-1]==0:
        result+=2
        aa[int(line[0])-1]=1
        aa[int(line[1])-1]=1
    
print(result)