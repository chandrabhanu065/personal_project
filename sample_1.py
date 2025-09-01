import re

def is_alphabet(string):
    regex_pattern = re.compile(r'[a-zA-Z]')
    result = re.findall(regex_pattern,string)
    if result:
        print("Match found")
    else:
        print("No Match found")

if __name__ == "__main__":
    input = input("Enter value :")
    res = is_alphabet(input)


