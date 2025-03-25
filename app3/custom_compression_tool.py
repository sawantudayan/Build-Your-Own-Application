import heapq

"""
This module implements a custom compression tool using Huffman coding.

The tool provides functionality to:
- Build a Huffman tree from a set of characters and their frequencies.
- Generate Huffman codes for each character in the tree.
- Encode a string using the generated Huffman codes.
- Decode a Huffman encoded string back to its original form.

Classes:
- Node: A class representing a node in the Huffman tree, which stores a character, its frequency, and pointers to its left and right children.

Functions:
- build_huffman_tree: Builds the Huffman tree based on character frequencies.
- generate_codes: Recursively generates Huffman codes for each character in the tree.
- encode: Encodes a string using the provided Huffman codebook.
- decode: Decodes a Huffman encoded string using the root of the Huffman tree.
"""

class Node:
    """
    A class representing a node in the Huffman tree.
    Each node stores a character, its frequency, and its left and right children.
    """
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """
        This method ensures that nodes can be compared by their frequency.
        """
        return self.freq < other.freq

    def __str__(self):
        """
        String representation of the node for debugging or visualization.
        """
        return f"Node(char={self.char}, freq={self.freq})"

def build_huffman_tree(frequencies):
    """
    Builds the Huffman tree from a dictionary of characters and their frequencies.
    Returns the root node of the tree.
    """
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook=None):
    """
    Recursively generates Huffman codes for each character in the tree.
    The `codebook` is populated with the character codes.
    """
    if codebook is None:
        codebook = {}

    if node:
        if node.char:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook

def encode(input_string, codebook):
    """
    Encodes an input string using the given Huffman codebook.
    """
    return ''.join(codebook[char] for char in input_string)

def decode(encoded_string, root):
    """
    Decodes a Huffman encoded string using the root of the Huffman tree.
    """
    decoded_string = []
    node = root
    for bit in encoded_string:
        node = node.left if bit == '0' else node.right
        if node.char:
            decoded_string.append(node.char)
            node = root

    return ''.join(decoded_string)

def main():
    """
    Main function that takes an input string, builds the Huffman tree, encodes the string,
    and decodes it back to the original text.
    """
    # Take input from the user
    input_string = input("Enter a string: ")

    # Frequency calculation
    frequencies = {char: input_string.count(char) for char in set(input_string)}

    # Build the Huffman tree
    root = build_huffman_tree(frequencies)

    # Generate the Huffman codes
    codebook = generate_codes(root)

    # Encode the input string
    encoded_string = encode(input_string, codebook)
    print(f"Encoded String: {encoded_string}")

    # Decode the encoded string
    decoded_string = decode(encoded_string, root)
    print(f"Decoded String: {decoded_string}")

if __name__ == "__main__":
    main()
