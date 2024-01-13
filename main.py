import logging
import time

import discord

from utilities.bot import BasicDiscordBot

try:
    import config
except ModuleNotFoundError:
    # Check if the file exists
    # If it doesn't, copy the example file
    from os.path import exists
    if not exists("config.py"):
        import shutil
        shutil.copyfile("config.example.py", "config.py")
        print("Please edit your config file (config.py) and then restart the bot.")
        exit()
    else:
        print("Something went wrong importing the config file. Check your config file for any errors, then restart the bot.")
        exit()

intents = discord.Intents.default()
        
bot = BasicDiscordBot(command_prefix=config.PREFIX, intents=intents)

handler = logging.FileHandler(filename=f'logs/{int(time.time())} discord.log', encoding='utf-8', mode='w')

bot.run(config.TOKEN, log_handler=handler)