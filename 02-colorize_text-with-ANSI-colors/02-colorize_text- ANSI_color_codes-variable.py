# 02-colorize_text-ANSI_color_codes-variable.py
# BadBytePunk
# 2024-12-13

#### ANSI COLOR CODES SIMPLE SCRIPT ####

""" ++++ ANSI COLOR AND COLOR STYLE CODES ++++ """

# ANSI COLOR CODES
RESET = '\033[0m'       # reset color
BLACK = '\033[30m'      # black color
RED = '\033[91m'        # red color
GREEN = '\033[32m'      # green color
YELLOW = '\033[33m'     # yellow color
BLUE = '\033[34m'       # blue color
MAGENTA = '\033[35m'    # magenta color    
CYAN = '\033[36m'       # cyan color
WHITE = '\033[37m'      # white color
# ANSI COLOR STYLE CODES FOR BOLD & UNDERLINE
BOLD = '\033[1m'        # bold style
UNDERLINE = '\033[4m'   # underline style

""" ++++ DISPLAY TEXT USING MULTIPLE ANSI COLORS AND STYLE IN THE SAME STRING (f-string) ++++ """
# Display text value and his ANSI color value
# Using f-string (format string) to embed expressions
# inside string litterals using cuirly brace {}
ColorText = f"""COLOR TEST : {BLACK}BLACK{RESET}, {RED}RED{RESET}, {GREEN}GREEN{RESET}, {YELLOW}YELLOW{RESET}, {BLUE}BLUE{RESET}, {MAGENTA}MAGENTA{RESET}, {CYAN}CYAN{RESET}, {WHITE}WHITE{RESET},
{BOLD}BOLD{RESET}, {UNDERLINE}UNDERLINE{RESET}""" # declare ColorText variable and assing string value with ANSI color code for each word including BOLD & UNDERLINE.
print(ColorText)    # print function to display the value of the ColorText variable on the console



