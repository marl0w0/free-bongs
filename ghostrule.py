import discord
import asyncio

async def ghost(x):
    await asyncio.sleep(30)
    print("ghosting")
    await x.delete()
