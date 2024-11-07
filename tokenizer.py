# tokenizer.py
import re

def tokenize(code):
    token_specification = [
        ('NUMBER', r'\d+'),
        ('SET', r'Set'),
        ('TO', r'to'),
        ('PRINT', r'Print'),
        ('IF', r'If'),
        ('THEN', r'Then'),
        ('ELSE', r'Else'),
        ('ENDIF', r'End If'),
        ('GT', r'>'),
        ('LT', r'<'),
        ('EQ', r'=='),
        ('ADD', r'\+'),
        ('SUB', r'-'),
        ('MUL', r'\*'),
        ('DIV', r'/'),
        ('ID', r'[A-Za-z]+'),
        ('NEWLINE', r'\n'),
        ('SKIP', r'[ \t\r]+'),
    ]
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tokens = [
        (match.lastgroup, match.group(match.lastgroup))
        for match in re.finditer(token_regex, code)
        if match.lastgroup not in {'SKIP', 'NEWLINE'}
    ]
    return tokens
