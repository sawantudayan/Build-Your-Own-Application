import sys
import os
from dotenv import load_dotenv

# Load the .env file to read environment variables
load_dotenv()

"""
This script provides functionality for counting various file statistics:
- bytes (-c)
- lines (-l)
- words (-w)
- characters (-m)

It reads a file or standard input and returns the count based on the option provided.
"""

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


def show_help():
    """Displays the help message for the tool."""
    print("""
Usage: python custom_cwc_tool.py [options] <file>

Options:
  -c, --bytes       Count the number of bytes in the file
  -l, --lines       Count the number of lines in the file
  -w, --words       Count the number of words in the file
  -m, --characters  Count the number of characters in the file
  -h, --help        Show this help message and exit

If no file is provided, the program will read from standard input (stdin).

Example usage:
  python custom_cwc_tool.py -c myfile.txt     # Count bytes in 'myfile.txt'
  python custom_cwc_tool.py -l myfile.txt     # Count lines in 'myfile.txt'
  python custom_cwc_tool.py -w myfile.txt     # Count words in 'myfile.txt'
  python custom_cwc_tool.py -m myfile.txt     # Count characters in 'myfile.txt'
  echo "Hello World" | python custom_cwc_tool.py -w  # Count words from stdin
    """)

def process_input():
    """Main function to handle command-line arguments and run the tool."""
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']:
        show_help()
        sys.exit(0)

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
    if option in ['-c', '--bytes']:
        count = count_bytes(filename) if filename else sum(len(line.encode()) for line in sys.stdin)
        print(f"{count} {filename}" if filename else count)
    elif option in ['-l', '--lines']:
        count = count_lines(filename) if filename else sum(1 for line in sys.stdin)
        print(f"{count} {filename}" if filename else count)
    elif option in ['-w', '--words']:
        count = count_words(filename) if filename else sum(len(line.split()) for line in sys.stdin)
        print(f"{count} {filename}" if filename else count)
    elif option in ['-m', '--characters']:
        count = count_characters(filename) if filename else sum(len(line) for line in sys.stdin)
        print(f"{count} {filename}" if filename else count)
    else:
        # If no specific option is provided, count all (lines, words, bytes)
        count_lines_result = count_lines(filename) if filename else sum(1 for line in sys.stdin)
        count_words_result = count_words(filename) if filename else sum(len(line.split()) for line in sys.stdin)
        count_bytes_result = count_bytes(filename) if filename else sum(len(line.encode()) for line in sys.stdin)
        print(f"{count_lines_result} {count_words_result} {count_bytes_result} {filename}" if filename
              else f"{count_lines_result} {count_words_result} {count_bytes_result}")


if __name__ == "__main__":
    process_input()