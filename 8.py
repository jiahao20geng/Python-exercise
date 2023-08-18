#数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。
n=int(input())
dic={}
for i in range(n):
    list=input().split()
    if int(list[0]) not in dic.keys():
        dic[int(list[0])]=int(list[1])
    else:
        dic[int(list[0])]+=int(list[1])
#print(dic)
dic = dict(sorted(dic.items()))
for i in dic.keys():
    print(i,dic[i])
