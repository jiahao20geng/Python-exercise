#计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
#输入：输入一行，代表要计算的字符串，非空，长度小于5000
import sys
for line in sys.stdin:#为终端输入的内容
    a=line.split()
    print(len(a[-1]))
#输出：输出一个整数，表示输入字符串最后一个单词的长度。