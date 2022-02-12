import discord 
import os
from keep_alive import keep_alive
from discord.exe import commands

Monster = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)



Monster.author_id = ENTER_YOUR_ID
#enter your discord id here

@Monster.event
async def on_ready():
  game = discord.Game(f'!help')
  await Monster.change_presence(status=discord.Status, activity=game)
print(f'Im signed into {Monster.user}')
#this changes the discord bots status to a custom one

@Monster.command()
async def ping(ctx):
 await ctx.send('pong!') 
#a simple command that shows the bot is online

@Monster.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")

@Monster.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member):
    try:
        await member.ban(reason=None)
        await ctx.send("banned "+member.mention) #simple ban command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")


@Monster.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@Monster.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")




keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("TOKEN")
#this pulles your token from .env
Monster.run(bot_token)
#runs the bot
