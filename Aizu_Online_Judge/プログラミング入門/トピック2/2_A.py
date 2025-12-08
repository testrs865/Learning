s = input()
a, b = map(int, s.split())

if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("a == b")