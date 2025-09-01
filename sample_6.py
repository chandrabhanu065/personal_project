lst = ['abc','bbc','ccd']
#oput = [{a:1, b:1, c:1},{b:2, c:1},{c:2,d:1}]

def func(lst):
    output = []
    for str in lst:
        frq = {}
        for char in str:
            #frq[char] = (frq.get(char, 0) + 1)
            if char in frq:
                frq[char] += 1
            else:
                frq[char] = 1
        output.append(frq)
    return output

if __name__ == "__main__":
    result = func(lst)
    print("frequecy of strings is {}".format(result))