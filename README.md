<div align="center">
	<br />
	<p>
		<a href="https://discordpy.readthedocs.io/"><img src="https://user-images.githubusercontent.com/122752399/213015275-813b391e-c057-4a12-9f09-26f6104e37a7.png" width="546" alt="discord.py"/></a>
</div>

## About

discord.py is a powerful [python](https://python.org).

## Ability
As follows:

`Embed Menu`

`Help Menu`

`Set states`

`Set activity`

`Setup verification`

`Ping`

`Server invite`

`Server info`

`Clear`

`Warn`

`Kick and Ban`


## Installation

**Python-3.10.5 or newer is required.**

```sh-session
pip install discord.py
pip install asyncio
pip install discord.ext
```

## Note
 It is a simple robot and has abilities but not advanced
Before running the robot, check the server.py file and fill the contents like `URL,ICON` and similar things according to your taste so that the robot does not encounter problems



## Usage 

Install The All package:

Go to The `botdiscord` File Open `Config.py` And Change The Setting Of Your Bot:

```py
token = '' #Put Your bots token here
prefix = '' #put prefix here
link = '' #put bot invite link here
ownerid = '' #put your id here
```
And read the note

Next Open The Server.py And Your Bot Is Ready In Server Discord

Example Use:
`Prefix`ping=>`200ms`
```py
@client.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
```
