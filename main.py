import os
import discord
import pytz
import datetime

from keep_alive import keep_alive
from replit import db
from presence import *

from help import *
from action import *
from Voice import *
from dictionary import *
from logvoiceupdate import *


PREFIX = os.getenv("PREFIX")
LOGGUILDID = os.getenv("LOGGUILDID")
LOGCHANNELID = os.getenv("LOGCHANNELID")
BOT_ID = os.getenv('BOT_ID')
PREVENTAFKKICK = os.getenv('preventAFKkickRoleName')

class MyClient(discord.Client):
	async def on_ready(self):
		await log('---------------------')
		await log('Logged on as {0}!'.format(self.user))
		await logStartUp(self)
		# await client.change_presence(activity=discord.Game(name="Ez"))
		await setpresence(client)
		await initdictionary()

	async def on_message(self, message):
		if message.author.bot:
			return
		print(type(message.author))
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

	async def on_voice_state_update(self,member,before,after):
		# print(type(member))
		if member.bot: 
			return
		if before.channel != after.channel:
			if before.channel != None and after.channel!= None:
				await logVC(member.name + " \n Moved To " + after.channel.name  + " From " + before.channel.name)
			elif before.channel == None:
				await logVC(member.name + " \n Entered Voice Channel " + after.channel.name)
			elif after.channel == None:
				await logVC(member.name + " \n Left All Voice Channel " + before.channel.name)
		# print("runned")
		guild = member.guild
		afkChannel = guild.afk_channel
		if afkChannel is not None and after.channel is not None:
			if after.channel.id == afkChannel.id:
				if before.channel.id != afkChannel.id:
					for targetRole in member.roles:
						if targetRole.name == PREVENTAFKKICK: 
							if before.channel.id != afkChannel.id:
								# await logVC("Prevented " + member.name + " from entering AFK room")
								await logVC("Prevent AFK disabled")
								# await member.move_to(channel = before.channel)
		
		
def getTime():
	# dt = datetime.timezone(datetime.timedelta(hours = 8))
	# hkdt = dt.now().time()
	# utsdt = pytz.utc.localize(datetime.utcnow())
	# hkdt = utsdt.astimezone(pytz.timezone("Asia/Hong_Kong"))
	# hkdt = hkdt.time()
	# hkdt = pytz.timezone('Asia/Hong_Kong').localize(datetime.now())
	# hkdt = hkdt.isoformat()
	hkdt = datetime.datetime.now().time()
	return hkdt

async def logStartUp(self):
	string = "[" + str(datetime.datetime.now().time())[:8] + "] " + 'Logged on as {0}!'.format(self.user)
	channel = client.get_channel(797016987522826260)
	await channel.send(string)

async def logVC(string):
	string = "[" + str(datetime.datetime.now().time())[:8] + "] " + string
	channel = client.get_channel(808338038727114772)
	print(string)
	await channel.send(string)

async def log(string):
	string = "[" + str(getTime())[:8] + "] " + string
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
	elif argumentlow[0] == ("preventafk"):
		await preventAFK(message,PREVENTAFKKICK)



client = MyClient()

keep_alive()
# dont add def below
client.run(os.getenv("TOKEN"))

