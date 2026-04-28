import random
import string


def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    
    all_chars = letters + digits + symbols

    
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password


def main():
    print("===== PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter desired password length: "))

        if length <= 0:
            print("Please enter a positive number.")
            return

        password = generate_password(length)
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input! Please enter a number.")



if __name__ == "__main__":
    main()
