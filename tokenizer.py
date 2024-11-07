import re


def tokenize(code):
    token_specification = [
        ('NUMBER', r'\b\d+\b'),  # Integer numbers
        ('SET', r'\bSet\b'),  # Set keyword
        ('TO', r'\bto\b'),  # to keyword
        ('PRINT', r'\bPrint\b'),  # Print keyword
        ('IF', r'\bIf\b'),  # If keyword
        ('THEN', r'\bThen\b'),  # Then keyword
        ('ELSE', r'\bElse\b'),  # Else keyword
        ('ENDIF', r'\bEnd If\b'),  # End If keyword
        ('GT', r'>'),  # Greater than operator
        ('LT', r'<'),  # Less than operator
        ('EQ', r'=='),  # Equality operator
        ('ADD', r'\+'),  # Addition operator
        ('SUB', r'-'),  # Subtraction operator
        ('MUL', r'\*'),  # Multiplication operator
        ('DIV', r'/'),  # Division operator
        ('ID', r'\b[A-Za-z]+\b'),  # Variable names
        ('NEWLINE', r'\n'),  # Line endings
        ('SKIP', r'[ \t\r]+'),  # Skip whitespace and tabs
    ]

    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tokens = []

    for match in re.finditer(token_regex, code):
        token_type = match.lastgroup
        token_value = match.group(token_type)

        if token_type == 'NEWLINE':
            continue  # Skip newline in token list, may handle differently if needed

        elif token_type != 'SKIP':
            tokens.append((token_type, token_value))

    return tokens
