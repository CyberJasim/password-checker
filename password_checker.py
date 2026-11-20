# password strength checker

import string

# password strength check conditions:
# 1. Minimum length of 8 characters
# 2. At least one numeric digit
# 3. At least one uppercase letter
# 4. At least one lowercase letter
# 5. At least one special symbol

def check_password_strength(password):
    if len(password) < 8: 
        return "Weak: password must be at least 8 chars"

    if not any(char.isdigit() for char in password):
        return "Weak: password must contain a digit"

    if not any(char.isupper() for char in password):
        return "Weak: password must contain an upper char"

    if not any(char.islower() for char in password):
        return "Weak: password must contain a lower char"

    if not any(char in string.punctuation for char in password):
        return "Medium: password must contain a special char"

    return "Strong: Your password is secured!"


def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password = input("Enter your password or type 'exit' to quit: ")

        if password.lower() == 'exit':
            print("Thank you for using this tool")
            break

        result = check_password_strength(password)
        print(result)


# Run the password checker tool
if __name__ == "__main__":
    password_checker()