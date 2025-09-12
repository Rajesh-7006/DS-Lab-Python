def precedence(op):
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    if op == "^":
        return 3
    return 0

def is_operand(ch):
    return ch.isalnum()

def infix_to_postfix(expression):
    stack = []
    result = ""
    for char in expression:
        if is_operand(char):
            result += char
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                result += stack.pop()
            stack.append(char)
    
    while stack:
        result += stack.pop()

    return result

if __name__ == "__main__":
    infix_exp = input("Enter Infix Expression: ")
    print("Postfix Expression:", infix_to_postfix(infix_exp))
