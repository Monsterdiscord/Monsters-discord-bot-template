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


@Monster.command()
async def credits(ctx):
    embed=discord.Embed(title="**======== *Your_bots_name Credits* ========**", description=f"""
                  Developer: 

                  Sub-Developer:
                  

                  """, color=0xf20202)
    embed.set_footer(text="Template made by Monstie#6632")
    await ctx.send(embed=embed)




keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("TOKEN")
#this pulles your token from .env
Monster.run(bot_token)
#runs the bot
