'''
Para distinguir que bot es el que eventualmente tiene problemas,
coloreamos los outputs de cada bot con su color correspondiente

Discord: MAGENTA
Telegram: CYAN
Whatsapp: GREEN

Errores: RED

'''
from colorama import Fore
from datetime import datetime



colors = {
    "discord": Fore.MAGENTA,
    "telegram": Fore.CYAN,
    "whatsapp" : Fore.GREEN
}

def tprint(text):
    '''
    Telegram printer
    '''
    now = datetime.now()
    print(colors["telegram"] + now.strftime("[%Y/%m/%d | %H:%M:%S] ") + text + Fore.RESET)

def dprint(text):
    '''
    Discord printer
    '''
    now = datetime.now()
    print(colors["discord"] + now.strftime("[%Y/%m/%d | %H:%M:%S] ")  + text + Fore.RESET)

# ----------------------------------------------------------------------

def wprint(text):
    '''
    Whatsapp printer

    Funcionalidad para whatsapp quizas se implemente a futuro
    '''
    now = datetime.now()
    print(Fore.GREEN + now.strftime("[%Y/%m/%d | %H:%M:%S] ") + text + Fore.RESET)
