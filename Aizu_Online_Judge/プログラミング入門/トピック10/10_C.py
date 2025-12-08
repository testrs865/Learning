import math

while True:
    n = int(input())

    if n == 0:
        break

    sn = []
    sn.extend(map(float, input().split()))
    avg = float(sum(sn)) / float(len(sn))
    var1 = 0
    
    for i in range(n):
        var1 += (sn[i] - avg)**2

    var2 = var1 / n
    a = math.sqrt(var2)
    print(a)