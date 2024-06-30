# Task 2: File Handling
# 
# 1. Read data from a text file (hamza.txt):

#   - Logic: Open and read the contents of a text file, handling potential exceptions.
#   - Approach:
#       Use open() to read the file within a try block.
#       Handle FileNotFoundError and general exceptions.
#       Print the file contents and count the number of words.
# 
# 2. Implement exception handling:

#   - Logic: Ensure the program handles scenarios where the file is not found or other read errors occur.
#   - Approach:
#       Wrap file operations in a try-except block.
#       Catch specific exceptions and provide informative messages.
# 
# 3. Create a function to write user input to a new file (output.txt):

#   Logic: Write user input to a file, ensuring exceptions related to file operations are handled.
#   Approach:
#       - Use open() in write mode within a try block.
#       - Handle exceptions related to file writing.
# 
# 4. Modify the file reading function to count the number of words:

#   - Logic: Extend the file reading function to count and print the number of words in the file.
#   - Approach:
#       Split the file contents into words and count them using len().

# File: file_handling.py

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
            print(contents)
            word_count = len(contents.split())
            print(f"Word count: {word_count}")
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Reading from data.txt
read_file('hamza.txt')

# Writing to output.txt
user_input = input("Enter some text to write to the file: ")
write_to_file('output.txt', user_input)
