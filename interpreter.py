# interpreter.py
variables = {}

def interpret(ast):
    for statement in ast:
        if statement[0] == 'SET':
            var_name = statement[1]
            value = evaluate_expression(statement[2])
            variables[var_name] = value
        elif statement[0] == 'PRINT':
            var_name = statement[1]
            if var_name in variables:
                print(variables[var_name])
            else:
                raise NameError(f"Variable '{var_name}' is not defined")
        elif statement[0] == 'IF':
            condition = evaluate_expression(statement[1])
            if condition:
                interpret(statement[2])
            else:
                interpret(statement[3])

def evaluate_expression(expression):
    if expression[0][0] == 'NUMBER':
        result = int(expression[0][1])
    elif expression[0][0] == 'ID':
        if expression[0][1] in variables:
            result = variables[expression[0][1]]
        else:
            raise NameError(f"Variable '{expression[0][1]}' is not defined")
    i = 1
    while i < len(expression):
        operator = expression[i][1]
        operand = expression[i + 1]
        operand_value = int(operand[1]) if operand[0] == 'NUMBER' else variables.get(operand[1], 0)
        
        if operator == '+':
            result += operand_value
        elif operator == '-':
            result -= operand_value
        elif operator == '*':
            result *= operand_value
        elif operator == '/':
            if operand_value == 0:
                raise ZeroDivisionError("Division by zero")
            result //= operand_value
        elif operator == '>':
            result = int(result > operand_value)
        elif operator == '<':
            result = int(result < operand_value)
        elif operator == '==':
            result = int(result == operand_value)
        i += 2
    return result
in
