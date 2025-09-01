
dict_1 = {"odd":[2,4,6,8],"even":[1,3,5,7]}
#output =
def func(a = 10, *args):
    addition = a
    addition += sum(args)
    return addition

#def
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    #result1 = func()
    result2 = func(func(),*arr)
    print(result2)