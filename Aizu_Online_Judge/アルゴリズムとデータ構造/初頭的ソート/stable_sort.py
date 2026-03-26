def Bubble_sort(c, n):
    c = c.copy()
    for j in range(n):
        for i in range(n - 1, j, -1):
            if int(c[i][1:]) < int(c[i - 1][1:]):
                c[i], c[i - 1] = c[i - 1], c[i]
    return c

def Selection_sort(c, n):
    c = c.copy()
    for i in range(n):
        minj = i
        for j in range(i, n):
            if int(c[j][1:]) < int(c[minj][1:]):
                minj = j
        c[i], c[minj] = c[minj], c[i]
    return c

n = int(input())
a = list(input().split())
a1 = Bubble_sort(a, n)
a2 = Selection_sort(a,n)

for i in range(n):
    print(f"{a1[i]}", end="")
    if i != n - 1:
        print(" ", end="")
print("")
print("Stable")

stable_flag = 0
for i in range(n):
    print(f"{a2[i]}", end="")
    if a1[i] != a2[i]:
        stable_flag = 1
    
    if i != n - 1:
        print(" ", end="")

print("")
if stable_flag:
    print("Not stable")
else:
    print("Stable")