import sys
from pkg.calculator import Calculator
from pkg.render import render
import re


def main():
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    expression = " ".join(sys.argv[1:])
    #expression = "3+7*2" # Hardcoded expression for testing
    expression = re.sub(r'([+\-*/])', r' \1 ', expression) # Add spaces around operators
    expression = ' '.join(expression.split()) # remove duplicate spaces
    print(expression)
    try:
        result = calculator.evaluate(expression)
        #to_print = render(expression, result)
        #print(to_print)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()