# Word Counter

A simple Python program that reads a text file and counts the number of words it contains.

## Description

This project was built to satisfy **Task 3: Word Counter**, with the following objectives:

- Read the content of a file
- Split the content into words and count them
- Handle exceptions, such as file not found

## Features

- Reads any plain text file provided by the user
- Counts words by splitting on whitespace
- Gracefully handles missing files and other unexpected errors

## Requirements

- Python 3.x (no external libraries needed)

## Usage

1. Clone or download this repository.
2. Run the script:

   ```bash
   python word_counter.py
   ```

3. When prompted, enter the path to the text file you want to analyze:

   ```
   Enter the name of the text file: sample.txt
   ```

4. The program will output the word count:

   ```
   The file 'sample.txt' contains 42 words.
   ```

## Example

**sample.txt**
```
The quick brown fox jumps over the lazy dog.
```

**Output**
```
The file 'sample.txt' contains 9 words.
```

## Error Handling

- If the file does not exist, the program prints a clear error message instead of crashing.
- Any other unexpected error is caught and reported to the user.

## How It Works

1. Opens the specified file using a `with` statement, which ensures the file is properly closed after reading.
2. Reads the entire file content into a string.
3. Uses `str.split()` to break the content into a list of words (splitting on any whitespace).
4. Returns the length of that list as the word count.

## Possible Extensions

- Count lines and characters in addition to words
- Use regular expressions (`re.findall(r'\b\w+\b', content)`) for stricter word matching that ignores attached punctuation
- Accept the filename as a command-line argument instead of via input prompt

## License

This project is open source and available for educational use.
