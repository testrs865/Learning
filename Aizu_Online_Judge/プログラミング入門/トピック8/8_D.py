s = input()
p = input()

s += s

if p in s:                  #s.find(p) != -1でも可
    print("Yes")
else:
    print("No")