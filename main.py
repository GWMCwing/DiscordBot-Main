import os
import discord
from keep_alive import keep_alive
from datetime import datetime
from replit import db
from presence import *

from help import *
from action import *
from Voice import *
from dictionary import *

PREFIX = os.getenv("PREFIX")
LOGGUILDID = os.getenv("LOGGUILDID")
LOGCHANNELID = os.getenv("LOGCHANNELID")
BOT_ID = os.getenv('BOT_ID')

class MyClient(discord.Client):
	async def on_ready(self):
		await log('----------------')
		await log('Logged on as {0}!'.format(self.user))
		# await client.change_presence(activity=discord.Game(name="Ez"))
		await setpresence(client)
		await initdictionary()

	async def on_message(self, message):
		if message.author.bot:
			return
		await log('{0.author}: {0.content}'.format(message))

		if message.mentions:
			print(type(message.mentions[0].id))
			print(type(BOT_ID))
			if message.mentions[0].id == int(BOT_ID):
				tempcontent = message.content[22:]
				tempcontent = tempcontent.replace(" ",'')
				# print(tempcontent)
				if tempcontent == "help":
					await helplist(message,PREFIX)
				return

		if message.content[0:1] == PREFIX:
			await runCommand(client,PREFIX,message)
			return

		
		
			
async def log(string):
	string = "[" + str(datetime.now().time())[:8] + "] " + string
	channel = client.get_channel(796250061419446325)
	print(string)
	await channel.send(string)

async def runCommand(client,PREFIX,message):
	argumentOrg = message.content[1:].split(" ")
	argumentlow = message.content[1:].lower().split(" ")
	print(argumentlow)
	if argumentlow[0] == ("help"):
		await helplist(message,PREFIX)
	elif argumentlow[0] == ("status"):
		await log(argumentOrg[1:])
	elif argumentlow[0] == ("getid"):
		await getid(message,argumentOrg[1:])
	elif argumentlow[0] == ("setpresence"):
		await changePresence(client,message,argumentOrg[1:])
	elif argumentlow[0] == ("connect"):
		await connectVoiceChannel(client,message)
	elif argumentlow[0] == ("disconnect"):
		await disconnectVoiceChannel(client,message)
	elif argumentlow[0] == ("p"):
		await addtoPlayList(client,message,"".join(argumentOrg[1:]))
	elif argumentlow[0] == ("playlist"):
		await getplaylist(message)
	elif argumentlow[0] == ("mute"):
		await mute(client,message,argumentOrg[1:])
	elif argumentlow[0] == ("unmute"):
		await unmute(client,message,argumentOrg[1:])
	elif argumentlow[0] == ("deafen"):
		await deafen(client,message,argumentOrg[1:])
	elif argumentlow[0] == ("undeafen"):
		await undeafen(client,message,argumentOrg[1:])




client = MyClient()
keep_alive()
# dont add def below
client.run(os.getenv("TOKEN"))

