import discord
import os
from discord.ext import commands
import requests
import random
from keep_alive import keep_alive
from dotenv import load_dotenv
from discord.utils import get

load_dotenv('.env')

bot = commands.Bot(command_prefix='-')

client = discord.Client()

emojis = ['👍', '👎']

media_ext = ['.jpg', '.png', '.jpeg', '.mp4', '.webm', 'mov']

# @bot.command(pass_context=True)
# async def test(ctx, arg):
#     await ctx.send(arg)

users_dict = {
    "Я": "Я",
    'Никита': '@nikvas#7453',
    'Костя': '@Intmain#9879 ',
    'Илья': '@trGg#7086',
    'Сережа': '@Sell255#1099'
}

str_len = '?'


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    users_dict_keys = users_dict.keys()
    users_dict_values = users_dict.values()

    channel = client.get_channel(531850115741253633)
    if message.channel.id == 531850115741253633 or message.channel.id == 513810147450159134:
        if message.attachments:
            for emoji in emojis:
                await message.add_reaction(emoji)
        else:
            for ext in media_ext:
                if msg.endswith(ext):
                    for emoji in emojis:
                        await message.add_reaction(emoji)

# keep_alive()
client.run(os.getenv('TOKEN'))
