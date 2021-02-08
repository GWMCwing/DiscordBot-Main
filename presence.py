import discord
async def setpresence(client):
	# game = discord.Activity()
	# game.name = "name"
	# game.type = listening
	# game.state = "Listening"
	# game.details = "details"
	await client.change_presence(status = discord.Status.idle, activity = discord.Activity(application_id = 670964358393888768, name = "NaNDe?", type = discord.ActivityType.listening,details = "Listening to Chapter I"))
#  https://discord.com/developers/applications/
# await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name='Enter status here'))
#  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))