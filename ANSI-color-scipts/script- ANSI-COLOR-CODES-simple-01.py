# script-ANSI-COLOR-CODES-simple-01.py
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

""" ++++ DISPLAY TEXT USING ANSI COLORS AND STYLE FOR EACH STRING (f-string) ++++ """
# Display strings with is color whit print function
# Using f-string (format string) to embed expressions
# inside string litterals using cuirly brace {}
print(f"{BLACK}COLOR BLACK{RESET}")
print(f"{RED}COLOR RED{RESET}")
print(f"{GREEN}COLOR GREEN{RESET}")
print(f"{YELLOW}COLOR YELLOW{RESET}")
print(f"{BLUE}COLOR BLUE{RESET}")
print(f"{MAGENTA}COLOR MAGENTA{RESET}")
print(f"{CYAN}COLOR CYAN{RESET}")
print(f"{WHITE}COLOR WHITE{RESET}")
print(f"{BOLD}COLOR BOLD{RESET}")
print(f"{UNDERLINE}COLOR UNDERLINE{RESET}")



