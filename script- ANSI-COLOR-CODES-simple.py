# script-ANSI-COLOR-CODES-simple.py
# BadBytePunk
# 2024-12-13

"""  ---  SCRIPT SIMPLE POUR AFFCIHER LES COULEURS ANSI  ---  """
# ANSI COLOR CODES
RESET = '\033[0m'       # reset to default color
BLACK = '\033[30m'      # black color
RED = '\033[91m'        # red color
GREEN = '\033[32m'      # green color
YELLOW = '\033[33m'     # yellow color
BLUE = '\033[34m'       # blue color
MAGENTA = '\033[35m'    # magenta color    
CYAN = '\033[36m'       # cyan color
WHITE = '\033[37m'      # white color
# ANSI CODES for BOLD & UNDERLINE
BOLD = '\033[1m'        # Bold text
UNDERLINE = '\033[4m'   # Underline text

ColorText = f"COLOR TEST : {BLACK}BLACK{RESET}, {RED}RED{RESET}, {GREEN}GREEN{RESET}, {YELLOW}YELLOW{RESET}, {BLUE}BLUE{RESET}, {MAGENTA}MAGENTA{RESET}, {CYAN}CYAN{RESET}, {WHITE}WHITE{RESET}" # ColorTextTest est une variable contenant une string
print(ColorText)    # appelle la fonction ColorText

CaracterStyle = f"\nCARACTER STYLE TEST: {BOLD}BOLD{RESET}, {UNDERLINE}UNDERLINE{RESET}" # CaracterStyleTest est une variable contenant une string
print(CaracterStyle)    # apelle la fonction CaracterStyle

# DISPLAY_ MESSAGE FUNCTION  
def display_message():
    WelcomeMessage = "\nTHIS IS A MESSAGE" # WelcomeMesssageTest est une variable contenant uen string
    print(WelcomeMessage)   # Affiche à l'écran le contenu de la variable WelcomeMessageTest
display_message() # Appelle la fonction display_TestMessage