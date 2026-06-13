def get_gread(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "F"
print(f"marks 95 -> Grade: {get_gread(95)}")
print(f"Marks 82 -> Grade: {get_gread(82)}")
print(f"Marks 65 -> Grade: {get_gread(65)}")
