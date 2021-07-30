def generate_errors(problems):
    # More than 5 problems return: 'Error: Too many problems.'
    if len(problems) > 5:
        return "Error: Too many problems."

    fullOp = []

    for x in problems:
        y = x.split()
        fullOp.append(y)

    # # Testing if only +- operations and if only numbers are passed as args
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


def arithmetic_arranger(problems, bool=False):

    # Checking for errors
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
        maxSize.append(0)

    maxSize.pop()

    first = []
    second = []
    third = []
    fourth = []
    i = 0
    j = 0

    for x in maxSize:
        if maxSize[i] == 0:
            first.append("    ")
            second.append("    ")
            third.append("    ")
            fourth.append("    ")
        else:
            first.append(" " * (maxSize[i] - len(fullOp[j][0])))
            first.append(fullOp[j][0])
            second.append(fullOp[j][1])
            second.append(" ")
            second.append(" " * (maxSize[i] - len(fullOp[j][2]) - 2))
            second.append(fullOp[j][2])
            third.append(maxSize[i] * "-")
            if fullOp[j][1] == "+":
                ans = int(fullOp[j][0]) + int(fullOp[j][2])
            else:
                ans = int(fullOp[j][0]) - int(fullOp[j][2])
            ans = str(ans)
            fourth.append(" " * (maxSize[i] - len(ans)))
            fourth.append(ans)
            j += 1
        i += 1

    first = "".join(first)
    second = "".join(second)
    third = "".join(third)
    fourth = "".join(fourth)

    result = first + "\n" + second + "\n" + third
    if bool:
        result = result + "\n" + fourth

    return result
