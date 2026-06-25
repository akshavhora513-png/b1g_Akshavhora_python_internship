try:
    num1 = float(input("Enter numerator:"))
    num2 = float(input("enter denomintor:"))

    result = num1 / num2
    print(f"result : {result}")

except ValueError:
    print("Error : input must be a valid number.")
except ZeroDivisionError:
    print("Error : connot divide by zero.")