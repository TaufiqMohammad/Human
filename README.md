# Custom Language Interpreter

A simple interpreter for a custom language with basic programming constructs such as variable assignment, printing, and conditional statements. Implemented in Python and organized into modular files for easy maintenance.

---

## Features

- **Variable Assignment**: Assign values to variables with `Set` and `to`.
- **Arithmetic Operations**: Supports `+`, `-`, `*`, and `/`.
- **Conditional Statements**: `If-Then-Else` logic with comparison operators (`>`, `<`, `==`).
- **Printing**: Print variable values using `Print`.
- **Error Handling**: Catches syntax errors, uninitialized variables, and division by zero.

---

## Project Structure

```
custom-interpreter/
├── tokenizer.py       # Tokenizes the input code
├── parser.py          # Parses tokens into an AST
├── interpreter.py     # Interprets and executes the AST
└── main.py            # REPL for interactive code entry
```

### File Overview

- **`tokenizer.py`**: Contains the `tokenize` function, which converts code into tokens for further processing.
- **`parser.py`**: Includes the `parse` and `parse_expression` functions to build an abstract syntax tree (AST) from tokens.
- **`interpreter.py`**: Contains the `interpret` and `evaluate_expression` functions to execute the AST and manage variables.
- **`main.py`**: Runs the interpreter in a REPL (Read-Eval-Print Loop) for interactive code execution.

---

## Setup

### Requirements

- **Python**: Version 3.6 or later

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Interpreter**:

   ```bash
   python main.py
   ```

---

## Usage

### Running Code

In the REPL, type commands and execute them by pressing Enter. Each command should end with a semicolon (`;`). Example commands:

```plaintext
Set x to 10;
Print x;
If x > 5 Then
    Print x;
Else
    Print 0;
End If;
```

Type `exit` to quit the interpreter.

### Example Commands

- **Setting a Variable**: `Set x to 5;`
- **Printing a Variable**: `Print x;`
- **Conditional Statements**:
  ```plaintext
  If x > 3 Then
      Print x;
  Else
      Print 0;
  End If;
  ```

### Error Handling

The interpreter will notify you of the following:

- **Syntax Errors**: For unrecognized commands.
- **Name Errors**: When using a variable that hasn’t been initialized.
- **Zero Division Errors**: If division by zero is attempted.

---

## Future Improvements

Possible enhancements:

- Support for more complex Boolean expressions (e.g., `If x > 5 and x < 10`)
- Expanded arithmetic and logical operators
- Function definitions and calls

---

## License

This project is open-source and available for modification and redistribution.
