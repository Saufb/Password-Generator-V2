import random
import string
import os

def generate_password(length=12, use_uppercase=True, use_digits=True, use_punctuation=True):
    """Generate a strong password with additional options."""
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_punctuation:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one option must be enabled.")

    return ''.join(random.choice(chars) for _ in range(length))

def save_passwords(passwords, filename="passwords.txt"):
    """Save generated passwords to a file."""
    with open(filename, "w") as file:
        for password in passwords:
            file.write(password + "\n")
    print(f"[+] Passwords saved to {filename}")

def display_license():
    """Display the custom license."""
    license_text = """
    /$$$$$$                                                   
   /$$__  $$                                                  
  | $$  \__/  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$ 
  | $$       |____  $$ /$$_____/ /$$__  $$ /$$__  $$ /$$__  $$
  | $$        /$$$$$$$|  $$$$$$ | $$  \ $$| $$$$$$$$| $$  \__/
  | $$    $$ /$$__  $$ \____  $$| $$  | $$| $$_____/| $$      
  |  $$$$$$/|  $$$$$$$ /$$$$$$$/| $$$$$$$/|  $$$$$$$| $$      
   \______/  \_______/|_______/ | $$____/  \_______/|__/      
                                | $$                          
                                | $$                          
                                |__/                          

    License:
    This project is under the MIT License.
    You are free to modify and distribute this tool, but please credit the original source.
    """
    print(license_text)

def main():
    print("[+] Welcome! This is an advanced password generator.")

    display_license()

    try:
        length = int(input("[+] Enter the password length (recommended 12 or more): "))
        if length < 12:
            print("[-] Length must be 12 or more.")
            return

        use_uppercase = input("[+] Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("[+] Include digits? (y/n): ").lower() == 'y'
        use_punctuation = input("[+] Include special characters? (y/n): ").lower() == 'y'

        num_passwords = int(input("[+] How many passwords do you want to generate? (e.g., 5): "))
        if num_passwords < 1:
            print("[-] You must generate at least one password.")
            return

        passwords = [generate_password(length, use_uppercase, use_digits, use_punctuation) for _ in range(num_passwords)]

        print("\n[+] Generated Passwords:")
        for i, password in enumerate(passwords, start=1):
            print(f"  {i}. {password}")

        save_option = input("\n[+] Do you want to save these passwords to a file? (y/n): ").lower() == 'y'
        if save_option:
            filename = input("[+] Enter the filename to save (e.g., passwords.txt): ")
            save_passwords(passwords, filename)

    except ValueError as e:
        print(f"[-] {e}")

if __name__ == "__main__":
    main()
