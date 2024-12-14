# 01-display_message-slow_print.py
# BadBytePunk
# 2024-12-13

#### DISPLAY MESSAGE WITH SLOW PRINT ####

import time # import time module

# Function for slow text printing animation
def slow_print(text):   # define slow print funciton

  for char in text: # loop iterates over each character in the input text string
    print(char, end='', flush=True) # print text to the console
    """ print(char) : Prints the character to the console.
        end='' : Prevents a newline character from being added after the character.
        flush=True : Forces the output to be displayed immediately, rather than waiting
                     for a full line to be printed.           
    """
    time.sleep(0.1)  # creating time delay between characters
  print()   # print a new line character to move hte cursor to the next line after all characters have been printed

slow_print_message = "Hello! You are now experiencing slow printing !!"
slow_print(slow_print_message)