import math

a, b, C = map(float, input().split())

area = a * b * math.sin(math.radians(C)) / 2
c1 = a**2 + b**2 - 2 * a * b * math.cos(math.radians(C))
c2 = math.sqrt(c1)
L = a + b + c2
h = area * 2 / a

print(area)
print(L)
print(h)