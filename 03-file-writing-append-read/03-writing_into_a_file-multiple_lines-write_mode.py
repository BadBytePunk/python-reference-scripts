# 03-writing_into_a_file-multiple_line.py
# BadBytePunk
# 2024-12-14

####  WRITING INTO A FILE  ####

""" ++++  WRITING TEXT INTO A FILE USING MULTIPLE LINES USING WRITE MODE  ++++ """

# Open a file for writting or create one if it doesn't exist
with open('my_file-02.txt', 'w') as file:
    """ 'w' : Write mode and create new file """
    # Write some text in the file and add a new line
    file.write("This is the first line of text.\n") # write specific text. '\n' : add new line
    file.write("Here's the sencond line of text.\n") # write specific text. '\n' add new line
    file.write("The third is here.\n") # write specific text. '\n' add new line
    