def process_file():
    filename = input("Enter the filename to read: ").strip()

    try:
        with open(filename, "r") as file:
            content = file.read()

        # Example modification: replace commas with newlines
        modified_content = content.replace(", ", "\n")

        # Create a new output filename
        output_filename = f"modified_{filename}"

        # Write the modified content (with commas replaced by newlines) to the new file
        with open(output_filename, "w") as file:
            file.write(modified_content)

        # Process lines: Add line numbers (excluding title/first line)
        def process_line(line, index):
            return f"{index}) {line.strip()}\n"

        # Open the modified file to process lines
        with open(output_filename, "r") as file:
            lines = file.readlines()

        # Open the file again to write the numbered lines, skipping the first line
        with open(output_filename, "w") as file:
            # First line (title) is written without numbering
            title_line = lines[0]
            file.write(title_line.strip() + "\n")

            # Now process the rest of the lines with numbers starting from 1
            for index, line in enumerate(lines[1:], start=1):  # Start from line 1
                file.write(process_line(line, index))

        print(f"Success! Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. Cannot read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
process_file()
