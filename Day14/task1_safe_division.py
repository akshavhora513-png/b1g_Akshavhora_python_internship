try:
    num1 = float(input("enter numerator"))
    num2 = float(input("enter denominator"))

    result = num1/num2
    print(f"result : {result}")

except ZeroDivisionError:    
    print("Error: connot divide by zero")
