n = int(input())
count = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for i in range(n):
    b, f, r, v = map(int, input().split())
    count[b - 1][f - 1][r - 1] += v

for i, buildings in enumerate(count):
    for floors in buildings:
        for rooms in floors:
            print(f" {rooms}", end="")
        print()
    if i != 3:
        print("####################")