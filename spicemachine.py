import discord
import asyncio
import time
import sys

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} ENTERING GAMER MODE: NOW!')

@client.event
async def on_message(message):
    backreference = message.id
    emb = message.embeds
    att = message.attachments
    
    print('in {0.channel} {0.author}: {0.content}'.format(message))
    if ''.join(map(str, att)) != '' :
        print('emb {0.embeds} att {0.attachments}'.format(message))

    if message.author == client.user:
        return

    if message.content.startswith("CALL"):
        await message.channel.send("RESPONSE")
    if message.content == "[abort]":
        sys.exit(0)
    if message.content == "z!init sm":
        await message.guild.get_member(self.user.id).edit(nick="Spice Machine")
        
    
    
    

client.run('')
#add token
