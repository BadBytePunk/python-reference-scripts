# script-ANSI-COLOR-CODES-simple.py
# BadBytePunk
# 2024-12-13


""" ++++ FONCTION POUR GÉRER LES CODES DE COULEURS ANSI ++++ """
# COLORIZE FUNCTION
def colorize(text, color):
    """ Applique de la couleur au texte en utilisant les codes ANSI.
        Ce qui comprend: 
            - les couleurs : BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN et WHITE
            - code d'évitement de propagation de couleurs ou de style RESET
         
         Args : text (str): Le texte à colorier.
                color (str): Le code de couleur ANSI.
                
        Returns: str: Le texte colorisé.
    """
    # ANSI COLOR CODE
    colors = {
        # ANSI COLOR CODES
        'RESET': '\033[0m',       # reset to default color
        'BLACK': '\033[30m',      # black color
        'RED': '\033[91m',        # red color
        'GREEN': '\033[32m',      # green color
        'YELLOW': '\033[33m',     # yellow color
        'BLUE': '\033[34m',       # blue color
        'MAGENTA': '\033[35m',    # magenta color    
        'CYAN': '\033[36m',       # cyan color
        'WHITE': '\033[37m',      # white color
        # ANSI CODES for BOLD & UNDERLINE
        'RESET': '\033[0m',       # reset to default color
        'BOLD': '\033[1m',        # Bold text
        'UNDERLINE': '\033[4m',   # Underline text
    }
    return colors.get(color, colors['RESET']) + text + colors['RESET']


# COLORIZE TEXT OUPUT
print(colorize("Test color BLACK", 'BLACK'))    # appelle la fonction colorize et applique la couleur BLACK
print(colorize("Test color RED", 'RED'))    # appelle la fonction colorize et applique la couleur RED
print(colorize("Test color GREEN", 'GREEN'))    # appelle la fonction colorize et applique la couleur GREEN
print(colorize("Test color YELLOW", 'YELLOW'))  # appelle la fonction colorize et applique la couleur YELLOW
print(colorize("Test color BLUE", 'BLUE'))  # appelle la fonction colorize et applique la couleur BLUE
print(colorize("Test color MAGENTA", 'MAGENTA'))    # appelle la fonction colorize et applique la couleur MAGENTA
print(colorize("Test color CYAN", 'CYAN'))  # appelle la fonction colorize et applique la couleur CYAN
print(colorize("Test color WHITE", 'WHITE'))    # appelle la fonction colorize et applique la couleur WHITE
print(colorize("Test style BOLD", 'BOLD'))    # appelle la fonction colorize et applique le style BOLD
print(colorize("Test style UNDERLINE", 'UNDERLINE'))    # appelle la fonction colorize et applique la couleur GREEN

# COLORIZE TEXT WITH BOLD STYLING, THEN CONCATENATE THE OUTPUT
print(colorize(colorize("\nTest color BLACK and BOLD", 'BOLD'), 'BLACK'))
print(colorize(colorize("Test color RED and BOLD", 'BOLD'), 'RED'))
print(colorize(colorize("Test color GREEN and BOLD", 'BOLD'), 'GREEN'))
print(colorize(colorize("Test color YELLOW and BOLD", 'BOLD'), 'YELLOW'))
print(colorize(colorize("Test color BLUE and BOLD", 'BOLD'), 'BLUE'))
print(colorize(colorize("Test color MAGENTA and BOLD", 'BOLD'), 'MAGENTA'))
print(colorize(colorize("Test color CYAN and BOLD", 'BOLD'), 'CYAN'))
print(colorize(colorize("Test color WHITE and BOLD", 'BOLD'), 'WHITE'))

# COLORIZE TEXT WITH UNDERLINE STYLING, THEN CONCATENATE THE OUTPUT
print(colorize(colorize("\nTest color BLACK and UNDERLINE", 'UNDERLINE'), 'BLACK'))
print(colorize(colorize("Test color RED and UNDERLINE", 'UNDERLINE'), 'RED'))
print(colorize(colorize("Test color GREEN and UNDERLINE", 'UNDERLINE'), 'GREEN'))
print(colorize(colorize("Test color YELLOW and UNDERLINE", 'BUNDERLINE'), 'YELLOW'))
print(colorize(colorize("Test color BLUE and BUNDERLINE", 'UNDERLINE'), 'BLUE'))
print(colorize(colorize("Test color MAGENTA and UNDERLINE", 'UNDERLINE'), 'MAGENTA'))
print(colorize(colorize("Test color CYAN and UNDERLINE", 'UNDERLINE'), 'CYAN'))
print(colorize(colorize("Test color WHITE and UNDERLINE", 'UNDERLINE'), 'WHITE'))

# COLORIZE TEXT WITH BOLD AND UNDERLINE STYLING, THEN CONCATENATE THE OUTPUT
print(colorize(colorize(colorize("\nTest color BLACK BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'BLACK'))
print(colorize(colorize(colorize("Test color RED BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'RED'))
print(colorize(colorize(colorize("Test color GREEN BOLD UNDERLINED", 'BOLD'), 'UNDERLINE'), 'GREEN'))
print(colorize(colorize(colorize("Test color YELLOW BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'YELLOW'))
print(colorize(colorize(colorize("Test color BLUE BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'BLUE'))
print(colorize(colorize(colorize("Test color MAGENTA BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'MAGENTA'))
print(colorize(colorize(colorize("Test color CYAN BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'CYAN'))
print(colorize(colorize(colorize("Test color WHITE BOLD UNDERLINE", 'BOLD'), 'UNDERLINE'), 'WHITE'))