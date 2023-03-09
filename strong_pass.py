import argparse
import string
import random

def generate_password(length=12, upper=True, lower=True, digits=True, special=True):
    # Define the character sets to use for each character type
    upper_chars = string.ascii_uppercase if upper else ""
    lower_chars = string.ascii_lowercase if lower else ""
    digit_chars = string.digits if digits else ""
    special_chars = string.punctuation if special else ""

    # Combine the character sets into a single set
    all_chars = upper_chars + lower_chars + digit_chars + special_chars

    # Generate the password
    password = "".join(random.choice(all_chars) for _ in range(length))

    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a strong password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password.")
    parser.add_argument("-u", "--upper", action="store_true", help="Include uppercase letters.")
    parser.add_argument("-o", "--lower", action="store_true", help="Include lowercase letters.")
    parser.add_argument("-d", "--digits", action="store_true", help="Include digits.")
    parser.add_argument("-s", "--special", action="store_true", help="Include special characters.")

    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        upper=args.upper,
        lower=args.lower,
        digits=args.digits,
        special=args.special
    )

    print(password)
