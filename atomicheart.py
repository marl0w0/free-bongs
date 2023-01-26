from datetime import datetime
import asyncio
import discord

async def cgrab(message):
    ofile = open("output.txt", "a", encoding="utf-8")
    print("beginning copy")
    await message.channel.send("beginning clone")
    async for x in message.channel.history(limit=None, oldest_first=True):
        ofile.write(f"in {x.channel} at {x.created_at} {x.author}: {x.content}\n")
        if ''.join(map(str, x.attachments)) != '':
            ofile.write(f"{x.embeds} {x.attachments}")
    print("snow crashed")
    await message.channel.send("clone completed")
    ofile.close()

async def wordScan(params, message):
    atime = datetime.strptime(params[1],"%d/%m/%Y")
    for ch in message.guild.channels:
        if str(type(ch)) == "<class 'discord.channel.TextChannel'>":
            print(ch.name)
            try:
                async for mes in ch.history(limit=None, after=atime):
                    if params[0] in mes.content.lower():
                        await message.channel.send(mes.jump_url + "\n" + mes.content)
            except:
                print("ERROR on "+ ch.name)
            if ch.threads != []:
                for thr in ch.threads:
                    print(thr.name)
                    try:
                        async for mes in thr.history(limit=None, after=atime):
                            if params[0] in mes.content.lower():
                                await message.channel.send(discord.utils.escape_mentions(mes.jump_url + "\n" + mes.content))
                    except:
                        print("ERROR on "+ thr.name)

async def clearbot(message, user):
    async for mes in message.channel.history(limit=None):
        if mes.author == user:
            await mes.delete()
