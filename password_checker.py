# ============================================
# Task 5: Password Strength Checker
# Built by: Gunn Fulwani
# ============================================

import re


def check_password_strength(password):
    strength = 0
    feedback = []

    # Check minimum length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    # Check for uppercase letter
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add at least 1 uppercase letter.")

    # Check for lowercase letter
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add at least 1 lowercase letter.")

    # Check for number
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Add at least 1 number.")

    # Check for special character
    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Add at least 1 special character (!@#$%^&* etc.)")

    return strength, feedback


def password_checker():
    print("=" * 40)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    while True:
        print()
        password = input("Enter a password to check (or 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Goodbye!")
            break

        strength, feedback = check_password_strength(password)

        print()
        print("-" * 40)

        if strength == 5:
            print("Result: STRONG PASSWORD")
            print("Your password meets all requirements!")
        elif strength >= 3:
            print("Result: MODERATE PASSWORD")
            print("Your password could be stronger.")
        else:
            print("Result: WEAK PASSWORD")
            print("Your password needs improvement.")

        print(f"Score: {strength}/5")

        if feedback:
            print("\nSuggestions:")
            for tip in feedback:
                print(f"  - {tip}")

        print("-" * 40)


password_checker()
