# Password Complexity Checker

# Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.

import string
import random

def check_password_strength(password):
    length_requirement = 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    is_length_valid = len(password) >= length_requirement
    is_complex_enough = has_uppercase and has_lowercase and has_digit and has_special

    if is_length_valid and is_complex_enough:
        return "Strong password"
    else:
        feedback = []
        if not is_length_valid:
            feedback.append("\nPassword should be at least {} characters long.".format(length_requirement))
        if not has_uppercase:
            feedback.append("\nPassword should include uppercase letters.")
        if not has_lowercase:
            feedback.append("\nPassword should include lowercase letters.")
        if not has_digit:
            feedback.append("\nPassword should include digits.")
        if not has_special:
            feedback.append("\nPassword should include special characters.")
        
        return "Weak password. Here are some suggestions for you: {}".format(", ".join(feedback))

def generate_strong_password(base_password):
    additional_chars = []

    if not any(char.islower() for char in base_password):
        additional_chars.append(random.choice(string.ascii_lowercase))
    
    if not any(char.isupper() for char in base_password):
        additional_chars.append(random.choice(string.ascii_uppercase))
    
    if not any(char.isdigit() for char in base_password):
        additional_chars.append(random.choice(string.digits))
    
    if not any(char in string.punctuation for char in base_password):
        additional_chars.append(random.choice(string.punctuation))

    while len(base_password) + len(additional_chars) < 8:
        additional_chars.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

    combined_chars = list(base_password)
    for char in additional_chars:
        pos = random.randint(0, len(combined_chars))
        combined_chars.insert(pos, char)

    return ''.join(combined_chars)

def suggest_stronger_password(password, count=5):
    suggestions = set()
    suggested_passwords = []

    while len(suggested_passwords) < count:
        stronger_password = generate_strong_password(password)

        if stronger_password not in suggestions:
            suggestions.add(stronger_password)
            suggested_passwords.append(stronger_password)
    
    return suggested_passwords

if __name__ == "__main__":
    suggestion_counter = 0
    while True:
        print("Welcome To Password Complexity Checker Tool:\n")
        password = input("Enter your password: ")
        
        strength = check_password_strength(password)
        print(strength)
        
        if strength != "Strong password":
            suggestions = suggest_stronger_password(password, count=5)
            print("Suggested stronger passwords:")
            for idx, suggestion in enumerate(suggestions):
                suggestion_counter += 1
                print(f"{suggestion_counter}. {suggestion}")
            
            more_suggestions = input("Do you want more suggested passwords? (yes/no): ").strip().lower()
            while more_suggestions not in {"yes", "no"}:
                print("Invalid input. Please enter 'yes' or 'no'.")
                more_suggestions = input("Do you want more suggested passwords? (yes/no): ").strip().lower()

            while more_suggestions == "yes":
                additional_suggestions = suggest_stronger_password(password, count=5)
                print("Additional suggested passwords:")
                for idx, suggestion in enumerate(additional_suggestions):
                    suggestion_counter += 1
                    print(f"{suggestion_counter}. {suggestion}")

                more_suggestions = input("Do you want more suggested passwords? (yes/no): ").strip().lower()
                while more_suggestions not in {"yes", "no"}:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    more_suggestions = input("Do you want more suggested passwords? (yes/no): ").strip().lower()
            
            if more_suggestions == "no":
                print("\n'Choosing a hard-to-guess, but easy-to-remember password is important. Thank you!'")
                break
        else:
            break
