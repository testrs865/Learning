n = int(input())
#test_array = []

for i  in range(1, n + 1):
    if i % 3 == 0:
        print(f" {i}", end="")
        #test_array.append(i)
    elif i % 10 == 3:
        print(f" {i}", end="")
        #test_array.append(i)
    else:
        j = i
        while True:
            j = int(j / 10)
            
            if j < 1:
                break

            if j % 10 == 3:
                print(f" {i}", end="")
                #test_array.append(i)
                break

print()
#print(len(test_array))