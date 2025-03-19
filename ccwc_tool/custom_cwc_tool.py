import sys

def count_bytes(filename):
    """Returns the byte count of the file."""
    with open(filename, 'rb') as f:
        return len(f.read())

def count_lines(filename):
    """Returns the line count of the file."""
    with open(filename, 'r') as f:
        return len(f.readlines())

def count_words(filename):
    """Returns the word count of the file."""
    with open(filename, 'r') as f:
        return sum(len(line.split()) for line in f)

def count_characters(filename):
    """Returns the character count of the file, supporting multibyte characters."""
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(len(line) for line in f)

def process_input():
    """Main function to handle command-line arguments and run the tool."""
    if len(sys.argv) < 2:
        print("Usage: ccwc [-c|-l|-w|-m] <file>")
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2] if len(sys.argv) > 2 else None

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
        count_lines = count_lines(filename) if filename else sum(1 for line in sys.stdin)
        count_words = count_words(filename) if filename else sum(len(line.split()) for line in sys.stdin)
        count_bytes = count_bytes(filename) if filename else sum(len(line.encode()) for line in sys.stdin)
        print(f"{count_lines} {count_words} {count_bytes} {filename}" if filename else f"{count_lines} {count_words} {count_bytes}")

if __name__ == "__main__":
    process_input()
