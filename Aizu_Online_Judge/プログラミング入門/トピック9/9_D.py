str_list = list(input())
str_cpy = str_list[:]
q = int(input())

for i in range(q):
    all_sets = input().split()
    command = all_sets[0]
    a = int(all_sets[1])
    b = int(all_sets[2])
    
    if command == "replace":
        command_replace = all_sets[3]
        command_replace = list(command_replace)
        for i in range(a, b+1):
            str_list[i] = command_replace[i-a]
    elif command == "reverse":
        for i in range(a, b+1):
            str_list[i] = str_cpy[b+a-i]         #str[b] = str_cpy[a], atr[a] = str_cpy[b]
    else:
        print("".join(map(str, str_list[a:b+1])))

    str_cpy = str_list[:]