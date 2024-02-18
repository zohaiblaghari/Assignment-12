import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_numbers=True, use_symbols=True):
    characters =''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_constraints():
    length = int(input("Enter desired password length:"))
    use_lowercase = input("Include lowercase letters? (yes/no):").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no):").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no):").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no):").lower() == 'yes'

    return {'length': length, 'use_lowercase': use_lowercase, 'use_uppercase': use_uppercase, 'use_numbers': use_numbers, 'use_symbols': use_symbols}

if __name__ == "__main__":
    password_constraints = get_password_constraints()
    password = generate_password(** password_constraints)
    print("Generated Password:", password)


