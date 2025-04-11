from  sympy import *
from sympy.parsing.sympy_parser import parse_expr  

def extrema_calculator(fx, x):
    x = symbols(str(x))
    j = 0
    maximas = []
    minimas = []

    diff1 = diff(fx, x)
    diff2 = diff(fx, x, 2)
    critical_points = solve(diff1, x)

    for i in critical_points:
        if diff2.subs(x, i) > 0:
            minimas.append(i)
        elif diff2.subs(x, i) < 0:
            maximas.append(i)
        else:
            j += 1
            
    if j == len(critical_points):
        print("No local extrema found")
    else:
        maximas = [float(i) for i in maximas]
        minimas = [float(i) for i in minimas]
        max_values = [fx.subs(x, i) for i in maximas]
        min_values = [fx.subs(x, i) for i in minimas]

        print(f"Local maximas of function are at:{maximas} and their value are: {max_values}")
        print(f"Local minimas of function are at:{minimas} and their value are: {min_values}")


def main():
    fx = input("Enter the function: ")
    x = input("Enter the variable to differentiate: ")
    
    # Parse the input expression
    fx = parse_expr(fx)
    
    extrema_calculator(fx, x)

main()
