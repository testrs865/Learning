n = int(input())
cards = [[False for i in range(13)] for j in range(4)]
pattern = ["S", "H", "C", "D"]

for i in range(n):
    a, b = input().split()
    ch = a
    rank = int(b)
    cards[pattern.index(ch)][rank - 1] = True

for i in range(4):
    for j in range(13):
        if cards[i][j] == False:
            print(pattern[i], j + 1)