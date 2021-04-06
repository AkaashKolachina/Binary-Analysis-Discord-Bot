# TODO Build standard discord bot here
# For now this may be left empty
import os
import discord

TOKEN = ...
client = discord.Client()
@client.event
async def on_ready():
    print("Pong!")
client.run(TOKEN)

def main():
    print("Discord bot running!")

if __name__ == '__main__':
    main()
    