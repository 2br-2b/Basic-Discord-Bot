import logging
import time

import discord

import config
from utilities.bot import BasicDiscordBot

intents = discord.Intents.default()
        
bot = BasicDiscordBot(command_prefix=config.PREFIX, intents=intents)

handler = logging.FileHandler(filename=f'logs/{int(time.time())} discord.log', encoding='utf-8', mode='w')

bot.run(config.TOKEN, log_handler=handler)