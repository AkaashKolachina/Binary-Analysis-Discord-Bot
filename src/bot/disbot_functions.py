'''
    SIGPwny Binary Analysis Discord Bot
    Created by Akaash K.
'''

# TODO Put all your FUNCTIONS for the discord bot in here
# That means everything related to actual functionallity goes in here
# We will eventually make a central discord bot that utilizes other bots,
# You will be able to add your bot just by adding this python file to the central bot.
import subprocess
import sys
import discord

SCRIPT_PATH = ""


async def read_symbols(ctx, executable, symbol):
    SYMBOL_PATH= "symbols.txt"
    has_symbol = False
    call = subprocess.check_call("sh /Users/akaashkolachina/UIUC2020/Binary-Analysis-Discord-Bot/src/scripts/dis.sh '%s'" % executable , shell=True)

    abs_path = SCRIPT_PATH + SYMBOL_PATH
    file = open(abs_path, "r")
    for line in file:
        line = line.rstrip("\n")
        if symbol in line:
            # TODO: Replace with discord send
            await ctx.send(line.replace('_','\_'))
            has_symbol = True
    file.close()

    if not has_symbol:
        # TODO: Replace with discord send
        await ctx.send("Sorry that symbol was not in the table")


async def download(ctx):
    download_path = '/Users/akaashkolachina/UIUC2020/Binary-Analysis-Discord-Bot/src/test-files/current_file'
    await ctx.message.attachments[0].save(fp = download_path)