# 04-writing_into_a_file-using_list.py
# BadBytePunk
# 2024-12-14

####  WRITING INTO A FILE  ####

""" ++++  WRITING TEXT INTO A FILE USING A LIST WRITE MODE  ++++ """

# Create a list of line with text
lines = ["This is the first line.\n",
"This is the second line.\n",
"This is the third line.\n"]

# Open a file for writting or create one if it doesn't exist
with open('my_file-03.txt', 'w') as file:  # open a file named or create one if doen'st exist.
    """ 'w' : Write mode and create new file """
    file.writelines(lines)