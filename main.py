# External libraries
import logging
from time import sleep
from sys import exit
from os import getenv
from dotenv import load_dotenv
from discord import Client as discordClient
from telegram.ext import Updater
from threading import Thread


# My Libraries
from src.discordBot import load_discord_logic
from src.telegramBot import load_telegram_logic
from src.messages import missing_env_vars

def verify_env():
    '''
        Revisa que el .env tiene las variables correspondientes
    '''
    missing_variables = []

    if True: # esto para esconder indentado y achicar funcion en editor de código
        if not getenv('DISCORD_BOT_TOKEN'):
            missing_variables.append('DISCORD_BOT_TOKEN')

        if not getenv('TELEGRAM_BOT_TOKEN'):
            missing_variables.append('TELEGRAM_BOT_TOKEN')

        if not getenv('TELEGRAM_CHAT_ID'):
            missing_variables.append('TELEGRAM_CHAT_ID')

        if not getenv('DISCORD_CHANNEL_ID'):
            missing_variables.append('DISCORD_CHANNEL_ID')

    if len(missing_variables) == 0:
        return True
    else:
        print(missing_env_vars)
        [print(" - " + var) for var in missing_variables]
        return False

def main():
    # verificar que el .env está correcto
    load_dotenv()
    if not verify_env():
        return exit(1)
    
    # Cargar tokens
    ds_token = getenv('DISCORD_BOT_TOKEN')
    tg_token = getenv('TELEGRAM_BOT_TOKEN')
    
    # Cargando Bot de Discord
    discordBot = discordClient()
    
    # Cargando Bot de Telegram
    telegramBot = Updater(tg_token, use_context=True)
    
    # Inicializando logica y threads de cada bots
    load_discord_logic(discordBot, telegramBot)
    td = Thread(None, target=discordBot.run, args=(ds_token,), daemon=True)
    load_telegram_logic(telegramBot, discordBot)
    tt = Thread(None, target=telegramBot.start_polling, daemon=True)

    ## Iniciando ambos bots
    # Discord
    td.start()

    # Telegram
    tt.start() 

    try:
        '''
            Mantener thread principal funcionando
            hacer .join() de los otros threads bloquea el thread
            principal evitando que CTRL + C funcione.

            PENDIENTE: implementar algo más elegante que esto
            en el futuro
        '''
        while True:
            sleep(5)
            
    except KeyboardInterrupt: # CTRL + C para detener bots
        print("--- CTRL + C Detected ---")
        exit(0)

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
    main()
    