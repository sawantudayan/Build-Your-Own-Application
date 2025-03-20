import sys

# Token types
TOKEN_LBRACE = 'LBRACE'
TOKEN_RBRACE = 'RBRACE'
TOKEN_EOF = 'EOF'
TOKEN_INVALID = 'INVALID'

# Lexer function: Tokenizes the input string
def lexer(input_str):
    pos = 0
    length = len(input_str)
    
    # Helper to get the current character
    def current_char():
        return input_str[pos] if pos < length else None

    # Helper to advance position
    def advance():
        nonlocal pos
        pos += 1

    # Start tokenizing
    while pos < length:
        char = current_char()
        
        if char == '{':
            yield (TOKEN_LBRACE, '{')
            advance()
        elif char == '}':
            yield (TOKEN_RBRACE, '}')
            advance()
        else:
            # If we encounter anything other than valid characters, return INVALID token
            yield (TOKEN_INVALID, char)
            return

    # End of file token
    yield (TOKEN_EOF, None)

# Parser function: Parses tokens and checks for a valid empty object
def parser(input_str):
    tokens = lexer(input_str)
    token = next(tokens)

    if token[0] == TOKEN_LBRACE:
        token = next(tokens)
        if token[0] == TOKEN_RBRACE:
            token = next(tokens)
            if token[0] == TOKEN_EOF:
                print("Valid JSON")
                sys.exit(0)
            else:
                print("Invalid JSON")
                sys.exit(1)
        else:
            print("Invalid JSON")
            sys.exit(1)
    else:
        print("Invalid JSON")
        sys.exit(1)

if __name__ == "__main__":
    # Test with an empty JSON object {}
    input_json = input("Enter JSON: ")
    parser(input_json)
