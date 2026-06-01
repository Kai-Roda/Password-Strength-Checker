import string 
import getpass

def check_Password():
    password = getpass.getpass("Enter your password: ")
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

    if wspace_count >= 1:
        strength += 1

    if special_count >= 1:
        strength += 1

    if strength == 1:
        feedback = "Very Weak Password - please consider adding more character types to strengthen your password."
    elif strength == 2:
        feedback = "Weak Password - please consider adding more character types to strengthen your password."
    elif strength == 3:
        feedback = "Moderate Password - please consider adding more character types to strengthen your password."
    elif strength == 4:
        feedback = "Strong Password - good job! Consider adding more character types for an even stronger password."
    else:
        feedback = "Very Strong Password - great job!"

    print(f"Password Strength: {strength}/5")
    print(f"Feedback: {feedback}")

def askPassword(another_password = False):
    valid = False
    if another_password:
        choice = input("Do you want to enter another password? Entering either yes (y) or no (n): ")
    else:
        choice = input("Do you want to start checking your password? Entering either yes (y) or no (n): ")

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
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
    if ask_password:
        check_Password()