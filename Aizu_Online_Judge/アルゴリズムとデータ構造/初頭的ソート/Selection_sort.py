n = int(input())
a = list(map(int, input().split()))
change_counts = 0
change_flag = 0

for i in range(n):
    minj = i
    for j in range(i, n):
        if a[j] < a[minj]:
            change_flag = 1
            minj = j
            
    a[i], a[minj] = a[minj], a[i]
    if change_flag:
        change_counts += 1
        change_flag = 0

for i in range(n):
    print(f"{a[i]}", end="")
    if i != n - 1:
        print(" ", end="")

print("")
print(change_counts)