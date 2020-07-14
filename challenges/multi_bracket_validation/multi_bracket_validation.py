def multi_bracket_validation(input):
    stack = []
    if not input:
        return False
    for i in input:
        if i == '(':
            stack.append(')')
        elif i == '{':
            stack.append('}')
        elif i == '[':
            stack.append(']')
        elif not stack:
            return False
        elif i == ')' or i == '}' or i == ']':
            if not stack or stack.pop() != i:
                return False
    if stack:
        return False            
    else:
        return True

print(multi_bracket_validation('(mm'))