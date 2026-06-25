try: 
    age = int(input("Enter your age: "))
    print(f"you are {age} years old. ")
except ValueError:
    print("Error : plase anter a valid numrical age (e.g,  20).")