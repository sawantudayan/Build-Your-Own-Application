# Build Your Own wc Tool

### Description:

I've created a custom version of the classic Unix command-line tool wc, called ccwc. The goal of this project was to replicate and extend the functionality of wc _(word count)_ using Python. This tool counts the number of lines, words, characters, and bytes in a file. It follows the Unix philosophy of simple, focused tools that can be connected together to build powerful workflows. The steps guide you through progressively adding functionality to create an efficient, flexible tool.

### Problem Statement:

The task is to build your own version of the wc command using Python. The tool should support counting the following:

    -c: Byte count in a file.
    -l: Line count in a file.
    -w: Word count in a file.
    -m: Character count (supporting multibyte characters).

Default option: Outputs the byte, line, and word counts.
Standard Input: The ability to read from standard input if no file is specified.


# Steps:

### 0 : Setup
Before starting development, make sure your environment is ready. Set up your IDE or text editor of choice, and download the [test.txt](https://www.dropbox.com/scl/fi/d4zs6aoq6hr3oew2b6a9v/test.txt?rlkey=20c9d257pxd5emjjzd1gcbn03&e=1&dl=0) file that will be used for testing the tool. You can get this file from the provided link.

### 1: Byte Count (-c)
In this step, your goal is to create a simple version of ccwc that supports the -c option. It will output the byte count of a given file.

- Objective: Implement the command ccwc -c test.txt to count the bytes in test.txt.
- Expected Output:

```yaml
342190 test.txt
```

If you encounter issues, debug your code and ensure the output matches the expected result.

<br>


### 2: Line Count (-l)
Next, enhance the tool to support the -l option to count the number of lines in the file.

- Objective: Implement the command ccwc -l test.txt to count the lines.
- Expected Output:
```yaml
7145 test.txt
```

If this doesn’t work, revisit your code, debug, and ensure the line count is accurate.

<br>


### 3: Word Count (-w)
Now, add the -w option to count words in the file.

- Objective: Implement the command ccwc -w test.txt to count the words.
- Expected Output:
```yaml
58164 test.txt
```

If the output doesn’t match, carefully check your word count logic.

<br>


### 4: Character Count (-m)

For this step, you’ll add support for the -m option, which counts the characters in a file. Depending on your locale, this may match the byte count from -c.

- Objective: Implement the command ccwc -m test.txt to count characters.
- Expected Output (may vary depending on locale):
```yaml
339292 test.txt
```

Ensure that your locale handles multibyte characters correctly.

<br>


### Step Five: Default Option
In this step, your tool should support the default behavior, which is equivalent to using -c, -l, and -w without any flags.

- Objective: Implement the command ccwc test.txt to output the byte, line, and word counts.
- Expected Output:

```yaml
7145   58164  342190 test.txt
```
If this step doesn’t work, review the implementation and make sure all counts are correctly handled.

<br>


### Final Step: Standard Input
Lastly, add functionality to support reading from standard input when no filename is provided.

- Objective: Implement the command cat test.txt | ccwc -l to read from standard input.
- Expected Output:
```yaml
7145
```

Once this is working, you’ve completed the challenge! Congratulations on building a useful, simple tool.

<br>


### Example Usage:

- `ccwc -c test.txt`: Outputs the byte count of `test.txt`.
- `ccwc -l test.txt`: Outputs the line count of `test.txt`.
- `ccwc -w test.txt`: Outputs the word count of `test.txt`.
- `ccwc test.txt`: Outputs the line, word, and byte counts for `test.txt`.
- `cat test.txt | ccwc -l`: Reads from standard input and outputs the line count.
