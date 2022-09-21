from random import randint

import discord
from discord.ext import commands


'''
This function returns the senders name
'''
async def return_name(ctx):
    await ctx.send(ctx.message.author.name)


'''
This function returns an integer between 1 and 6
'''
async def roll_number(ctx):
    await ctx.send(randint(1, 6))

'''
This function returns a link to xkcd comics
'''
async def comic(ctx):
    random_value = randint(1, 2673)
    await ctx.send(f"https://xkcd.com/{random_value}")


'''
This function creates a poll
'''
async def poll(ctx, question):
    await ctx.send("@here")
    message = await ctx.send(question)
    await message.add_reaction('👍')
    await message.add_reaction('👎')
