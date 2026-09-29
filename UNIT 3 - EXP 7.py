# assignment1.py
# Program: Line Counter and Extractor
# Purpose:
# 1. Read all lines from input.txt
# 2. Count the total number of lines
# 3. Extract the first two lines
# 4. Save the result in output.txt

try:
    # Open the input.txt file in read mode ('r')
    # 'with' automatically closes the file after use
    with open("input.txt", "r") as f:

        # readlines() reads all lines from the file
        # and stores them in a list
        lines = f.readlines()

        # len() counts the number of elements in the list
        # Therefore, it gives the total number of lines
        count = len(lines)

        # [:2] extracts the first two elements from the list
        # So, first_two contains the first two lines
        first_two = lines[:2]

    # Open output.txt in write mode ('w')
    # If the file does not exist, Python creates it
    # If it already exists, its old contents are replaced
    with open("output.txt", "w") as out:

        # Write the total number of lines to output.txt
        # \n moves the cursor to the next line
        out.write(f"Total lines: {count}\n")

        # Write the first two lines into output.txt
        out.writelines(first_two)

    # Display a success message on the screen
    print("Done! Check output.txt")

# This error occurs when input.txt does not exist
except FileNotFoundError:

    # Display an error message
    print("Error: input.txt not found")
