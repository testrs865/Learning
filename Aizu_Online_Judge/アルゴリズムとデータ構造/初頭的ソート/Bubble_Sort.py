n = int(input())
a = list(map(int, input().split()))
change_counts = 0

for j in range(n):
    for i in range(n - 1, j, -1):
        if a[i] < a[i - 1]:
            a[i], a[i - 1] = a[i - 1], a[i]
            change_counts += 1

for i in range(n):
    print(f"{a[i]}", end="")
    if i != n - 1:
        print(" ", end="")

print("")
print(change_counts)