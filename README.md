# PLP_Python_Week4_Assignment
This repository provides answers to the PLP week 4 Python assignment:
                File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
                Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

The code performs the following:

1. Requests the user to enter a filename to read.
   In this case, the progLang.txt file is used.
   
2. Replaces the commas with a new line.
  
3. Creates a new output file with the prefix "modified_"

4. Opens the modified file and enumerates the list from line 2, excluding the title line.

5. Performs exception handling and captures likely errors such as:
       a) The file isn't found.
       b) Permission to read the file is denied.
       c) An unexpected error occurs.

