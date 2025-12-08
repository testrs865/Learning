r, c = map(int, input().split())
table = [[0 for i in range(101)] for j in range(101)]
row = []

for i in range(r):
    row.extend( list(map(int, input().split())))
    row.append(0)
    table[i] = row
    row = []

for i in range(r + 1):
    for j in range(c):
        print(table[i][j], end=" ")
        table[i][c] += table[i][j]      
        table[r][j] += table[i][j]      #最後尾r行目にj列目の足し合わせたものを代入
    print(table[i][c])