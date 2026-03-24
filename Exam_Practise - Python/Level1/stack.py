
def stack(fjala:str):
    open=["(","{","["]

    closed=[")","}","]"]     
    stack=[]                                      
    #      ({[])}stack ( { [  

    for c in word:
        if c in open:
            stack.append(c)
        else:
            if c in closed:
                index=closed.index(c)
                if open.index(stack[len(stack)-1]) == index:                   
                    stack.pop()

    if len(stack) != 0:
        return False
    
    return True


print(stack("({[]})"))   # True
print(stack("({[])}"))   # False
print(stack("("))        # False
print(stack("()[]{}"))   # True
