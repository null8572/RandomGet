import os
import traceback
import discord

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_message(message):
    if message.content == '/start':
        message = random.randint(1,10)
        await message.channel.send(num)
    await message.channel.send('debug::') 


    
client.run(token)    
