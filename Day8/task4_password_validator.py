password = input("Enter password:")

has_min_length = len(password) >=8
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break;
if has_min_length and has_digit:
    print("valid password")
else:
    print("invalid password")
if not has_min_length:
    print("  -password must be at least 8 charcter long.")
if not has_digit:
    print("  -password must countion at least one number.")