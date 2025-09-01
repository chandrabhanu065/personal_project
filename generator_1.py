def count_up_to(num):
    count = 0
    while count <= num:
        if count%2 == 1:
            yield count
        count += 1

number = 10
for numb in count_up_to(number):
    print(numb)