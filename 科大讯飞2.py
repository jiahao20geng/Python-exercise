# 定义系数和常数
A = [[3, 1], [1, 2]]
b = [9, 8]

n = len(A)
# 进行高斯消元
for i in range(n):
    max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
    print(max_row)
    A[i], A[max_row] = A[max_row], A[i]
    b[i], b[max_row] = b[max_row], b[i]
    
    # 将主对角线上的元素变为1
    for j in range(i + 1, n):
        factor = A[j][i] / A[i][i]
        b[j] -= factor * b[i]
        for k in range(i, n):
            A[j][k] -= factor * A[i][k]

# 求解解向量
x = [0] * n
for i in range(n - 1, -1, -1):
    x[i] = b[i] / A[i][i]
    for k in range(i - 1, -1, -1):
        b[k] -= A[k][i] * x[i]

print(x)  # 输出结果 [2.0, 3.0]
