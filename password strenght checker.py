import re

def check_password(password):

    if password == "":
        print("Password cannot be empty.")
        return

    if " " in password:
        print("Password must not contain spaces.")
        return

    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    # Check uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter")

    # Check lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter")

    # Check digit
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add a digit")

    # Check special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add a special character")

    # Classify password strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("Strength:", strength + f" ({score}/5)")

    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("No suggestions. Your password is secure.")


# Main program
password = input("Enter your password: ")
check_password(password)