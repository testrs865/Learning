ch = input()
ch_len = len(ch)

for i in range(ch_len):
    if ch[i].islower():
        print(ch[i].upper(), end="")
    elif ch[i].isupper():
        print(ch[i].lower(), end="")
    else:
        print(ch[i], end="")
    
    if i == ch_len - 1:
        print()

#print(ch.swapcase())