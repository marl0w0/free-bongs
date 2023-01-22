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
        
#    if message.content.startswith(pref + "d"):
#        operation = message.content
#        params = [int(i) for i in operation.split() if i.isdigit()]
#        await message.channel.send(str(roll(params[0], params[1], params[2])))
    
    
    

client.run('OTQ3NzYwNDkxNzA5NzU1NDIy.Gq0p78.cvxQwKnhdjofv9TrFpI4-9vAldvUYAWsyTcAuU')
#OTQ3NzYwNDkxNzA5NzU1NDIy.Gq0p78.cvxQwKnhdjofv9TrFpI4-9vAldvUYAWsyTcAuU
