"""
Conditional statement examples
"""

def check_age(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

def is_even(number):
    return "Even" if number % 2 == 0 else "Odd"

def grade_checker(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    print("Age 10 va 10:", check_age(10))
    print("Age 25   va 25:", check_age(25))
    print("Number 7 va 7:", is_even(7))
    print("Number 10 va 10:", is_even(10))
    print("Score 85 va 85:", grade_checker(85))
