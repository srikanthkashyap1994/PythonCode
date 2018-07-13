prime_list = list()
for i in range(0,101):
    if (i == 1):
        continue
    elif (i == 2):
        prime_list.append(i)
        continue
    else:
        for j in range(2,i):
            if (i%j == 0):
                break
            else:
                continue

i = 1
while (i < 101):
    if (i == 1):
        continue
    elif (i == 2):
        prime_list.append(i)
        continue
    else:
        j = 2
        while (j < i):
            if (i%j == 0):
                i = i + 1
                break
            else:
                j = j + 1
                continue
