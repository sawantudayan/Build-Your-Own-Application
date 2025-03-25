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

def lexer(input_str):
    """
    Tokenizes the input string into a sequence of tokens.

    Args:
        input_str (str): The input string to tokenize.
        
    Yields:
        tuple: A tuple containing the token type and token value.
    """
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
            yield from parse_string(input_str, pos)
        elif char == 't':  # Boolean true
            yield from parse_boolean(input_str, pos, "true", True)
        elif char == 'f':  # Boolean false
            yield from parse_boolean(input_str, pos, "false", False)
        elif char == 'n':  # Null
            yield from parse_null(input_str, pos)
        elif char.isdigit() or char == '-':  # Number (integer or float)
            yield from parse_number(input_str, pos)
        elif char.isspace():
            advance()  # Skip whitespace
        else:
            yield (TOKEN_INVALID, char)
            return

    yield (TOKEN_EOF, None)

def parse_string(input_str, pos):
    """Helper function to parse a string literal."""
    match = re.match(r'"(.*?)"', input_str[pos:])
    if match:
        value = match.group(1)
        pos += len(match.group(0))
        yield (TOKEN_STRING, value)
    else:
        yield (TOKEN_INVALID, 'Invalid string syntax')

def parse_boolean(input_str, pos, value_str, boolean_value):
    """Helper function to parse a boolean literal."""
    if input_str[pos:pos+len(value_str)] == value_str:
        yield (TOKEN_BOOLEAN, boolean_value)
        pos += len(value_str)
    else:
        yield (TOKEN_INVALID, f"Invalid boolean: {value_str}")

def parse_null(input_str, pos):
    """Helper function to parse the 'null' literal."""
    if input_str[pos:pos+4] == "null":
        yield (TOKEN_NULL, None)
        pos += 4
    else:
        yield (TOKEN_INVALID, 'Invalid null syntax')

def parse_number(input_str, pos):
    """Helper function to parse a number literal."""
    match = re.match(r'-?\d+(\.\d+)?', input_str[pos:])
    if match:
        value = match.group(0)
        yield (TOKEN_NUMBER, float(value) if '.' in value else int(value))
        pos += len(value)
    else:
        yield (TOKEN_INVALID, 'Invalid number format')

def parse_array(tokens):
    """Parse a JSON array from tokens."""
    array_values = []
    token = next(tokens)

    if token[0] != TOKEN_LBRACKET:
        print("Invalid JSON: Expected opening bracket '['")
        sys.exit(1)

    token = next(tokens)
    while token[0] != TOKEN_RBRACKET:
        value = parse_value(tokens, token)
        array_values.append(value)

        token = next(tokens)
        if token[0] == TOKEN_COMMA:
            token = next(tokens)
        elif token[0] != TOKEN_RBRACKET:
            print("Invalid JSON: Unexpected token in array")
            sys.exit(1)

    return array_values

def parse_value(tokens, token):
    """
    Parse a JSON value (string, number, boolean, null, object, or array).
    
    Args:
        tokens (iter): The iterator over the token stream.
        token (tuple): The current token to process.
        
    Returns:
        The parsed value (string, number, boolean, etc.)
    """
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

def parse_object(tokens):
    """Parse a JSON object from tokens."""
    obj = {}
    token = next(tokens)

    if token[0] != TOKEN_LBRACE:
        print("Invalid JSON: Expected opening brace '{'")
        sys.exit(1)

    token = next(tokens)
    while token[0] == TOKEN_STRING:
        key = token[1]
        token = next(tokens)

        if token[0] != TOKEN_COLON:
            print("Invalid JSON: Expected colon after key")
            sys.exit(1)

        token = next(tokens)
        value = parse_value(tokens, token)
        obj[key] = value
        token = next(tokens)

        if token[0] == TOKEN_COMMA:
            token = next(tokens)
        elif token[0] == TOKEN_RBRACE:
            break
        else:
            print("Invalid JSON: Unexpected token in object")
            sys.exit(1)

    if token[0] != TOKEN_RBRACE:
        print("Invalid JSON: Expected closing brace '}'")
        sys.exit(1)

    return obj

def parser(input_str):
    """
    Parse the entire JSON structure.
    
    Args:
        input_str (str): The JSON string to parse.
    """
    tokens = lexer(input_str)  # Generate the token stream
    token_list = list(tokens)  # Capture all tokens in a list for printing

    print("Tokens:", token_list)

    token_iter = iter(token_list)  # Create an iterator from the token list
    token = next(token_iter)

    result = parse_value(token_iter, token)

    token = next(token_iter, None)
    if token and token[0] != TOKEN_EOF:
        print("Invalid JSON: Unexpected token after parsing ends")
        sys.exit(1)

    print("Parsed JSON:", result)

if __name__ == "__main__":
    input_json = input("Enter JSON: ")
    parser(input_json)