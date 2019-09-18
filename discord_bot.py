import discord
import requests
from my_token import TOKEN
client = discord.Client()

INTERPRETER_URL = "http://localhost:5005/model/parse"

def interprete(message):
    data = f'{{"text":"{message}"}}'
    return requests.post(INTERPRETER_URL, data=data).json()

@client.event  
async def on_ready():  
    print('Bot ready :-)') 

@client.event
async def on_message(message):
    # On test si c'est le bot qui vient de parler
    # Dans ce cas, il ne va pas répéter ce que j'ai déjà dit
    if message.author == client.user:
        return
    try:
        r = interprete(message.content)
        if r["intent"]["name"]:
            return await message.channel.send(f'{message.author.mention} : analyse donne : {r["intent"]["name"]} avec une confiance de {r["intent"]["confidence"]}')
        else:
            return await message.channel.send(f'{message.author.mention} Je ne sais pas :(')
    except requests.exceptions.RequestException as e:
            return await message.channel.send(f"{message.author.mention} Aïe, j'ai une défaillance de cerveau :(")

client.run(TOKEN)
