n, m = map(int, input().split())
matrix = [[0 for i in range(m)] for j in range(n)]
vector =[]
c = []
c_sum = 0

for i in range(n):
    matrix[i] = list(map(int, input().split()))

for i in range(m):
    vector.append(int(input()))

for i in range(n):
    for j in range(m):
        c_sum += matrix[i][j] * vector[j]
    c.append(c_sum)
    print(c[i])
    c_sum = 0