import random
import string

class PasswordGenerator:
    @staticmethod
    def generate(length=12, use_upper=True, use_digits=True, use_symbols=True):
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase if use_upper else ""
        digits = string.digits if use_digits else ""
        symbols = string.punctuation if use_symbols else ""

        all_chars = lowercase + uppercase + digits + symbols
        if not all_chars:
            return "Error: All character sets are disabled."

        # Ensure at least one of each selected type is included
        password_chars = []
        if use_upper and uppercase:
            password_chars.append(random.choice(uppercase))
        if use_digits and digits:
            password_chars.append(random.choice(digits))
        if use_symbols and symbols:
            password_chars.append(random.choice(symbols))

        # Fill the rest of the length
        for _ in range(length - len(password_chars)):
            password_chars.append(random.choice(all_chars))

        random.shuffle(password_chars)
        return "".join(password_chars)


if __name__ == "__main__":
    print("=== Secure Password Generator ===")
    try:
        length = int(input("Enter desired password length (default 12): ") or 12)
        if length < 4:
            print("Password length should be at least 4 for security.")
        else:
            pwd = PasswordGenerator.generate(length=length)
            print(f"\nGenerated Password: {pwd}")
    except ValueError:
        print("Please enter a valid number for length.")
