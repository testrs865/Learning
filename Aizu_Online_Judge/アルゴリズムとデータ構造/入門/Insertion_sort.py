n = int(input())

array = list(map(int, input().split()))

for i in range(n):
    v = array[i]
    j = i - 1
    while j >= 0 and array[j] > v:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = v

    for k in range(n):
        print(f"{array[k]}", end="")
        if k != n - 1:
            print(end=" ")
    print("")