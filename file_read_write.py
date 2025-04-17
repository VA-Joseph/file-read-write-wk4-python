filename = input("Enter the filename to read: ")

try:
    # Try to open the user-specified file in read mode
    with open(filename, 'r') as file:
        print("File content:")
        print(file.read())  # Display the file content

except FileNotFoundError:
    # Handle the case where the file doesn't exist
    print(f"The file {filename} does not exist.")
except IOError:
    # Handle other input/output errors (e.g., permission issues)
    print(f"An error occurred while reading the file {filename}.")
except Exception as e:
    # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")
