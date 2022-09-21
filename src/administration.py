import discord
'''
This function sets the user as admin
If no admin role exist, create one
'''
async def set_admin(ctx, nickname):

    # check if admin role exist
    admin_role = False
    for role in ctx.guild.roles: 
        if role.name == 'Admin':
            admin_role = True
            break

    # create admin role
    user = discord.utils.get(ctx.guild.members, name=nickname)
    if not admin_role: 
        permissions = discord.Permissions.all()
        print("Creating admin role")
        await ctx.guild.create_role(name="Admin", mentionable=True, permissions=permissions)
    if user:
        await user.add_roles(discord.utils.get(user.guild.roles, name="Admin"))


'''
This function bans mentionned user
'''
async def ban_user(ctx, member): 
    user = discord.utils.get(ctx.guild.members, name=member)
    await user.ban(reason="Déso, byebye")


'''
This function count the number of members and their status
'''
async def count_user(ctx):
    online = []
    offline = []
    idle = []
    do_not_disturb = []

    for member in ctx.guild.members:
        if str(member.status) == 'online':
            online.append(member.name)
            continue
        if str(member.status) == 'offline':
            offline.append(member.name)
            continue
        if str(member.status) == 'idle':
            idle.append(member.name)
            continue
        if str(member.status) == 'dnd' or str(member.status) == "do_not_disturb":
            do_not_disturb.append(member.name)
            continue
    
    #reply = f"{online} members are online, {idle} are idle, {offline} are off and {do_not_disturb} are Do not disturb"
    reply = f"Online (total : {len(online)}): "
    for name in online :
        reply += name + ", "
    reply += f"\nOffline (total : {len(offline)}): "
    for name in offline :
        reply += name + ", "
    reply += f'\nIdle (total : {len(idle)}): '
    for name in idle :
        reply += name + ", "
    reply += f'\nDo not disturb (total : {len(do_not_disturb)}): '
    for name in do_not_disturb :
        reply += name + ", "

    await ctx.send(reply)