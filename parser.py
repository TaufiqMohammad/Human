# parser.py

def parse(tokens):
    ast = []
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token[0] == 'SET':
            var_name = tokens[i + 1][1]
            value = parse_expression(tokens[i + 3:])  # Skip 'to' keyword
            ast.append(('SET', var_name, value))
            i += len(value) + 3  # Move past 'Set', variable, 'to', and expression

        elif token[0] == 'PRINT':
            var_name = tokens[i + 1][1]
            ast.append(('PRINT', var_name))
            i += 2  # Move past 'Print' and variable

        elif token[0] == 'IF':
            condition = parse_expression(tokens[i + 1:])  # Parse entire condition after 'If'
            then_branch = []
            else_branch = []
            i += len(condition) + 2  # Move past 'If', condition, 'Then'

            # Parse the 'Then' block
            while i < len(tokens) and tokens[i][0] not in {'ENDIF', 'ELSE'}:
                then_branch.append(tokens[i])
                i += 1

            # Parse the 'Else' block if present
            if i < len(tokens) and tokens[i][0] == 'ELSE':
                i += 1  # Skip 'Else'
                while i < len(tokens) and tokens[i][0] != 'ENDIF':
                    else_branch.append(tokens[i])
                    i += 1

            i += 1  # Move past 'End If'
            ast.append(('IF', condition, parse(then_branch), parse(else_branch)))

        else:
            raise SyntaxError(f"Unknown token: {token[1]}")
    return ast


def parse_expression(tokens):
    expression = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token[0] in ('NUMBER', 'ADD', 'SUB', 'MUL', 'DIV', 'GT', 'LT', 'EQ'):
            expression.append(token)
        elif token[0] == 'ID':
            expression.append(token)
        elif token[0] in {'THEN', 'ENDIF', 'ELSE'}:
            # Stop parsing at control-flow keywords
            break
        else:
            raise SyntaxError(f"Unknown token: {token[1]}")
        i += 1
    return expression
