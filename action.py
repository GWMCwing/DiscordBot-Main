import discord
async def getid(message, argument):
	if len(argument) == 0:
		await message.channel.send("Missing Argument [guild/channel]")
	elif argument[0] == "guild":
		await message.channel.send("This Guild id: "+str(message.guild.id))
	elif argument[0] == "channel":
		await message.channel.send("This Channel id: "+str(message.channel.id))
	else:
		await message.channel.send("-status [guild/channel]")

async def changePresence(client,message,argument):
	if len(argument) == 0:
		await message.channel.send("Missing Argument [String]")
		return
	await client.change_presence(activity=discord.Game(name=" ".join(argument)))

async def mute(client,message,arguments):
	tempboolean = False
	if message.mentions:
		for user in message.mentions:
			print(type(user))
			await user.edit(mute=True)
			tempboolean = True
	elif arguments:
		for idt in arguments:
			try:
				target = await message.guild.fetch_member(int(idt))
				await target.edit(mute=True)
				tempboolean = True
			except:
				1==1
	elif len(arguments) == 0:
		target = message.author
		await target.edit(mute = True)
		tempboolean = True
	if not tempboolean:
		await message.channel.send("No user is mentioned")

async def unmute(client,message,arguments):
	tempboolean = False
	if message.mentions:
		for user in message.mentions:
			print(type(user))
			await user.edit(mute=False)
			tempboolean = True
	elif arguments:
		for idt in arguments:
			try:
				target = await message.guild.fetch_member(int(idt))
				await target.edit(mute=False)
				tempboolean = True
			except:
				1==1
	elif len(arguments) == 0:
		target = message.author
		await target.edit(mute = False)
		tempboolean = True
	if not tempboolean:
		await message.channel.send("No user is mentioned")

async def deafen(client,message,arguments):
	tempboolean = False
	if message.mentions:
		for user in message.mentions:
			print(type(user))
			await user.edit(deafen=True)
			tempboolean = True
	elif arguments:
		for idt in arguments:
			try:
				target = await message.guild.fetch_member(int(idt))
				await target.edit(deafen=True)
				tempboolean = True
			except:
				1==1
	elif len(arguments) == 0:
		target = message.author
		await target.edit(deafen = True)
		tempboolean = True
	if not tempboolean:
		await message.channel.send("No user is mentioned")

async def undeafen(client,message,arguments):
	tempboolean = False
	if message.mentions:
		for user in message.mentions:
			print(type(user))
			await user.edit(deafen=False)
			tempboolean = True
	elif arguments:
		for idt in arguments:
			try:
				target = await message.guild.fetch_member(int(idt))
				await target.edit(deafen=False)
				tempboolean = True
			except:
				1==1
	elif len(arguments) == 0:
		target = message.author
		await target.edit(deafen = False)
		tempboolean = True
	if not tempboolean:
		await message.channel.send("No user is mentioned")

async def compareRole(user1,user2):
	
	return False

async def autoAddRoleMessage(message, PREFIX):
	mesg = await message.channel.send("Please reply this message according to this format: [emoji] [role] [emoji] [role]...\nExample :space_invader: @spaceRole")
	# add user and guild and channel to the dict => 
	# choose channel to be sent
	# send message to confirm
