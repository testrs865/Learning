n = int(input())
prime_sum = 0

for i in range(n):
    m = int(input())
    if m < 2:
        continue
    elif m == 2:
        prime_sum += 1
        continue
    
    if m % 2 == 0:
        continue
    j = 3
    while j * j <= m:
        if m % j == 0:
            break
        j += 2
    prime_sum += 1
    
print(prime_sum)