# External Libraries
from os import getenv
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import ParseMode


# My libraries
from src.terminal_logger import tprint
from src.messages import help_cmd_telegram, loading_logic

async def build_and_send_discord_message(msg, discordBot):
    '''
    Crea y envia un mensaje a Discord
    '''
    channel_id = int(getenv("DISCORD_CHANNEL_ID"))
    channel = discordBot.get_channel(channel_id)
    if channel:
        await channel.send(f"{msg['from_user']['username']}: {msg['text']}")

def print_msg_on_console(message):
    message_author = message['from_user']
    if (message_author['first_name'] != None and message_author['last_name'] != None):
        tprint(message_author['first_name'] + ' ' + message_author['last_name'] + ': ' + update['message']['text'])
    else:
        tprint(message_author['username'] + ': ' + message['text'])

def load_telegram_logic(updater, discordBot):
    tprint(loading_logic)

    ### Definición de handlers
    # ------ Comandos y Logging de errores ------
    def cmd_help(update, context):
        # responder comando de /help en telegram
        update.message.reply_text(text=help_cmd_telegram, parse_mode=ParseMode.MARKDOWN_V2)

    def non_cmd_error(update, context):
        # Logear error causado por actualización
        tprint('Update ' + update.message + ' caused error ' + context.error)

    # ------ Funciones de Puente a Discord ------
    def read_and_resend_message(update, context):
        
        if (update['message']['chat']['id'] == int(getenv("TELEGRAM_CHAT_ID"))):
            ## Si es mensaje del grupo...
            # printeamos en consola el usuario y su mensaje
            print_msg_on_console(update['message'])

            # Y luego enviamos el mensaje de texto a discord
            discordBot.loop.create_task(build_and_send_discord_message(update['message'], discordBot))
            

        else: # alguien más está hablando con el bot? f
            pass
    
    def read_and_resend_photo(update, context):
        print(update)
        '''
            SEGUIR TRABAJANDO AQUÍ

            https://github.com/python-telegram-bot/v13.x-wiki/wiki/Code-snippets#working-with-files-and-media
        '''
        pass

    ## Registrando handlers para el funcionamiento del bot 

    # Contestar comandos en telegram
    updater.dispatcher.add_handler(CommandHandler("help", cmd_help))

    # Añadiendo Handlers para que funcione el puente a discord
    updater.dispatcher.add_handler(MessageHandler(Filters.text, read_and_resend_message))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, read_and_resend_photo))

    # log all errors
    updater.dispatcher.add_error_handler(non_cmd_error)

