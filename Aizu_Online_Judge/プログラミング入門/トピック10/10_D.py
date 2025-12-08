import math

def minko(p, n, x, y):
    x_y_sum = 0
    x_y_sets = []
    for i in range(n):
        x_y_sum += abs((x[i] - y[i]))**p
        x_y_sets.append(abs(x[i] - y[i]))

    if p < 4:
        return x_y_sum**(1 / p)
    else:
        return max(x_y_sets)

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

print(minko(1, n, x, y))
print(minko(2, n, x, y))
print(minko(3, n, x, y))
print(minko(100, n, x, y))