# 09-reading_file-read_mode-function.py
# BadBytePunk
# 2024-12-14

#### READING INTO A FILE ####

""" ++++ READING TEXT OF FILE LINE BY LINE ++++ """

# Define a function to read a text file
def read_file(file_name):
    """Reads a text file and returns its content.

    Args:
        file_name: The name of the file to read.

    Returns:
        The content of the file as a string.
    """
    # Open and read text of the file that is stock in a variable and return his content
    with open(file_name, 'r') as file:  # open a file in read mode
        """ 'r' : Read mode, opens a file for reading. """
        content = file.read()   # read the entire content of the file
        return content # Return the content

file_name = 'my_file-03.txt'    # specify the file path
file_content = read_file(file_name) # call the function to read the file and stor the content
print(file_content) # print the content to the console