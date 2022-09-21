
'''
Event function that is called at each message
Stops if the sender is the bot itself (to avoid infinite loop)
Sends "Salut tout seul" and pings the sender when he types "Salut tout le monde"
'''
async def reply(message, bot):
    if message.author == bot.user:
        return

    if message.content == 'Salut tout le monde':
        reply = f'Salut tout seul {message.author.mention} 😆'
        await message.channel.send(reply)
    await bot.process_commands(message)