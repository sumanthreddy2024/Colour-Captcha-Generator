import random
import sys
from colorama import Fore, Back, Style, init

# Initialize Colorama
init(autoreset=True)

# Define constants
CAPTCHA_CHARACTERS = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
COLORS = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
    Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

def generate_pattern(width: int, height: int) -> str:
    """Generate a random CAPTCHA art pattern."""
    pattern = ''
    for _ in range(height):
        row = ''.join(random.choice(CAPTCHA_CHARACTERS) for _ in range(width))
        pattern += row + '\n'
    return pattern.strip()  # Remove trailing newline

def colorize_pattern(pattern: str) -> str:
    """Apply random colors to the CAPTCHA art pattern."""
    colored_pattern = ''
    for line in pattern.split('\n'):
        color = random.choice(COLORS)
        colored_pattern += color + line + '\n'
    return colored_pattern.strip()  # Remove trailing newline

def get_user_input(prompt: str) -> int:
    """Get user input and validate it as a positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    width = get_user_input("Enter that how many letter captcha needed: ")
    height = get_user_input("Enter  that how many captcha needed: ")
    
    pattern = generate_pattern(width, height)
    colored_pattern = colorize_pattern(pattern)
    print(colored_pattern)


if __name__ == "__main__":
    main()
