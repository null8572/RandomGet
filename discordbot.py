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

@bot.command()
async def start(ctx):
    await ctx.send('pong')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    message = random.randint(1,10)
    await message.channel.send(num)
    
    
bot.run(token)

