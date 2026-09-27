def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        words = content.split()
        word_count = len(words)
        
        print(f"The file '{filename}' contains {word_count} words.")
        return word_count
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    filename = input("Enter the name of the text file: ")
    count_words(filename)