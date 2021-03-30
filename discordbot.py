from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_message(message):
    if message.content == '/start':
        message = random.randint(1,10)
        await message.channel.send(num)
    await message.channel.send('debug::') 

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)

