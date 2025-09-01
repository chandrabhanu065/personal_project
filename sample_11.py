#ip = "aaabbc"
#op = "a3b2c1"

def convert_string(string):
    result = ""
    count = 1
    for x in range(1, len(string)+1):
        if x < len(string) and string[x] == string[x-1]:
            count += 1
        else:
            result += string[x-1] + str(count)
            count = 1
    return result

if __name__ == '__main__':
    string = 'aaabbc'
    result = convert_string(string)
    print("Encoded string is {}".format(result))