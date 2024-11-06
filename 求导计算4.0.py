import sympy as sp
import math

def factorial(n):
    return math.factorial(n)


def get_function():
    expr_str = input("请输入函数表达式（例如：x**2 + 2*x + 1）：")
    x = sp.symbols('x')
    return sp.sympify(expr_str)


def differentiate(func, n):
    x = sp.symbols('x')
    derivative = func
    for i in range(n):
        derivative = sp.diff(derivative, x)
    return derivative



def main():
    while True:
        func = get_function()
        n = int(input("请输入求导的阶数："))
        derivative = differentiate(func, n)
        print(f"函数的{n}阶导数为：{derivative}")
        
        choice = input("是否继续求导？（输入 q 退出，其他键继续）：")
        if choice.lower() == 'q':
            break



if __name__ == "__main__":
    main()