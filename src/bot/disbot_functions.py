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
import os

RESULT_PATH = "src/results/"

async def read_symbols(ctx, executable, symbol):
    SYMBOL_PATH = "symbols.txt"
    has_symbol = False
    dis_script = 'src/scripts/dis.sh'
    call = subprocess.check_call("sh " + dis_script + " '%s'" % executable , shell=True)

    abs_path = RESULT_PATH + SYMBOL_PATH
    file = open(abs_path, "r")
    for line in file:
        line = line.rstrip("\n")
        if symbol in line:
            await ctx.send("`" + line + "`")
            has_symbol = True
    file.close()

    if not has_symbol:
        await ctx.send("Sorry that symbol was not in the table")


async def download(ctx):
    download_path = 'src/active-files/current_file'
    await ctx.message.attachments[0].save(fp = download_path)


async def get_rop_gadgets(ctx, executable):
    ROP_FILE_PATH = "rop_file.txt"
    rop_script = 'src/scripts/rop.sh'
    call = subprocess.check_call("sh " + rop_script + " '%s'" % executable , shell=True)

    abs_path = RESULT_PATH + ROP_FILE_PATH
    if os.path.isfile(abs_path) and os.path.getsize(abs_path) > 0:
        file = open(abs_path, "r")
        lines = file.readlines()
        await ctx.send(lines[0].strip())
        for i in range(2,len(lines)):
            if lines[i].strip():
                await ctx.send("```" + lines[i] + "```")
    else:
        await ctx.send("Gadgets not found")