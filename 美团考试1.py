import sys
num=int(sys.stdin.readline())
a=sys.stdin.readline().split()
b=sys.stdin.readline().split()

way1=0
way2=0
sum=0
for i in range(len(a)):
    sum+=int(a[i])
if int(b[0])<int(b[1]):
    min=int(b[0])
    max=int(b[1])
else:
    min=int(b[1])
    max=int(b[0])
for i in range(min,max):
    way1+=int(a[i-1])

way2=sum-way1

print(min(way1,way2))

