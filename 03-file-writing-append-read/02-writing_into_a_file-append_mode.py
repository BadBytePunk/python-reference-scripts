# 02-writing_into_a_file-append_mode.py
# BadBytePunk
# 2024-12-14

####  WRITING INTO A FILE  ####

""" ++++  ADDING TEXT INTO A FILE USING APPEND MODE  ++++ """

# Open a file for writting or create one if it doesn't exist
with open('my_file-01.txt', 'a') as file:  # open a file named or create one if doen'st exist.
    """ 'a' : Append mode, adds content to he end of a existing file """
    # Write some text in the file
    file.write("New line of text has been added.\n")   # add and write a new line of text into the file 'my_file-01.txt'