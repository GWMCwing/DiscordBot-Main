async def helplist(message, prefix):
	
	array = ["help","status","getid","setpresence","connect","disconnect","mute","unmute","deafen","undeafen"]
	WIPArray = ["addrolemessage","connectfour","play","game"]
	await message.channel.send("Prefix in this Guild: " + prefix + "\nAvailable Commands: " + ", ".join(array)+"\nWIP Commands: " + ", ".join(WIPArray))