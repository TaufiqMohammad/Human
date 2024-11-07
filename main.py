# main.py
from tokenizer import tokenize
from parser import parse
from interpreter import interpret

def repl():
    print("Welcome to the custom language REPL. Type 'exit' to quit.")
    code_buffer = []
    while True:
        user_input = input(">> " if not code_buffer else ".. ").strip()
        if user_input.lower() == 'exit':
            break
        code_buffer.append(user_input)
        if user_input.endswith(';'):
            code = '\n'.join(code_buffer).replace(';', '\n')
            tokens = tokenize(code)
            try:
                ast = parse(tokens)
                interpret(ast)
            except SyntaxError as e:
                print(f"SyntaxError: {e}")
            except NameError as e:
                print(f"NameError: {e}")
            except ZeroDivisionError as e:
                print(f"ZeroDivisionError: {e}")
            code_buffer = []

if __name__ == "__main__":
    repl()
