import random
import discord
import time
import config
from config import token, link, prefix, ownerid
from discord import colour
from discord import embeds
from discord import member
from discord.ext import commands
from asyncio import *
from discord.flags import Intents
from discord import Intents
from discord.ext.commands import Bot



client = Bot(prefix)
client.remove_command('help')
colors = [0x000000 , 0x0000AA , 0x000055]

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(title="Not Found the Command" , colour=random.choice(colors))
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)

async def help(ctx, amount=5):
    embed=discord.Embed(title="Help Bot Commands ❤❤" , colour=random.choice(colors))
    embed.add_field(name="-ban", value="```⛔For Ban User⛔```",inline=True)
    embed.add_field(name="-kick", value="```⛔For Kick User⛔```",inline=True)
    embed.add_field(name="-clear", value="```♻For Clear Message♻```",inline=True)
    embed.add_field(name="-setstates", value="```✅Change States Bot✅```",inline=True)
    embed.add_field(name="-setactivity", value="```🔰Change Activity Bot🔰```",inline=True)
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)

async def setstates(ctx,status_type):
    if (status_type == 'idle'):
        await client.change_presence(status=discord.Status.idle)
        await ctx.send('Status Change idle ')

    elif(status_type == 'dnd'):
        await ctx.send('Status Change dnd')
        await client.change_presence(status=discord.Status.dnd)

    else:
        await ctx.send('Status Change Online')
        await client.change_presence(status=discord.Status.online)



@client.command()
@commands.has_permissions(administrator=True)

async def setactivity(ctx,activity_type, * ,activity_text):
    if (activity_type == 'playing'):
         await client.change_presence(activity=discord.Game(name=activity_text))
         await ctx.send('Status Change To Playing')


    elif(activity_type == 'streaming'):
         await client.change_presence(activity=discord.Streaming(name=activity_text,url='https://www.twitch.tv/twitch'))
         await ctx.send('Status Change To streaming')


    elif(activity_type == 'listening'):
         await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=activity_text))
         await ctx.send('Status Change To listening')

         
    elif(activity_type == 'watching'):  
         await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=activity_text))
         await ctx.send('Status Change To watching')



@client.command()
@commands.has_permissions(administrator=True)

async def setup_verification(ctx):
    channel_id = #channel ID
    Text = "For Verify Please Send !verify"
    embedVar = discord.Embed(title = "Verify your identity", description = Text, color = 0xC311EF)
    embedVar.add_field(name = "\u200B", value = "\u200B")
    embedVar.add_field(name = "Your Text", value = "Your Text." , inline=False)
    await ctx.channel.send(embed=embedVar)
    #await ctx.send(Text)

@client.command()
@commands.has_permissions(administrator=True)

async def verify(ctx):
    channel = #channel Id
    if discord.TextChannel.id == channel:
        clear()
        embed=discord.Embed(title=f"{author} You Have Been verify" , colour=random.choice(colors))
        await ctx.channel.send(embed=embed)
    else:
        author = ctx.message.author.name
        memberRole = discord.utils.get(ctx.guild.roles, name='Your Role Name')
        await ctx.author.add_roles(memberRole)


        roleremove = discord.utils.get(ctx.guild.roles, name='Your Role Name')
        await ctx.author.remove_roles(roleremove)
        embed=discord.Embed(title=f"{author} unVerify" , colour=random.choice(colors))
        await ctx.channel.send(embed=embed)


@client.event
async def on_ready():
    print("----------------------")
    print("Logged In As")
    print("Username: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    print("----------------------")

@client.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")



@client.command()
async def serverinvite(ctx):
    invites = []
    for guild in client.guilds:
        for c in guild.text_channels:
            # make sure the bot can actually create an invite
            if c.permissions_for(guild.me).create_instant_invite:
                invite = await c.create_invite()
                invites.append(invite)
                await ctx.send(invite)
                break

#Gets a List of Bans From The Server


@client.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.author).split("#")[0]
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="👑|Owner", value=f"{owner}", inline=True)
    embed.add_field(name="🆔|Server ID", value=id, inline=True)
    embed.add_field(name="📆|Created On", value = ctx.guild.created_at.strftime("%b %d %Y"), inline = True)
    embed.add_field(name="🌎|Region", value=region, inline=True)
    embed.add_field(name="👥|Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

#a command that sets the bots game



#Clears The Chat

@client.command()
@commands.has_permissions(administrator=True)

async def clear(ctx, amount=0):
    if amount == 0:
       fail = await ctx.send ("**Send The Value ** !")
       await asyncio.sleep (6)
       await fail.delete()
    if amount > 3:
       await ctx.channel.purge(limit=amount)
       sucess = await ctx.send (f"**{amount} Message Delete ☑️**") #sending success msg
       await asyncio.sleep (6) #wait 6 seconds
       await sucess.delete() #deleting the sucess msg
    elif amount == 0:
       fail = await ctx.send ("**Please Enter The Value** !")
       await asyncio.sleep (6)
       await fail.delete()


@client.command()
@commands.has_permissions(administrator=True)

async def warn(ctx, member: discord.Member, *, arg):
    logsChannel = client.get_channel()#channel ID
    user = member.mention
    embed = discord.Embed(title="Warning issued: ", color=0xf40000)
    embed.add_field(name="Warning: ", value=f'Reason: {arg}', inline=False)
    embed.add_field(name="User warned: ", value=f'{member.mention}', inline=False)
    embed.add_field(name="Warned by: ", value=f'{ctx.author}', inline=False)

    embed2 = discord.Embed(title="Warning issued: ", color=0xf40000)
    embed2.add_field(name="Warning: ", value=f'Reason: {arg}', inline=False)
    embed2.add_field(name="User warned: ", value=f'{member.mention}', inline=False)
    embed2.add_field(name="Warned by: ", value=f'{ctx.author}', inline=False)

    rolememberemove = discord.utils.get(ctx.guild.roles, name='⇃👤️⇂Member')
    await member.remove_roles(rolememberemove)

    warnrole = discord.utils.get(ctx.guild.roles, name='Warn')
    await member.add_roles(warnrole)

    await logsChannel.send(embed=embed2)
    await member.send(f'Your Have Been warn : **{arg}**!')
    message = await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)

async def unwarn(ctx, member: discord.Member):
    logsChannel = client.get_channel()#channel ud
    user = member.mention
    embed = discord.Embed(title="Warning issued: ", color=0xf50000)
    embed.add_field(name="User UnWarned: ", value=f'{member.mention}', inline=False)
    embed.add_field(name="UnWarned By: ", value=f'{ctx.author}', inline=False)

    embed2 = discord.Embed(title="Warning issued: ", color=0xf40000)
    embed2.add_field(name="User Unwarned: ", value=f'{member.mention}', inline=False)
    embed2.add_field(name="UnWarned by: ", value=f'{ctx.author}', inline=False)

    givememberole = discord.utils.get(ctx.guild.roles, name='⇃👤️⇂Member')
    await member.add_roles(givememberole)

    takewarnrole = discord.utils.get(ctx.guild.roles, name='Warn')
    await member.remove_roles(takewarnrole)
    
    await logsChannel.send(embed=embed2)
    await member.send(f'warn take for you')
    message = await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)

async def kick(ctx , member: discord.Member , * , reason=None):

    await member.kick(reason=reason)
    amount = 1
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
        colour= (0x00CECE),
        description = f'{member} The reason {reason} Kick '

    )
    embed.set_author(name="Kick System", url="" , icon_url="")
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)

async def ban(ctx , member: discord.Member , * , reason=None):

    await member.ban(reason=reason)
    amount = 1
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
        colour= (0x00CECE),
        description = f'{member} Be reason {reason} ban'

    )
    embed.set_author(name="ban System", url="" , icon_url="")
    await ctx.send(embed=embed)




client.run(token)