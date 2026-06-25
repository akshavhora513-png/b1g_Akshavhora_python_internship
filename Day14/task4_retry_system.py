while True:
    try:
        age = int(input("Enter your age: "))
        break # this line only runs if the above succeeds!
    except ValueError:
      print("Invalid input. please enter number only.")

print(f"thank you . your age is {age}." )