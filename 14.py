#给定 n 个字符串，请对 n 个字符串按照字典序排列。
n=int(input())
result=[]
for i in range(n):
    word=input()
    result.append(word)
result.sort()#这就已经给result排序了
for i in range(n):
    print(result[i])