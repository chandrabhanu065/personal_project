x = 10
def func():
    x = 3 + 3
    print("Inside function {}".format(x))

x = func()

print("outside function {}".format(x))