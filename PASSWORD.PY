import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    char_pool = ""
    
    if use_uppercase:
        char_pool = char_pool+ string.ascii_uppercase
    if use_lowercase:
        char_pool = char_pool+ string.ascii_lowercase
    if use_digits:
        char_pool = char_pool+ string.digits
    if use_special:
        char_pool = char_pool+string.punctuation
    
    if not char_pool:
        raise ValueError("You must select at least one character type (uppercase, lowercase, digits, special).")
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length < 6:
            print("Password length should be at least 6 characters.")
            return
        
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").lower() == 'yes'
        
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"Your generated password is: {password}")
        
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
