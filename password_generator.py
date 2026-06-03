# Project 3: Random Entropy Engine - Password Generator
# Designed for high-security randomized credential synthesis.

import random
import string
import sys
import time

# Premium UI Constants
PURPLE = '\033[95m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
WHITE = '\033[97m'
RESET = '\033[0m'

def print_header():
    print(f"\n{BOLD}{CYAN}⚙️ RANDOM ENTROPY ENGINE ⚙️{RESET}")
    print(f"{YELLOW}Standard Security Protocol: v2.4{RESET}")
    print("-" * 35)

def generate_password(length):
    # Defining character pools
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Combined pool for maximum complexity
    all_chars = letters + numbers + symbols
    
    # Shuffle for extra entropy simulation
    char_list = list(all_chars)
    random.shuffle(char_list)
    
    # Generating the password
    password = "".join(random.choice(char_list) for _ in range(length))
    return password

def main():
    if sys.platform == 'win32':
        import os
        os.system('color')

    print_header()
    
    while True:
        try:
            print(f"\n{BOLD}{WHITE}ENTROPY CONFIGURATION{RESET}")
            user_input = input(f"Enter desired password length (8-64) or 'exit': {RESET}")
            
            if user_input.lower() == 'exit':
                print(f"\n{CYAN}Deactivating Entropy Engine. Stay secure.{RESET}")
                break
                
            length = int(user_input)
            
            if length < 4:
                print(f"{RED}⚠ Warning: Length too short for secure synthesis. Minimum 4 required.{RESET}")
                continue
            if length > 128:
                print(f"{RED}⚠ Warning: Length exceeds buffer capacity. Maximum 128 recommended.{RESET}")
                continue

            print(f"\n{BOLD}{PURPLE}Synthesizing unique credential...{RESET}")
            time.sleep(0.5)
            
            password = generate_password(length)
            
            print(f"{BOLD}{GREEN}Synthesis Complete!{RESET}")
            print(f"\n{BOLD}{WHITE}Your Secure Password:{RESET}")
            print(f"{BOLD}{CYAN}>>> {password} <<<{RESET}")
            print(f"\n{YELLOW}Note: Store this securely. It cannot be recovered once the session ends.{RESET}")
            
        except ValueError:
            print(f"{RED}⚠ ERROR: Please enter a numeric value for length.{RESET}")

if __name__ == "__main__":
    main()
