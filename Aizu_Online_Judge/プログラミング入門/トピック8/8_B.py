while True:
    ch = input()
    sum = 0

    if int(ch) == 0:
        break

    for i in ch:
        sum += int(i)
    
    print(sum)