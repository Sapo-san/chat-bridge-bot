# External Libraries
from os import getenv
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import ParseMode
from io import BytesIO
from discord import File


# My libraries
from src.terminal_logger import tprint
import src.messages as m

async def build_and_send_discord_message(msg, discordBot):
    '''
    Crea y envia un mensaje a Discord
    '''
    channel_id = int(getenv("DISCORD_CHANNEL_ID"))
    channel = discordBot.get_channel(channel_id)
    if channel:
        await channel.send(f"{msg['from_user']['username']}: {msg['text']}")

async def send_discord_image(author, caption, img, discordBot):
    '''
    Envia una imagen a Discord
    '''
    # Procesar imagen
    processed_img = File(img, "image_from_telegram.png")

    # Enviarla al canal
    channel_id = int(getenv("DISCORD_CHANNEL_ID"))
    channel = discordBot.get_channel(channel_id)

    if caption == None:
        caption = ""

    if channel:
        await channel.send(f"{author}: {caption}", file=processed_img)


def load_telegram_logic(updater, discordBot):
    tprint(m.loading_logic)

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
            message_author = update['message']['from_user']
            tprint(message_author['username'] + ': ' + update['message']['text'])

            # Y luego enviamos la imagen a discord
            discordBot.loop.create_task(build_and_send_discord_message(update['message'], discordBot))
            

        else: # alguien más está hablando con el bot? f
            pass
    
    def read_and_resend_photo(update, context):
        img_file = context.bot.get_file(update.message.photo[-1].file_id)
        byte_img =  BytesIO(img_file.download_as_bytearray())

        photo_caption = update['message']['caption']
        message_author = update['message']['from_user']['username']

        # printeamos en consola el usuario y su mensaje
        if photo_caption != None:
            tprint(f'{message_author} {m.sending_image_1} (ID:{update.message.photo[-1].file_id}) {m.sending_image_2} {photo_caption}')
        else:
            tprint(f'{message_author} {m.sending_image_1} (ID:{update.message.photo[-1].file_id})')

        discordBot.loop.create_task(send_discord_image(message_author, photo_caption, byte_img, discordBot))


    ## Registrando handlers para el funcionamiento del bot 

    # Contestar comandos en telegram
    updater.dispatcher.add_handler(CommandHandler("help", cmd_help))

    # Añadiendo Handlers para que funcione el puente a discord
    updater.dispatcher.add_handler(MessageHandler(Filters.text, read_and_resend_message))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, read_and_resend_photo))

    # log all errors
    updater.dispatcher.add_error_handler(non_cmd_error)

