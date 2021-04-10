# Imports Here
# This is the primary runner function that will get all your scripts running
import os
import discord
import tokens

from discord.ext import commands

def main():
    TOKEN = tokens.DISCORD_TOKEN
    '''
    client = discord.Client()
    @client.event
    async def on_ready():
        print("Discord bot running!")
    client.run(TOKEN)
    '''
    #bot = discord.Client()
    bot = commands.Bot(command_prefix='!')
    @bot.command(name='ping', pass_context = True)
    async def pong(ctx):
	    await ctx.send("pong!")
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
