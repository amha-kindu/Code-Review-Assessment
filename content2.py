def is_valid_parenthesis(string):
    brackets = {
        '(': ')',
          "{": "}",
         '[': ']'
    }

    stack = []
    for char in string:
        if char in brackets: 
            stack.append(char)

        else:
            if len(stack) == 0:
                return False
            
            opening = stack.pop()
            if brackets[opening] != char:
                return False
    
    return len(stack) == 0