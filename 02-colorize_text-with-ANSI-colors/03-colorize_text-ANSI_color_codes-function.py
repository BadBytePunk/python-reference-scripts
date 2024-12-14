# 03-colorize_text-ANSI_color_codes-function.py
# BadBytePunk
# 2024-12-13

#### ANSI COLOR CODES FUCTION SCRIPT ####

""" ++++ COLORIZE TEXT FUNCTION USING ANSI CODES ++++ """

# Function to Colorize Text Using ANSI Codes
def colorize(text, color):  # define a function named colorize
    """ Applies color to text using ANSI codes. This includes:

    Colors: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, and WHITE

    Reset code to prevent color or style propagation (RESET)

    Args:
        - text (str): The text to color.
        - color (str): The ANSI color code.

    Returns:
        - str: The colorized text.
    """
    # ANSI color codes dictionary
    colors = {
        # ANSI COLOR CODES
        'RESET': '\033[0m',       # reset color
        'BLACK': '\033[30m',      # black color
        'RED': '\033[91m',        # red color
        'GREEN': '\033[32m',      # green color
        'YELLOW': '\033[33m',     # yellow color
        'BLUE': '\033[34m',       # blue color
        'MAGENTA': '\033[35m',    # magenta color    
        'CYAN': '\033[36m',       # cyan color
        'WHITE': '\033[37m',      # white color       
        # ANSI COLOR STYLE CODES FOR BOLD & UNDERLINE
        'BOLD': '\033[1m',        # bold style
        'UNDERLINE': '\033[4m',   # underline style
    }
    return colors.get(color, colors['RESET']) + text + colors['RESET']  # retreives ANSI code for the given color
                                                                        # (or uses RESET if the color is not found) and
                                                                        # concatanates it with the text. The RESET code
                                                                        # to ensure the color does not propagate


""" ++++ APPLYING ANSI COLORS TO THE TEXT ++++ """
# Calls the solorize function and applies the 'COLOR" ti the text
print(colorize("Test color BLACK", 'BLACK')) 
print(colorize("Test color RED", 'RED'))
print(colorize("Test color GREEN", 'GREEN'))
print(colorize("Test color YELLOW", 'YELLOW'))
print(colorize("Test color BLUE", 'BLUE'))
print(colorize("Test color MAGENTA", 'MAGENTA'))
print(colorize("Test color CYAN", 'CYAN'))
print(colorize("Test color WHITE", 'WHITE'))
print(colorize("Test style BOLD", 'BOLD'))
print(colorize("Test style UNDERLINE", 'UNDERLINE'))


""" ++++ APPLYING BOLD AND COLOR TO THE TEXT USING ANSI CODE ++++ """
# Calls the colorize function, apply first the 'BOLD' style first to the text and
# then apply the 'COLOR' to the text.   
print(colorize(colorize("\nTest color BLACK and BOLD", 'BOLD'), 'BLACK')) 
print(colorize(colorize("Test color RED and BOLD", 'BOLD'), 'RED'))
print(colorize(colorize("Test color GREEN and BOLD", 'BOLD'), 'GREEN'))
print(colorize(colorize("Test color YELLOW and BOLD", 'BOLD'), 'YELLOW')) 
print(colorize(colorize("Test color BLUE and BOLD", 'BOLD'), 'BLUE'))
print(colorize(colorize("Test color MAGENTA and BOLD", 'BOLD'), 'MAGENTA'))
print(colorize(colorize("Test color CYAN and BOLD", 'BOLD'), 'CYAN'))
print(colorize(colorize("Test color WHITE and BOLD", 'BOLD'), 'WHITE')) 


""" ++++ APPLYING UNDERLINE AND COLOR TO THE TEXT USING ANSI CODE ++++ """
# Calls the colorize function, apply first the 'UNDERLINE' style first to the text and
# then apply the 'COLOR' to the text.
print(colorize(colorize("\nTest color BLACK and UNDERLINE", 'UNDERLINE'), 'BLACK'))
print(colorize(colorize("Test color RED and UNDERLINE", 'UNDERLINE'), 'RED'))
print(colorize(colorize("Test color GREEN and UNDERLINE", 'UNDERLINE'), 'GREEN'))
print(colorize(colorize("Test color YELLOW and UNDERLINE", 'BUNDERLINE'), 'YELLOW'))
print(colorize(colorize("Test color BLUE and BUNDERLINE", 'UNDERLINE'), 'BLUE'))
print(colorize(colorize("Test color MAGENTA and UNDERLINE", 'UNDERLINE'), 'MAGENTA'))
print(colorize(colorize("Test color CYAN and UNDERLINE", 'UNDERLINE'), 'CYAN'))
print(colorize(colorize("Test color WHITE and UNDERLINE", 'UNDERLINE'), 'WHITE'))


""" ++++ APPLYING UNDERLINE, BOLD AND COLOR TO THE TEXT USING ANSI CODE ++++ """
# Calls the colorize function, apply 'BOLD' first, then 'UNDERLINE', and finally
# 'COLOR' to the text.
print(colorize(colorize(colorize("\nTest color BLACK BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'BLACK'))
print(colorize(colorize(colorize("Test color RED BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'RED'))
print(colorize(colorize(colorize("Test color GREEN BOLD UNDERLINED", 'BOLD'), 'UNDERLINE'), 'GREEN'))
print(colorize(colorize(colorize("Test color YELLOW BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'YELLOW'))
print(colorize(colorize(colorize("Test color BLUE BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'BLUE'))
print(colorize(colorize(colorize("Test color MAGENTA BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'MAGENTA'))
print(colorize(colorize(colorize("Test color CYAN BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'CYAN'))
print(colorize(colorize(colorize("Test color WHITE BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'WHITE'))