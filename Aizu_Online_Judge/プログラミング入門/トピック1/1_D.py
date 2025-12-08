S = input()
h = int(int(S) / 3600)
m = int(int(S) / 60 % 60)
s = int(int(S) % 60)
print(f"{h}:{m}:{s}")       #print(h,":",m,":",s)だと空白が入る