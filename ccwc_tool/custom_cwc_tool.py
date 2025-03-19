import sys
import os
from dotenv import load_dotenv

# Load the .env file to read environment variables
load_dotenv()

def count_bytes(filename):
    """Returns the byte count of the file."""
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    with open(filename, 'rb') as f:
        return len(f.read())

def count_lines(filename):
    """Returns the line count of the file."""
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    
    # Open the file with UTF-8 encoding and handle errors gracefully
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        return len(f.readlines())

def count_words(filename):
    """Returns the word count of the file."""
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    
    # Open the file with UTF-8 encoding and handle errors gracefully
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        return sum(len(line.split()) for line in f)


def count_characters(filename):
    """Returns the character count of the file, supporting multibyte characters."""
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(len(line) for line in f)

def process_input():
    """Main function to handle command-line arguments and run the tool."""
    if len(sys.argv) < 2:
        print("Usage: ccwc [-c|-l|-w|-m] <file>")
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2] if len(sys.argv) > 2 else None

    # If no filename is provided, use the path from the .env file
    if filename is None:
        filename = os.getenv("FILE_PATH")
        if not filename:
            print("Error: No file provided and no default file path found in the .env file.")
            sys.exit(1)

    print(f"Reading from file: {filename}")
    
    # Process options: -c, -l, -w, -m
    if option == '-c':
        count = count_bytes(filename) if filename else sum(len(line.encode()) for line in sys.stdin)
        print(f"{count} {filename}" if filename else count)
    elif option == '-l':
        count = count_lines(filename) if filename else sum(1 for line in sys.stdin)
        print(f"{count} {filename}" if filename else count)
    elif option == '-w':
        count = count_words(filename) if filename else sum(len(line.split()) for line in sys.stdin)
        print(f"{count} {filename}" if filename else count)
    elif option == '-m':
        count = count_characters(filename) if filename else sum(len(line) for line in sys.stdin)
        print(f"{count} {filename}" if filename else count)
    else:
        count_lines_result = count_lines(filename) if filename else sum(1 for line in sys.stdin)
        count_words_result = count_words(filename) if filename else sum(len(line.split()) for line in sys.stdin)
        count_bytes_result = count_bytes(filename) if filename else sum(len(line.encode()) for line in sys.stdin)
        print(f"{count_lines_result} {count_words_result} {count_bytes_result} {filename}" if filename else f"{count_lines_result} {count_words_result} {count_bytes_result}")

if __name__ == "__main__":
    process_input()