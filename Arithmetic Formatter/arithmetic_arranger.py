'''
If the user supplied the correct format of problems, the conversion you return will follow these rules:
    There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
    Numbers should be right-aligned.
    There should be four spaces between each problem.
    There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
    
    ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"] , True

    '''


def generate_errors(problems):
    # If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
    if len(problems) > 5:                       
        return "Error: Too many problems."      

    fullOp = []

    for x in problems:
        y = x.split()
        fullOp.append(y)

    # # Testing if only + or - operations and if only numbers are passed as args
    for x in fullOp:                            
        if not x[1] == "+" and not x[1] == "-":
            return "Error: Operator must be \'+\' or \'-\'."
        try:
            x[0] = int(x[0])
            x[2] = int(x[2])
        except:
            return "Error: Numbers must only contain digits."
        
        if x[0] > 9999 or x[2] > 9999:
            return "Error: Numbers cannot be more than four digits."

    return False



def arithmetic_arranger(problems, bool = False):

    if generate_errors(problems):
        return generate_errors(problems)

    fullOp = []
    maxSize = []

    for x in problems:
        y = x.split()
        fullOp.append(y)

    for x in fullOp:
        y = max(len(x[0]), len(x[2]))
        maxSize.append(y + 2)

        

    result = maxSize
    return print(result)

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))