# Python
DAT
🧮 Simple Python Calculator 🧮A straightforward and easy-to-use calculator function written in Python. Perform basic arithmetic operations with a simple function call! 🚀📝 About The ProjectThis project contains a single Python script, operators.py, which defines a function called calc. This function takes two numbers and an operator as input and prints the result of the calculation. It's a great example of basic function definition and conditional logic in Python. ✨🐍 The Code: operators.pyHere is the complete source code for the calculator function:def calc(a, b, o="*"):
    if o == '+':
        c = a + b
        print("result =", c)
    elif o == '-':
        c = a - b
        print("result =", c)
    elif o == '*':
        c = a * b
        print("result =", c)
    elif o == '/':
        c = a / b
        print("result=", c)
    else:
        print("invalid operator")

# Example call
calc(8, 2)
✅ FeaturesAddition (+) ➕Subtraction (-) ➖Multiplication (*) ✖️Division (/) ➗Default Operation: Defaults to multiplication if no operator is provided.Error Handling: Prints a message for invalid operators.🚀 How to UseTo use the calc function, simply call it with two numbers. You can also provide a third argument to specify the operation.Example 1: Default MultiplicationIf you don't specify an operator, it will multiply the numbers by default.# The operator defaults to '*'
calc(8, 2)
Output:result = 16
Example 2: AdditionProvide '+' as the third argument to add the numbers.calc(10, 5, '+')
Output:result = 15
Example 3: DivisionProvide '/' as the third argument to divide the numbers.calc(20, 4, '/')
Output:result= 5.0
Example 4: Invalid OperatorIf you provide an unsupported operator, it will let you know.calc(7, 3, '%')
Output:invalid operator
<div align="center"><em>Happy calculating! 🔢</em></div>
