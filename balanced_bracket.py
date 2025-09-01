def balanced_bracket(str):
    opening_bracket = "{[("
    closed_bracket = "}])"
    matchingbrackets = {"}":"{","]":"[",")":"("}
    stack = []
    for char in str:
        if char in opening_bracket:
            stack.append(char)
        elif char in closed_bracket:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingbrackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

if __name__ == "__main__":
    string = "()[]{}"
    result = balanced_bracket(string)
    if result == False:
        print("Unbalaced brackets")
    else:
        print("balanced_bracket")
