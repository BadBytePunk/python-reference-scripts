# 01-writing_into_a_file-write_mode.py
# BadBytePunk
# 2024-12-14

####  WRITING INTO A FILE  ####

""" ++++  WRITING TEXT INTO A FILE USING WRITE MODE  ++++ """
# Open a file for writting or create one if it doesn't exist
with open('my_file-01.txt', 'w') as file:  # open a file named or create one if doen'st exist.
    """ 'w' : Write mode and create new file """
    # Write some text in the file
    file.write("This is a line of text.\n") # write specific text.