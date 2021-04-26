# Imports Here
# This is the primary runner function that will get all your scripts running
import os
import discord
import tokens

from discord.ext import commands
from bot import disbot_functions as df

def main():
    TOKEN = tokens.DISCORD_TOKEN

    bot = commands.Bot(command_prefix='!')
    @bot.command(name='ping', pass_context = True)
    async def pong(ctx):
	    await ctx.send("pong!")
    
    '''
    @bot.command(name = 'download', pass_context = True)
    async def download(ctx):
        download_path = '/Users/akaashkolachina/UIUC2020/Binary-Analysis-Discord-Bot/src/test-files/current_file'
        await ctx.message.attachments[0].save(fp = download_path)
    '''
    @bot.command(name = 'symbol_table', pass_context = True)
    async def find_symbol_entry(ctx, symbol):
        if ctx.message.attachments:
            await df.download(ctx)
        # You should prob move this out of the test folder
        executable = '/Users/akaashkolachina/UIUC2020/Binary-Analysis-Discord-Bot/src/test-files/current_file'
        await df.read_symbols(ctx,executable,symbol)

    bot.run(TOKEN)

if __name__ == '__main__':
    main()
