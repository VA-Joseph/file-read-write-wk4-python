# File Read & Write with Exception Handling
# PLP Week 4 Python Assignment

def read_and_modify_file(input_filename, output_filename):
    try:
        # Try to open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify content (convert to uppercase)
        modified_content = content.upper()

        # Write modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File '{input_filename}' was read successfully.")
        print(f"Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied while accessing '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Ask the user for the input file name
user_input = input("Enter the name of the file to read: ")
output_file = "output_file.txt"

# Call the function
read_and_modify_file(user_input, output_file)
