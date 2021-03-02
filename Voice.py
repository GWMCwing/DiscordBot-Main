# edited
from typing import NoReturn
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

async def removeItemFormPlaylist(client,message,arg):
    global guild_dictionary
    guild = message.guild

    if type(arg) != int:
        await message.channel.send('Incorrect argument' + str(arg))

    try:
        guildobj = guild_dictionary[str(guild.id)]
    except:
        await message.channel.send("There is nothing playing in this server")
    playlist = guildobj.playlist 

    # check if the playlist is incorrect
    if len(playlist) < arg:
        await message.channel.send("Index Incorrect: Index < " + str(len(playlist)))
        await sendPlayList(playlist,message)
    else:
    # correct index 
        removed = playlist.pop(arg)
        await message.channel.send("Removed: " + str(removed))




async def checkSupportedUrl(url):
    # check for youtube
    if youtube in url:
        address = url[12:]
    elif youtu.be in url:
        address = url[8:]
    else:
        return False
    return [url,address]


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
    await sendPlayList(playlist,message)

async def sendPlayList(playlist,message):
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
