# 07-reading_file-read_mode.py
# BadBytePunk
# 2024-12-14

#### READING INTO A FILE ####

""" ++++ READING TEXT OF FILE ++++ """

# Open, read and print text of the file to the console
with open('my_file-01.txt', 'r') as file:  # open the file in read mode
    """ 'r' : Read mode, opens a file for reading. """
    print(file.read())  # print the entire content to the console