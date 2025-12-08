W = input()
count = 0

while True:
    T = input().split()

    if T[0] == "END_OF_TEXT":
        break

    T_len = len(T)

    for i in range(T_len):
        if T[i].lower() == W.lower():
            count += 1

print(count)