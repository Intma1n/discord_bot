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

good_words = ['хорошее', 'приятное', 'ободряющее', 'жизнеутверждающее']

thanks_str = 'спасибо, робот'

thanks_response = 'Да пошёл ты нахуй'

good_words_response = ['С вероятностью 50% ты завтра не проснешься']

wow_words = [' wow ', ' шош ', ' вов ', ]

media_ext = ['.jpg', '.png', '.jpeg', '.mp4', '.webm', 'mov']

wow_words_response = ["Я уже говорил, что ВоВ - говно?",
                      "Даже я знаю, что ВоВ - говно",
                      "В ВоВ играть - себя не уважать",
                      "Воверы - долбаёбы"]

zanyat_str = ' очень занят важными делами. Дела такой важности, что не представляется возможности общаться и прослушивать вас в голосовом канале.' \
             ' Попрошу дождаться, пока появится возможность закончить свои важные дела и самостоятельно подключиться или размутить микрофон.' \
             ' Спасибо за понимание'

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
    for key in users_dict_keys:
        lower_key = key.lower()
        if message.content.lower().startswith(key.lower() + ' занят'):
            await message.channel.send(users_dict[key] + ' ' + zanyat_str)

    if any(word in msg.lower() for word in wow_words):
        await message.channel.send(random.choice(wow_words_response))

    if any(word in msg.lower() for word in good_words):
        await message.channel.send(random.choice(good_words_response))

    if msg.startswith(str_len):
        msg_len = len(msg) - len(str_len)
        await message.channel.send('долбоеб высрал сообщение длиной ' + str(msg_len))

    if msg.lower().find(thanks_str) >= 0:
        await message.channel.send(thanks_response)

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

    # if msg.startswith('похуй'):
    #     msg_len = len(msg) - len(str_len)
    #     await message.channel.send('долбоеб высрал сообщение длиной ' + str(msg_len))


# keep_alive()
client.run(os.getenv('TOKEN'))
