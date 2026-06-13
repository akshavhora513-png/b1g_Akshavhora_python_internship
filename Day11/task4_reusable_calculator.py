def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if b == 0:
        return "Error : division by zero"
    return a/b

numl = float(input("Enter first number:"))
num2 =float(input("Enter second number:"))

print(f"addition : {add(numl, num2)}")
print(f"sub : {sub(numl, num2)}")
print(f"mul : {mul(numl, num2)}")
print(f"div : {div(numl, num2)}")