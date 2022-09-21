from random import randint
from discord.ext import commands
import discord

# This import contains the events functions
import event

# This import contains the commands functions
import command

# This import contains the administration functions
import administration

intents = discord.Intents.default()
intents.members = True
intents.presences = True
#intents.message_content = True
intents.messages = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 0000  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')



''' 
Commands
'''
# !name command
@bot.command(name="name")
async def name(ctx):
    await command.return_name(ctx)

# !d6 command
@bot.command(name="d6")
async def roll(ctx):
    await command.roll_number(ctx)

# !admin command adds user as admin 
@bot.command(name="admin")
async def admin(ctx, member):
    await administration.set_admin(ctx, member)

# !ban command to ban member
@bot.command(name="ban")
async def ban(ctx, member):
    await administration.ban_user(ctx, member)

# !count command to count users
@bot.command(name="count")
async def count(ctx):
    await administration.count_user(ctx)

# !xkcd post a comic
@bot.command(name="xkcd")
async def comic(ctx):
    await command.comic(ctx)

# !poll to create a poll 
@bot.command(name="poll")
async def poll(ctx, question):
    await command.poll(ctx, question)

'''
# Events
'''
# Triggered at every message
@bot.event
async def on_message(message):
    await event.reply(message, bot)



token = "token"
bot.run(token)  # Starts the bot