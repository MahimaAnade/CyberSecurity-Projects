import re

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search("[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letter")

    if re.search("[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letter")

    if re.search("[0-9]", password):
        score += 1
    else:
        suggestions.append("Include numbers")

    if re.search("[@#$%^&*!]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    if score <= 2:
        print("Weak Password")
    elif score <= 4:
        print("Medium Password")
    else:
        print("Strong Password")

    if suggestions:
        print("\nSuggestions to improve password:")
        for s in suggestions:
            print("-", s)


password = input("Enter your password: ")
check_password_strength(password)