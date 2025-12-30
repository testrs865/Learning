n = int(input())
r = []

for i in range(n):
    m = int(input())
    r.append(m)

min_value = r[0]
max_profit = -10 ** 9

for i in range(1, n):
    max_profit = max(max_profit, r[i] - min_value)
    min_value = min(min_value, r[i])

print(max_profit)