# External libraries
from os import getenv

# My Libraries
from src.terminal_logger import dprint
from src.messages import help_cmd_telegram, loading_logic

def print_msg_on_console(message):
    if message.attachments != []: # Si hay attachment, probablemente tiene link
        for elem in message.attachments:
            dprint(f"{message.author.nick}: {elem.url}")
    else: # Si no hay attachment, probablemente es solo texto
        dprint(f"{message.author.nick}: {message.content}")

def build_and_send_telegram_message(tgBot, message):
    '''
    Crea y envia un mensaje a telegram
    '''
    if message.attachments != []: # Si hay attachment, probablemente tiene link
        for elem in message.attachments:
            tgBot.send_message(chat_id=getenv("TELEGRAM_CHAT_ID"), text=f"{message.author.nick}: {elem.url}")
    else: # Si no hay attachment, probablemente es solo texto
        tgBot.send_message(chat_id=getenv("TELEGRAM_CHAT_ID"), text=f"{message.author.nick}: {message.content}")

def load_discord_logic(client, telegramBot):

    dprint(loading_logic)



    @client.event
    async def on_ready():
        dprint('Sesión iniciada correctamente en discord como {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user: 
            return
        
        if message.channel.id == int(getenv("DISCORD_CHANNEL_ID")):
            # printear mensaje en consola
            print_msg_on_console(message)

            # construir y enviar mensaje a telegram
            build_and_send_telegram_message(telegramBot.bot, message)
            
    



