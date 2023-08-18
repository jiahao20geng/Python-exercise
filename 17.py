#开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
x=0
y=0
word=input().split(";")
for i in word:
    if len(i)<=3 & len(i)>=2:
        if i[0]=="A":
            try:
                num=int(i[1:3])
            except ValueError:
                num=0
                continue
            x-=num
        
        if i[0]=="W":
            
            try:
                num=int(i[1:3])
            except ValueError:
                num=0
                continue
            y+=num
        
        if i[0]=="S":
            try:
                num=int(i[1:3])
            except ValueError:
                num=0
                continue
            y-=num
        
        if i[0]=="D":
            try:
                num=int(i[1:3])
            except ValueError:
                num=0
                continue
            x+=num
result=list((x,y))
print(",".join(str(i)for i in result))
            
            
        