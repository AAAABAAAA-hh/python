# 生成一个二维数组 m * n
m,n = map(int,input().split())
dp = [[0] * n for _ in range(m)]

def build_arr(m,n):
    list_binary = [[0] * m for _ in range(n)]
