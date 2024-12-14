# 09-reading_file_line_by_line-read_mode-function.py
# BadBytePunk
# 2024-12-14

#### READING INTO A FILE ####

""" ++++ READING TEXT OF FILE LINE BY LINE ++++ """


""" *** Reading a file text line by line mean to process each line individually,
        and not printing each line once at the time in to the concole *** """

# Function to read a text file line by line
def read_file_line_by_line(file_path):  # define a function to read a text file
    """ Reads a text file line by line and returns a list of lines.
    
    Args:
        file_path (str): The path to the text file.

    Returns:
        list: A list of lines from the file.
    """
    # Open and read text of the file that is stock in a variable and return his content
    with open(file_path, 'r') as file:  # open a file in read mode
        """ 'r' : Read mode, opens a file for reading. """
        for line in file:
            print(line.strip()) # remove leading and tailing white space

file_path = "my_file-03.txt"
read_file_line_by_line(file_path)