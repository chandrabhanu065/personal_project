def reverse_words_in_string(string):
    words = []
    startofword = 0
    for idx in range(len(string)):
        char = string[idx]
        if char == " ":
            words.append(string[startofword:idx])
            startofword = idx
        else:
            if string[startofword] == " ":
                words.append(" ")
                startofword = idx
    words.append(string[startofword:])
    reverseList(words)
    return "".join(words)

def reverseList(string):
    start, end = 0, len(string) -1
    while start < end:
       string[start], string[end] = string[end], string[start]
       start += 1
       end -= 1

if __name__ == "__main__":
    string = "My name is chandra bhanu"
    result = reverse_words_in_string(string)
    print(result)


