# Build Your Own JSON Parser


### Description

In this challenge, I have created a Python-based JSON parser from scratch. This application will allow you to understand the process of parsing JSON data through various stages. The goal of the project is to implement a parser that can read and analyze JSON data, identifying whether the structure is valid or not, and reporting errors when necessary.

This project starts by parsing simple JSON structures and gradually extends its capabilities to handle more complex data types, including strings, numbers, booleans, null values, and nested objects and arrays. By the end of this challenge, you will have a fully functional, custom JSON parser.

### Problem Statement
JSON ```(JavaScript Object Notation)``` is a lightweight data-interchange format that is commonly used for transmitting data between a server and a client in web applications. The purpose of this challenge is to build a simple JSON parser that can handle different types of JSON objects and structures.

The parser should go through the following steps:

 - Step 1: Implement a basic lexer and parser to check if a given input is a valid empty JSON object ```({})``` or an invalid JSON.
 - Step 2: Extend the parser to handle JSON objects with string keys and string values, e.g., ```{"key": "value"}```.
 - Step 3: Further extend the parser to handle additional JSON data types: booleans ```(true, false)```, null values, and numbers, e.g., {"key1": true, "key2": false, "key3": null, "key4": 101}.
 - Step 4: Enhance the parser to handle nested objects and arrays, e.g., ```{"key": "value", "key-n": 101, "key-o": {}, "key-l": []}```.
 - Step 5: Add custom tests to ensure that the parser works correctly for various edge cases and produces meaningful error messages for invalid JSON.

 By completing this challenge, you will have a deeper understanding of parsing techniques and the steps involved in creating a basic JSON parser.

### Steps to Build the JSON Parser
Set Up the Development Environment:
Choose your IDE or editor, set up Python, and ensure you have a working environment for testing the parser.

### Step 1 - Basic JSON Parsing:

Implement a lexer that can handle the simplest form of JSON—an empty object ```({})```. Also, set up the parser to handle this structure and report success (exit code 0) or failure (exit code 1).

 - Key Functionality: Lexical analysis for {} and invalid JSON detection.
- Test Cases: Provided in the ```tests/step1``` directory.


### Step 2 - Handling String Keys and Values:

Extend the parser to handle JSON objects with string keys and string values, e.g., ```{"key": "value"}```.

 - Key Functionality: Handle string parsing and key-value pairs.
 - Test Cases: Provided in the ```tests/step2``` directory.


### Step 3 - Handling Additional Data Types:

The parser should be extended to handle JSON objects containing booleans, null values, and numeric values.

- Key Functionality: Parse true, false, null, and numeric values in addition to strings.
- Test Cases: Provided in the ```tests/step3``` directory.


### Step 4 - Nested Objects and Arrays:

Implement the ability to parse nested objects ```({})``` and arrays ```([])```.

- Key Functionality: Nested structures and array parsing.
- Test Cases: Provided in the ```tests/step4``` directory.


### Step 5 - Additional Test Coverage:
Add your own test cases to ensure that the parser can handle both valid and invalid JSON. Ensure that meaningful error messages are reported for invalid inputs.

Key Functionality: Error handling and testing invalid JSON scenarios.
Test Cases: Add additional cases based on edge cases or tricky inputs.


### Key Methods in the Parser
 - Lexer ```(Tokenization)```: 
A method to break down the input string into meaningful tokens. Each token represents a meaningful component of the JSON syntax (e.g., string literals, numbers, curly braces, etc.).

 - Parser ```(Syntactic Analysis)```:
A method to process the sequence of tokens and verify if they match the correct JSON structure based on the syntax rules.

 - Error Handling
Functions to catch and display error messages if the JSON input is invalid or malformed.


## Running the Tests

To test the parser, run the following command:

```python3
python parser.py
```