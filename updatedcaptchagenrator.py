import random
import sys
from colorama import Fore, Back, Style, init
import logging

# Initialize Colorama
init(autoreset=True)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants
CAPTCHA_OBJECTS_OR_LETTERS = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
COLORS = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
    Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

def creating_pattern(width: int, height: int) -> str:
    """Generate a random CAPTCHA art pattern."""
    logging.info(f"Generating CAPTCHA pattern with symobls {width} and height {height}")
    pattern = ''
    for _ in range(height):
        row = ''.join(random.choice(CAPTCHA_OBJECTS_OR_LETTERS) for _ in range(width))
        pattern += row + '\n'
    logging.debug(f"Generated pattern: {pattern}")
    return pattern.strip()  # Remove trailing newline

def colorize_pattern(pattern: str) -> str:
    """Apply random colors to the CAPTCHA art pattern."""
    logging.info("Colorizing CAPTCHA pattern")
    colored_pattern = ''
    for line in pattern.split('\n'):
        color = random.choice(COLORS)
        colored_pattern += color + line + '\n'
    logging.debug(f"Colored pattern: {colored_pattern}")
    return colored_pattern.strip()  # Remove trailing newline

def take_response_from_user(prompt: str) -> int:
    """Get user input and analyse it as a positive integer."""
    logging.info(f"Getting user input for {prompt}")
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                logging.warning("Invalid input. Please enter a positive integer.")
                print("Please enter a positive integer.")
            else:
                logging.info(f"User input: {value}")
                return value
        except ValueError:
            logging.error("Invalid input. Please enter a positive integer.")
            print("Invalid input. Please enter a positive integer.")

def main():
    logging.info("Starting main function")
    width = take_response_from_user("Enter that how many letter captcha needed: ")
    height = take_response_from_user("Enter  that how many captcha needed: ")
    
    pattern = creating_pattern(width, height)
    colored_pattern = colorize_pattern(pattern)
    logging.info("Printing colored pattern")
    print(colored_pattern)


if __name__ == "__main__":
    main()
