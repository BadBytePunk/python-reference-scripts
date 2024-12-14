# 08-reading_file-read_mode-variable.py
# BadBytePunk
# 2024-12-14

#### READING INTO A FILE ####

""" ++++ READING TEXT OF FILE ++++ """

# Open and read text of the file that is stock in a variable and print to the console
with open('my_file-02.txt', 'r') as file:  # open a file named or create one if doen'st exist.
    """ 'r' : Read mode, opens a file for reading. """
    content = file.read()   # read the entire content of the file
    print(content)  # print the content to the console