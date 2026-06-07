from ast import For
import string 
import getpass

BLUE = '\033[34m'
GREEN = '\033[32m'
RESET = '\033[0m' # Resets terminal back to default color
RED = '\033[31m'

print(BLUE + "_" * 68 + RESET)
print(BLUE + "|" + " " * 66 + "|" + RESET)
print(BLUE + "|" + "                  " + GREEN +" PASSWORD STRENGTH CHECKER " + BLUE + "                     " + "|" + RESET)
print(BLUE + "|" + " " * 66 + "|" + RESET)
print(BLUE + "|" + " " * 66 + "|" + RESET)

def check_Password():

    password = getpass.getpass("Enter your password: ")

    if check_common_password(password):
        print("This password is very commonly used and insecure.")
        return

    strength = 0
    feedback = ""
    upper_count = lower_count = special_count = num_count = wspace_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char in string.whitespace:
            wspace_count += 1
        else:
            special_count += 1 

    if lower_count >= 1:
        strength += 1

    if upper_count >= 1:
        strength += 1

    if num_count >= 1:
        strength += 1

    if special_count >= 1:
        strength += 1

    if wspace_count >= 1:
        strength += 1

    if strength == 1:
        feedback = "Very Weak Password"
    elif strength == 2:
        feedback = "Weak Password"
    elif strength == 3:
        feedback = "Moderate Password"
    elif strength == 4:
        feedback = "Strong Password"
    elif strength == 5:
        feedback = "Very Strong Password"
    else:
        feedback = "Extremely Strong Password"

    if len(password) >= 8:
        strength += 1
    else:
        feedback = "Password should be at least 8 characters long."

    print("\nYour password contains:")
    print(f"{upper_count} uppercase letters")
    print(f"{lower_count} lowercase letters")
    print(f"{num_count} numeric characters")
    print(f"{special_count} special characters")
    print(f"{wspace_count} whitespace characters")

    print(f"\nPassword Strength: {strength}/6")
    print(f"Feedback: {feedback}")

def check_common_password(password):
    try:
        with open("common_passwords.txt", "r") as file:
            common_passwords = [line.strip() for line in file]

        if password.lower() in common_passwords:
            return True
        else:
            return False

    except FileNotFoundError:
        print("common_passwords.txt file not found.")
        return False

def askPassword(another_password = False):
    valid = False
    if another_password:
        choice = input("Do you want to enter another password? Entering either yes (y) or no (n): ")
    else:
        choice = input("Do you want to start checking your password? Entering either yes (y) or no (n): ")

    while not valid:
        if choice.lower() in ['y', 'yes']:
            return True
        elif choice.lower() in ['n','no']:
            return False
        else:
            print('Invalid input. Please try again and enter either yes (y) or no (n).')

if __name__ == '__main__':
    print('\n'
          '\n'
    'Welcome to the Password Strength Checker!'
    '\n'
    '\n'
    'Enter a password to check its strength and receive a score to see how secure it is.'
    '\n'
    '\n'
    'A strong password should include uppercase and lowercase letters, numbers and special characters.'
    '\n')

    ask_password = askPassword()   

    while ask_password:
        check_Password()
        ask_password = askPassword(True)

    print("\nThank you for using the Password Strength Checker. Stay safe online!")