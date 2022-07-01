# PDE Bot
## Version 0.0.0
Puente para chats de discord, telegram y whatsapp (funcionalidad para whatsapp aún pendiente). Hice este mini proyecto para ejercitar mis conocimientos de python y aprender sobre el funcionamiento de las APIs de Telegram y Discord. 

## Funcionalidades actuales
- Puente Telegram <---> Discord
    * Envio de texto funcional
    * Envio de imagenes funciona solo en dirección Discord ---> Telegram

- Logs en consola son coloreados por plataforma
    * Errores/Logging por defecto de Python se imprime en el color predeterminado de la consola.
    * Mensajes originados en Telegram se imprimen en azul
    * Mensajes originados en Discord se imprimen en Morado

## Descripción de la implementación
En pocas palabras, invoco dos instancias (una del cliente de Discord.py y otra del cliente de python-telegram-bot) y las dejo funcionando cada una en su propio thread. Cuando una instancia recibe un mensaje, imprime en consola el mensaje y luego invoca metodos de la otra instancia para enviar el mensaje a la otra plataforma.

## Dependencias
Output de ```pip list```

```bash
colorama              0.4.5
discord.py            1.7.3
python-dotenv         0.20.0
python-telegram-bot   13.12
```
## Para iniciar el bot
En carpeta raiz, crear archivo ```.env``` con las siguientes variables:
- DISCORD_BOT_TOKEN -> token del bot
- TELEGRAM_BOT_TOKEN -> token del bot
- TELEGRAM_CHAT_ID -> id del chat de Telegram al que se le hará puente
- DISCORD_CHANNEL_ID -> id del canal del servidor de Discord al que se le hará puente

Luego, crear dentro de la carpeta ```src/``` el archivo ```messages.py``` que contendrá strings utilizados por el bot. Plantilla para este archivo detallada al final de este README.

Después de instalar dependencias, inciar bot con ```python main.py```





### Plantilla src/messages.py 
```python
'''
    Mensajes del Bot
'''

missing_env_vars = "Missing enviroment variables:"

help_cmd_telegram = "this bot is for private use. Ask for bot host for help"

loading_logic = "Loading Logic..."
```