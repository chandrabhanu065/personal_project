str_1 = 'chandra'
str_2 = []
for i in range(1, len(str_1) + 1):
    str_2 += str_1[len(str_1) - i]

print(''.join(str_2))