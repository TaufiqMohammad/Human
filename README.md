Custom Language Interpreter
This is a simple interpreter for a custom language with basic programming constructs such as variable assignment, printing, and conditional statements.
The interpreter is implemented in Python and divided into four main modules for ease of maintenance.

Features
Variable Assignment: Assign values to variables using Set and to.
Arithmetic Operations: Supports addition (+), subtraction (-), multiplication (*), and division (/).
Conditional Statements: Allows If-Then-Else logic with comparison operators (>, <, ==).
Printing Variables: Print the value of a variable with Print.
Error Handling: Detects and reports syntax errors, uninitialized variables, and division by zero.

Files
tokenizer.py: Contains the tokenize function, which converts code into tokens for further processing.
parser.py: Includes the parse and parse_expression functions to build an abstract syntax tree (AST) from tokens.
interpreter.py: Contains the interpret and evaluate_expression functions to execute the AST and handle variable storage.
main.py: Runs the interpreter in a REPL (Read-Eval-Print Loop), allowing users to enter and execute code interactively.

Setup
Requirements
Python 3.6 or later

Installation
Clone the repository or download the files, then navigate to the project directory:
git clone <repository-url>
cd <repository-directory>

Running the Interpreter
Execute the interpreter by running main.py:
python main.py

Usage
In the REPL environment, you can type commands and execute them by pressing Enter. Each command should end with a semicolon (;). Example commands:
Set x to 10;
Print x;
If x > 5 Then
    Print x;
Else
    Print 0;
End If;
Type exit to quit the interpreter.

Example Commands
Setting a Variable: Set x to 5;
Printing a Variable: Print x;

Conditional Statements:
If x > 3 Then
    Print x;
Else
    Print 0;
End If;
Error Handling
The interpreter will provide feedback for:

Syntax Errors: If an unrecognized command is used.
Name Errors: If you try to use a variable that hasn't been initialized.
Zero Division Errors: If division by zero is attempted.

Project Structure
custom-interpreter/
├── tokenizer.py       # Tokenizes the input code
├── parser.py          # Parses tokens into an AST
├── interpreter.py     # Interprets and executes the AST
└── main.py            # REPL for interactive code entry

Future Improvements
Possible enhancements include:
Support for more complex Boolean expressions (e.g., If x > 5 and x < 10)
Expanded arithmetic and logical operators
Support for function definitions and calls

License
This project is open-source and available for modification and redistribution.

