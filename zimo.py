#import spicemachine.py
import ghostrule
import atomicheart
import discord
import asyncio
import time
import sys

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

bmode = 0
grtarget = 0

@client.event
async def on_ready():
    print(f'{client.user} ENTERING GAMER MODE: NOW!')

@client.event
async def on_message(message):
    backreference = message.id
    emb = message.embeds
    att = message.attachments
    op = ""
    global bmode
    global grtarget
    
    print('in {0.channel} {0.author}: {0.content}'.format(message))
    if ''.join(map(str, att)) != '' :
        print('emb {0.embeds} att {0.attachments}'.format(message))

    if message.author == client.user:
        return

    if message.content.startswith("CALL"):
        await message.channel.send("RESPONSE")
    if message.content == "z!close":
        await message.guild.get_member(client.user.id).edit(nick="")
        sys.exit(0)
    if message.content == "z!de-initialize":
        bmode=0
        await message.guild.get_member(client.user.id).edit(nick="")
    if message.content == "z!init sm":
        await message.guild.get_member(client.id).edit(nick="Spice Machine")
        bmode=1
        print("spice shipping")
    if message.content == "z!init d2":
        await message.guild.get_member(client.user.id).edit(nick="DECO*27")
        bmode=2
        grtarget = message.author
        print("ghost rule")
    if message.content == "z!init at":
        await message.guild.get_member(client.user.id).edit(nick="Atomic Heart")
        bmode=3
        print("atomic heart")
    if bmode == 2:
        if message.author == grtarget:
            if message.content.startswith("-x") != True:
                print("activating ghost")
                await ghostrule.ghost(message)
    if bmode == 3:
        if message.content.startswith("z!cgrab"):
            await atomicheart.cgrab(message)
        if message.content == "z!ATclear":
            opfile = open("output.txt", "w")
            opfile.write("")
            opfile.close()
        
    
    
    

client.run('OTUxMDIyMDY3OTY3NDU5MzI5.YihaUg.49ojy8B6OLoa6V0542XkHO1DPhs')
#add token
