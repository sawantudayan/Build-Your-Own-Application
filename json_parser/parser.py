import sys
import re

# Token types
TOKEN_LBRACE = 'LBRACE'
TOKEN_RBRACE = 'RBRACE'
TOKEN_LBRACKET = 'LBRACKET'
TOKEN_RBRACKET = 'RBRACKET'
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
        elif char == '[':
            yield (TOKEN_LBRACKET, '[')
            advance()
        elif char == ']':
            yield (TOKEN_RBRACKET, ']')
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

# Helper function: Parse an array
def parse_array(tokens):
    array_values = []
    token = next(tokens)

    if token[0] == TOKEN_LBRACKET:
        token = next(tokens)

        while token[0] != TOKEN_RBRACKET:
            # Parse a value (can be any valid JSON data type)
            value = parse_value(tokens, token)
            array_values.append(value)

            token = next(tokens)

            if token[0] == TOKEN_COMMA:
                token = next(tokens)
            elif token[0] != TOKEN_RBRACKET:
                print("Invalid JSON: Unexpected token in array")
                sys.exit(1)

        return array_values
    else:
        print("Invalid JSON: Expected opening bracket '['")
        sys.exit(1)

# Helper function: Parse a value (string, number, boolean, null, object, or array)
def parse_value(tokens, token):
    if token[0] == TOKEN_STRING:
        return token[1]
    elif token[0] == TOKEN_BOOLEAN:
        return token[1]
    elif token[0] == TOKEN_NULL:
        return token[1]
    elif token[0] == TOKEN_NUMBER:
        return token[1]
    elif token[0] == TOKEN_LBRACE:
        return parse_object(tokens)
    elif token[0] == TOKEN_LBRACKET:
        return parse_array(tokens)
    else:
        print("Invalid JSON: Unexpected token")
        sys.exit(1)

# Helper function: Parse an object (key-value pairs)
def parse_object(tokens):
    obj = {}
    token = next(tokens)

    if token[0] == TOKEN_LBRACE:
        token = next(tokens)

        while token[0] == TOKEN_STRING:
            key = token[1]
            token = next(tokens)

            if token[0] == TOKEN_COLON:
                token = next(tokens)
                value = parse_value(tokens, token)
                obj[key] = value
                token = next(tokens)

                # If there's a comma, continue parsing the next key-value pair
                if token[0] == TOKEN_COMMA:
                    token = next(tokens)
                elif token[0] == TOKEN_RBRACE:
                    break
                else:
                    print("Invalid JSON: Unexpected token in object")
                    sys.exit(1)

        if token[0] == TOKEN_RBRACE:
            return obj
        else:
            print("Invalid JSON: Expected closing brace '}'")
            sys.exit(1)
    else:
        print("Invalid JSON: Expected opening brace '{'")
        sys.exit(1)

# Parser function: Parse the entire JSON structure
def parser(input_str):
    tokens = lexer(input_str)  # Generate the token stream
    token_list = list(tokens)  # Capture all tokens in a list for printing

    # Debugging: Print all tokens for troubleshooting
    print("Tokens:", token_list)

    # Now that we have captured all tokens, use the list to parse
    token_iter = iter(token_list)  # Create an iterator from the token list
    token = next(token_iter)

    # Start parsing the first value (could be object, array, etc.)
    result = parse_value(token_iter, token)

    # Ensure that the token stream ends with EOF
    token = next(token_iter, None)
    if token and token[0] != TOKEN_EOF:
        print("Invalid JSON: Unexpected token after parsing ends")
        sys.exit(1)

    print("Parsed JSON:", result)

if __name__ == "__main__":
    input_json = input("Enter JSON: ")
    parser(input_json)