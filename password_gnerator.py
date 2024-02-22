import random
import string

def generate_strong_password(length=12):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password has a mix of lowercase, uppercase, digits, and special characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Ensure at least one character from each category
    password = [random.choice(lowercase_letters),
                random.choice(uppercase_letters),
                random.choice(digits),
                random.choice(punctuation)]

    # Fill up the rest of the password with random characters
    password.extend(random.choice(characters) for _ in range(length - 4))

    # Shuffle the password to make it more random
    random.shuffle(password)

    # Convert the list of characters into a string
    password = ''.join(password)

    return password

while True:
    length_of_password = input('enter desired length of password :')
    try:
        length_of_password = int(length_of_password)
    except:
        print("Sorry, a password length must be an integer!")
        exit(0)

    strong_password = generate_strong_password(length_of_password)
    print("Generated Strong Password:", strong_password)