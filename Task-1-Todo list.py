# Mystic Task Scroll - Python CLI Version (Premium Edition)

import sys

# Constants for colors
HEADER = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

def print_animated_header():
    print(f"{BOLD}{HEADER}✨ Welcome to the Mystic Task Scroll ✨{RESET}")
    print(f"{CYAN}Where your productivity meets magic.{RESET}")

def main():
    # Check if ANSI escapes are supported (basic check for Windows)
    if sys.platform == 'win32':
        import os
        os.system('color') # Enables ANSI support in some Windows terminals

    tasks = []
    print_animated_header()
    
    while True:
        print(f"\n{BOLD}{YELLOW}--- Mystic Scroll Menu ---{RESET}")
        print(f"{GREEN}1.{RESET} Inscribe a New Task")
        print(f"{GREEN}2.{RESET} Reveal the Scroll")
        print(f"{GREEN}3.{RESET} Depart from the Sanctuary")
        
        choice = input(f"\n{BOLD}{CYAN}Enter your choice (1-3): {RESET}")
        
        if choice == '1':
            new_task = input(f"\n{YELLOW}What task shall we add to the scroll? {RESET}")
            if new_task.strip():
                tasks.append(new_task.strip())
                print(f"\n{BOLD}{GREEN}✓ '{new_task}' has been inscribed on the scroll!{RESET}")
            else:
                print(f"\n{RED}⚠ You cannot inscribe an empty task!{RESET}")
        
        elif choice == '2':
            if not tasks:
                print(f"\n{RED}The scroll is currently empty and whispers of forgotten deeds...{RESET}")
            else:
                print(f"\n{BOLD}{BLUE}📜 Captured Tasks on the Scroll:{RESET}")
                for index, task in enumerate(tasks, 1):
                    print(f"  {BOLD}{CYAN}{index}.{RESET} {task}")
        
        elif choice == '3':
            print(f"\n{BOLD}{HEADER}Farewell, traveler! May your tasks be completed with ease.{RESET}")
            break
        
        else:
            print(f"\n{BOLD}{RED}⚠ Invalid choice. The spirits are confused. Please try again.{RESET}")

if __name__ == "__main__":
    main()
