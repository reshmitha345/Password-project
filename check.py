from password_checker import check_password_strength

password = input("Enter your password: ")
result, tips = check_password_strength(password)

print("\nResult:", result)
if tips:
    print("Suggestions to improve:")
    for tip in tips:
        print("-", tip)

