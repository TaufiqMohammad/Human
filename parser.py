# parser.py
from tokenizer import tokenize

def parse(tokens):
    ast = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token[0] == 'SET':
            var_name = tokens[i + 1][1]
            value = parse_expression(tokens[i + 3:])  # Skip 'to' keyword
            ast.append(('SET', var_name, value))
            i += len(value) + 3
        elif token[0] == 'PRINT':
            var_name = tokens[i + 1][1]
            ast.append(('PRINT', var_name))
            i += 2
        elif token[0] == 'IF':
            condition = parse_expression(tokens[i + 1:])
            then_branch = []
            else_branch = []
            i += 3
            while i < len(tokens) and tokens[i][0] not in {'ENDIF', 'ELSE'}:
                then_branch.append(tokens[i])
                i += 1
            if i < len(tokens) and tokens[i][0] == 'ELSE':
                i += 1
                while i < len(tokens) and tokens[i][0] != 'ENDIF':
                    else_branch.append(tokens[i])
                    i += 1
            i += 1
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
        else:
            break
        i += 1
    return expression
