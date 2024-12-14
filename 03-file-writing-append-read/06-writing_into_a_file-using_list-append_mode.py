# 04-writing_into_a_file-using_list.py
# BadBytePunk
# 2024-12-14

####  WRITING INTO A FILE  ####

""" ++++  WRITING TEXT INTO A FILE USING A LIST APPEND MODE  ++++ """

# Create a list of line with text
lines = ["This is the fourth line.\n",
"This is the fifth line.\n"]

# Open a file for writting or create one if it doesn't exist
with open('my_file-03.txt', 'a') as file:  # open a file named or create one if doen'st exist.
    """ 'a' : Write mode and create new file """
    file.writelines(lines)