import random
import string

def generate_password(length):
    """
    Generate a strong, random password of the specified length.

    :param length: int - Length of the password to be generated
    :return: str - Randomly generated password
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    # Define character pools
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choices(characters, k=length))

    return password

def main():
    """
    Main function to prompt user input and display the generated password.
    """
    print("Welcome to the Password Generator!")

    try:
        # Get user input for password length
        length = int(input("Enter the desired password length: ").strip())
        if length < 4:
            print("Password length must be at least 4.")
            return

        # Generate and display the password
        password = generate_password(length)
        print("\nGenerated Password:")
        print(password)

    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
