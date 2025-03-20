import sys
import re

# Token types
TOKEN_LBRACE = 'LBRACE'
TOKEN_RBRACE = 'RBRACE'
TOKEN_COLON = 'COLON'
TOKEN_COMMA = 'COMMA'
TOKEN_STRING = 'STRING'
TOKEN_BOOLEAN = 'BOOLEAN'
TOKEN_NULL = 'NULL'
TOKEN_NUMBER = 'NUMBER'
TOKEN_EOF = 'EOF'
TOKEN_INVALID = 'INVALID'

# Lexer function: Tokenizes the input string
def lexer(input_str):
    pos = 0
    length = len(input_str)

    def current_char():
        return input_str[pos] if pos < length else None

    def advance():
        nonlocal pos
        pos += 1

    while pos < length:
        char = current_char()

        if char == '{':
            yield (TOKEN_LBRACE, '{')
            advance()
        elif char == '}':
            yield (TOKEN_RBRACE, '}')
            advance()
        elif char == ':':
            yield (TOKEN_COLON, ':')
            advance()
        elif char == ',':
            yield (TOKEN_COMMA, ',')
            advance()
        elif char == '"':  # String literal
            match = re.match(r'"(.*?)"', input_str[pos:])
            if match:
                value = match.group(1)
                yield (TOKEN_STRING, value)
                pos += len(match.group(0))
        elif char == 't':  # Boolean true
            if input_str[pos:pos+4] == "true":
                yield (TOKEN_BOOLEAN, True)
                pos += 4
            else:
                yield (TOKEN_INVALID, char)
                return
        elif char == 'f':  # Boolean false
            if input_str[pos:pos+5] == "false":
                yield (TOKEN_BOOLEAN, False)
                pos += 5
            else:
                yield (TOKEN_INVALID, char)
                return
        elif char == 'n':  # Null
            if input_str[pos:pos+4] == "null":
                yield (TOKEN_NULL, None)
                pos += 4
            else:
                yield (TOKEN_INVALID, char)
                return
        elif char.isdigit() or char == '-':  # Number (integer or float)
            match = re.match(r'-?\d+(\.\d+)?', input_str[pos:])
            if match:
                value = match.group(0)
                yield (TOKEN_NUMBER, float(value) if '.' in value else int(value))
                pos += len(value)
        elif char.isspace():
            # Skip whitespace
            advance()
        else:
            yield (TOKEN_INVALID, char)
            return

    yield (TOKEN_EOF, None)

# Parser function: Parses tokens and checks for valid JSON objects with multiple data types
def parser(input_str):
    tokens = lexer(input_str)
    token = next(tokens)

    if token[0] == TOKEN_LBRACE:
        token = next(tokens)

        # Parse key-value pairs
        while token[0] == TOKEN_STRING:
            key = token[1]
            token = next(tokens)

            if token[0] == TOKEN_COLON:
                token = next(tokens)
                # Check for string, boolean, null, or number as value
                if token[0] == TOKEN_STRING:  # String value
                    value = token[1]
                elif token[0] == TOKEN_BOOLEAN:  # Boolean value
                    value = token[1]
                elif token[0] == TOKEN_NULL:  # Null value
                    value = token[1]
                elif token[0] == TOKEN_NUMBER:  # Numeric value
                    value = token[1]
                else:
                    print("Invalid JSON: Expected a value")
                    sys.exit(1)

                print(f'Key: {key}, Value: {value}')
                token = next(tokens)

                # If there's a comma, continue parsing the next key-value pair
                if token[0] == TOKEN_COMMA:
                    token = next(tokens)
                elif token[0] == TOKEN_RBRACE:
                    break
                else:
                    print("Invalid JSON: Unexpected token")
                    sys.exit(1)
        
        if token[0] == TOKEN_RBRACE:
            print("Valid JSON")
            sys.exit(0)
        else:
            print("Invalid JSON: Expected closing brace '}'")
            sys.exit(1)
    else:
        print("Invalid JSON: Expected opening brace '{'")
        sys.exit(1)

if __name__ == "__main__":
    input_json = input("Enter JSON: ")
    parser(input_json)