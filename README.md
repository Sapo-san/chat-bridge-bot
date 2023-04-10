# PDE Bot
## Version 0.1.0
Puente para chats de Discord y Telegram. Hice este mini proyecto para ejercitar mis conocimientos de python y aprender sobre el funcionamiento de las APIs de Telegram y Discord. 

## Funcionalidades actuales
- Puente Telegram <---> Discord
    * Envio de texto funcional
    * Envio de imágenes
        * Discord -> Telegram: Envia URL de la imagen (Telegram carga la preview)
        * Telegram -> Discord: Envia la imagen
    * Envio de videos:
        * Discord -> Telegram: Envia URL de del video (Telegram carga la preview)
        * Telegram -> Discord: Envia el video
    * Envio de stickers:
        * Telegram -> Discord: Envia el sticker como una imagen
    * Envio de mensajes de voz:
        * Telegram -> Discord: Envia el mensaje como un archivo de voz
    * Envio de archivos\*:
        * Discord -> Telegram: Manda la url del archivo.


- Logs en consola son coloreados por plataforma
    * Errores/Logging por defecto de Python se imprime en el color predeterminado de la consola.
    * Mensajes originados en Telegram se imprimen en azul
    * Mensajes originados en Discord se imprimen en Morado

## Funcionalidades planeadas (sin fecha)
- Puente a chat de Whatsapp

## Descripción de la implementación
En pocas palabras, invoco dos instancias (una del cliente de Discord.py y otra del cliente de python-telegram-bot) y las dejo funcionando cada una en su propio thread. Cuando una instancia recibe un mensaje, imprime en consola el mensaje y luego invoca metodos de la otra instancia para enviar el mensaje a la otra plataforma.

## Dependencias
Programado Python 3.10

**Output de ```pip list```**

```bash
colorama              0.4.5
discord.py            1.7.3
python-dotenv         0.20.0
python-telegram-bot   13.13
```
## Para iniciar el bot
En carpeta raiz, crear archivo ```.env``` con las siguientes variables:
- DISCORD_BOT_TOKEN -> token del bot (Ver en [Discord Developer Portal](https://discord.com/developers/applications/))
- TELEGRAM_BOT_TOKEN -> token del bot (Hablar con Telegram Bot Father)
- TELEGRAM_CHAT_ID -> id del chat de Telegram al que se le hará puente (Como obtener ID del chat [aquí](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id))
- DISCORD_CHANNEL_ID -> id del canal del servidor de Discord al que se le hará puente

Luego, crear dentro de la carpeta ```src/``` el archivo ```messages.py``` que contendrá strings utilizados por el bot. Plantilla para este archivo detallada al final de este README.

Después de instalar dependencias, inciar bot con ```python main.py```


### Plantilla src/messages.py 
```python
'''
    Bot Messages
'''

missing_env_vars = "Missing enviroment vars: "

help_cmd_telegram = "Bot is for private use, ask deployer for help."

loading_logic = "Loading bot logic..."

sending_image_1 = "sent an image"

sending_image_2 = "with caption"

sending_sticker = "sent a sticker"

sending_video_1 = "sent a video"

sending_video_2 = "with caption"

sending_voice = "sent a voice message"
```