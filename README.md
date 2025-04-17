# File Read Write Program – Week 4 Python Assignment

## Assignment Overview

This Week 4 Python assignment demonstrates how to work with file input/output and handle exceptions in Python. It includes two main components:

1. **File Read & Write**
   - Reads content from an existing text file (`input_file.txt`)
   - Modifies the content (e.g., converts it to uppercase)
   - Writes the modified content to a new file (`output_file.txt`)

2. **Error Handling**
   - Prompts the user to enter a filename
   - Handles errors gracefully if the file does not exist or cannot be read

## Skills Practiced

- File reading and writing operations in Python
- Using `try`, `except`, and exception-specific handling
- Writing robust code that handles unexpected issues

## How to Run the Code

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/file-read-write-program-wk4-python.git
cd file-read-write-program-wk4-python
```
2. Make sure you have an input_file.txt file in the same folder with sample content.

3. Run the script in your terminal:
python file_read_write.py


**Files Included**
- file_read_write.py – Main script for reading, modifying, and writing file content
- input_file.txt – Sample input file with text to be modified
- output_file.txt – New file created with modified content
- README.md – Project documentation

**Expected Output**

After running the script:
- The content of input_file.txt will be read
- It will be modified (e.g., converted to uppercase)
- The modified content will be saved in output_file.txt
- If the specified file is missing or inaccessible, a user-friendly error message will be displayed

## Possible Errors and How to Fix Them

- **FileNotFoundError**: Happens if the input file name is wrong or doesn’t exist. Make sure `input_file.txt` is present in the same folder or enter a correct file name.
- **PermissionError**: You may not have permission to access or write to the file. Try running your script in a folder where you have full access.
- **Other Exceptions**: If something else goes wrong, the program will show a message with the specific error.

Always double-check the file name you enter and make sure it’s in the same directory as the script.
