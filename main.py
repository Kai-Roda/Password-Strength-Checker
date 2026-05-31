import string 
import getpass

def check_passWord():
    password = getpass.getpass("Enter your password: ")
    strength = 0
    changeNeeded = ""
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
        changeNeeded = "Very Weak Password - please consider adding more character types to strengthen your password."
    elif strength == 2:
        changeNeeded = "Weak Password - please consider adding more character types to strengthen your password."
    elif strength == 3:
        changeNeeded = "Moderate Password - please consider adding more character types to strengthen your password."
    elif strength == 4:
        changeNeeded = "Strong Password - good job! Consider adding more character types for an even stronger password."
    else:
        changeNeeded = "Very Strong Password - great job!"



    print(f"Password Strength: {strength}/5")
    print(f"Feedback: {changeNeeded}")

check_passWord()