# edited
from replit import db
from dictionary import *
#  https://www.youtube.com/watch?v=q0lsD7U0JSI
#  https://gabrieltanner.org/blog/dicord-music-bot
async def connectVoiceChannel(client, message):
    if message.author.voice != None:
        channel = message.author.voice.channel
        guild = message.guild
        await guild.change_voice_state(channel=channel)
        return channel
    else:
        await message.channel.send("Please connecte to a Voice Channel")
        return None


async def addtoPlayList(client, message, url):
    # if await checkSupportedUrl(url):
        # await message.channel.send("This URL is not Supported")
        # return
    global guild_dictionary
    guild = message.guild
    if str(guild.id) in guild_dictionary:
        1 == 1
    else:
        guild_dictionary[str(guild.id)] = guildObj()
    #  get the guild obj
    guildobj = guild_dictionary[str(guild.id)]
    #  get the playlist []
    playlist = guildobj.playlist
    guildobj.addUrl(url)
    return


async def checkSupportedUrl(url):

    return false


async def disconnectVoiceChannel(client, message):
    guild = message.guild
    await guild.change_voice_state(channel=None)


async def playSound(client, message, url):
    channel = await connectVoiceChannel(client, message)
    if channel == None:
        return
    # channel.play()


async def getplaylist(message):
    global guild_dictionary
    guild = message.guild
    try:
        guildobj = guild_dictionary[str(guild.id)]
    except:
        await message.channel.send("There is nothing playing in this server")
    playlist = guildobj.playlist
    playlist.insert(0, "Current Playlist: ")
    i = 1
    while i < len(playlist):
        playlist[i] = str(i) + ". " + playlist[i]
        i += 1
    tempmessage = "\n".join(playlist)
    await message.channel.send(tempmessage)


class guildObj:
    def __init__(self):
        self.playlist = []

    def addUrl(self, url):
        self.playlist.append(url)
