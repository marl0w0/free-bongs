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
