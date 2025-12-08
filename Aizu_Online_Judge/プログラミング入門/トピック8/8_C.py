ALPHABET_NUM = 26
counter = [0 for i in range(ALPHABET_NUM)]

while True:
    try:
        str = input()
    except EOFError:
        break

    for ch in str.lower():
        num = ord(ch) - ord("a")
        for i in range(26):
            if i == num:
                counter[i] += 1

for i in range(26):            #a ~ zの値は97 ~ 97+25+1
    print(f"{chr(i + 97)} : {counter[i]}")