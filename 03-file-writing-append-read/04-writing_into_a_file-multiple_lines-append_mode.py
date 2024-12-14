# 03-writing_into_a_file-multiple_line.py
# BadBytePunk
# 2024-12-14

####  WRITING INTO A FILE  ####

""" ++++  WRITING TEXT INTO A FILE USING MULTIPLE LINES WITH APPEND MODE  ++++ """

# Open a file for writting or create one if it doesn't exist
with open('my_file-02.txt', 'a') as file:
    """ 'w' : Write mode and create new file """
    # Write some text in the file and add a new line
    file.write("This is the fourth line of text.\n") # write specific text. '\n' : add new line
    file.write("Here's the fifth line of text.\n") # write specific text. '\n' add new line
    