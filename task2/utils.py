from colorama import Fore, Style


def print_banner():
    """ print banner """


    baner = """
   _       _     _             _       ___       _   
  /_\  ___(_)___| |_ ___ _ __ | |_    / __\ ___ | |_ 
 //_\\/ __| / __| __/ _ \ '_ \| __|  /__\/// _ \| __|
/  _  \__ \ \__ \ ||  __/ | | | |_  / \/  \ (_) | |_ 
\_/ \_/___/_|___/\__\___|_| |_|\__| \_____/\___/ \__|
                                                     
    """
    print(Fore.GREEN + baner + Style.RESET_ALL)


def print_with_color(data: str, color: str = 'green'):
    """ 
    print word in text with color 

     - data: text string
     - color: 
       - green: color is green (by default)
       - yellow: color is yellow


     - FG color green
     - BS open (start) bold marker
     - BE close (end) bild marker
     - SR reset all styles  
    """

    # color case
    
    if color == 'yellow':
        print(Fore.YELLOW + data + Style.RESET_ALL)
    else:
        use_color = Fore.GREEN
        # parsing text string
        data = data.replace('FG', use_color)
        data = data.replace('BS', '\033[1m')
        data = data.replace('BE', '\033[0m')
        data = data.replace('SR', Style.RESET_ALL)
        print(data)

