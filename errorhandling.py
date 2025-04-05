def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (for example, converting all text to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File has been successfully modified and written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except IOError:
        print("Error: An issue occurred while reading or writing the file.")

# Example usage:
input_filename = "input.txt"
output_filename = "output.txt"
read_and_modify_file(input_filename, output_filename)

def handle_file_error():
    filename = input("Please enter the filename you want to read: ")
    
    try:
        # Attempt to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print("File content successfully read.")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: The file {filename} cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the error handling function
handle_file_error()

