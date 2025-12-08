n, m, l = map(int, input().split())
c = [[[] for i in range(l)] for j in range(n)]
c_sum = 0
a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(m):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(l):
        for k in range(m):
            c_sum += a[i][k] * b[k][j]
        c[i][j] = c_sum
        c_sum = 0
        print(c[i][j], end="")
        if j != l - 1:
            print(end=" ")
    print()