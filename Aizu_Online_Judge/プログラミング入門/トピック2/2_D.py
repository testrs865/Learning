s = input()
W, H, x, y, r = map(int, s.split())

if x - r < 0 or y - r < 0 or x + r > W or y + r > H:
    print("No")
else:
    print("Yes")