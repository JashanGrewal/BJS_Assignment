def getEquationValue(expression_string, pair):
    """
    :param expression_string: expression based on which to calculate value
    :param pair: tuple of x and y values
    :return: final result of expression after complete evaluation
    """
    expressions = list(expression_string)
    result = 0
    index = 0
    dictionary = {'x': pair[0], 'y': pair[1]}

    stack = []
    while index < len(expressions):
        if (expressions[index] in ['+', '-', '*', '/']):
            stack.append(expressions[index])
            index += 1
        else:
            result = getValue(expressions, index, stack.pop(), dictionary, result)
            index += 2
    return result


def getValue(expressions, index, operation, dictionary, result):
    """
    :param expressions: list of all the elements in expression string
    :param index: index of element from expression if it does not lies in "+-*/"
    :param operation: +,-,*,/
    :param dictionary: key-value pair of x and y
    :param result: last evaluated value
    :return: value after each evaluation
    """
    operand1 = expressions[index]
    if (index == len(expressions) - 1):
        operand2 = result
    else:
        operand2 = expressions[index + 1]

    if not isinstance(operand1, int) and not operand1.isnumeric():
        operand1 = dictionary[operand1]

    if not isinstance(operand2, int) and not operand2.isnumeric():
        operand2 = dictionary[operand2]

    if (operation == '+'):
        return int(operand1) + int(operand2)
    elif operation == '*':
        return int(operand1) * int(operand2)
    elif operation == '-':
        return int(operand1) - int(operand2)
    elif operation == '/':
        return int(operand1) / int(operand2)
    else:
        return -1

def get_max_evaluated_value(variables,expression_string):
    """
    :param variables: range of x and y values
    :param expression_string: expression to be evaluated
    :return: max_value evaluated from a range of x and y values
    """
    x_range = range(variables['x'][0], variables['x'][1] + 1)
    y_range = range(variables['y'][0], variables['y'][1] + 1)
    x_y_pair_list = []
    result_list = []
    for i in x_range:
        for j in y_range:
            x_y_pair_list.append((i,j))
    for pair in x_y_pair_list:
        res = getEquationValue(expression_string, pair)
        result_list.append(res)
    return max(result_list)


Variables = {"x": (0, 2), "y": (2, 4)}
expression_string = "*+2xy"
print(get_max_evaluated_value(Variables, expression_string))
