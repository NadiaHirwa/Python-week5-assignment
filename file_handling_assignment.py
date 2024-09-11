# Step 1: File Creation and Writing to a File
try:
    # Creating a new text file and opening it in 'write' mode
    with open("my_file.txt", "w") as file:
        # Writing three lines of text, including strings and numbers
        file.write("Hello, this is the first line.\n")
        file.write("My name is Nadia Iradukunda Hirwa.\n")
        file.write("I'm 21 years old.\n")
    print("File created and written successfully.")

# Step 4: Error handling
except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")
except PermissionError as p_error:
    print(f"Permission Error: {p_error}")
finally:
    print("File creation process complete.")

# Step 2: Reading and Displaying File Content
try:
    # Opening the file in 'read' mode to display the contents
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nReading file content:")
        print(content)

# Step 4: Error handling
except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")
except PermissionError as p_error:
    print(f"Permission Error: {p_error}")
finally:
    print("File reading process complete.")

# Step 3: Appending Additional Text to the File
try:
    # Opening the file in 'append' mode to add more content
    with open("my_file.txt", "a") as file:
        # Appending three more lines of text
        file.write("Appending another line.\n")
        file.write("Learning file handling in Python.\n")
        file.write("This is the final line of text.\n")
    print("\nText appended successfully.")

# Step 4: Error handling
except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")
except PermissionError as p_error:
    print(f"Permission Error: {p_error}")
finally:
    print("File appending process complete.")

# Reading the final content of the file after appending
try:
    # Opening the file in 'read' mode again to display updated contents
    with open("my_file.txt", "r") as file:
        final_content = file.read()
        print("\nFinal content of the file after appending:")
        print(final_content)

# Step 4: Error handling
except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")
except PermissionError as p_error:
    print(f"Permission Error: {p_error}")
finally:
    print("Final reading process complete.")
