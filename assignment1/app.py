
'''
    This is Assignment 1
'''

def check(mystr):
    '''
        Here is the function definition to check valid expression
    '''
    mystack = []    # empty list for keeping the starting backets
    for y in mystr:
        if y in ['(','{','[']:  # appending the starting bracket in list
            mystack.append(y)
        else:                  # will remove the starting bracket from list if it exists
            if y == ')' and '(' in mystack:
                mystack.remove('(')
            else:
                if y == '}' and '{' in mystack:
                    mystack.remove('{')
                else:
                    if y == ']' and '[' in mystack:
                        mystack.remove('[')
                    else:
                        return False      # returning False as none of the closing brackets matches
            
    if len(mystack)==0:  # checking the mystr list lenght for any pending bracket which is not closed
        return True
    return False