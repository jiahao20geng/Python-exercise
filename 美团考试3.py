import sys

dimension=sys.stdin.readline().split()
n=int(dimension[0])
m=int(dimension[1])
matrix=[[0]*m for _ in range(n)]
sum=0
for i in range(n):
    line=sys.stdin.readline().split()
    for j in range(len(line)):
        matrix[i][j]=int(line[j])
        sum+=matrix[i][j]
        
min_difference=sum
for i in range(n-1):
    s1=0
    #print("i is ",i)
    for j in range(i+1):
        #print("j is ",j)
        row_sum=0
        for k in range(m):
            row_sum+=matrix[j][k]
            #print(matrix[j][k])
        s1+=row_sum
    s2=sum-s1
    difference=abs(s2-s1)
    if difference<min_difference:
        min_difference=difference
#print(min_difference)

for i in range(m-1):
    #print("i is ",i)
    s1=0
    for j in range(i+1):
        row_sum=0
        #print("j is ",j)
        for k in range(n):
            #print("k is ",k)
            row_sum+=matrix[k][j]
            #print(row_sum)
            #print(matrix[k][j])
        s1+=row_sum
    #print("s1 is ",s1)
    s2=sum-s1
    difference=abs(s2-s1)
    if difference<min_difference:
        min_difference=difference
print(min_difference)


