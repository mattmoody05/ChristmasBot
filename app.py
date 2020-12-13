# config vars
BOTTOKEN = ""
BOTPREFIX = "."
IMAGE = "https://i.imgur.com/1kriI0K.jpg"


# discord imports
import discord
from discord.ext import commands

# other imports
from time import sleep
import christmasfunctions
from random import randint


# useful functions
def SimpleEmbed(author):
    Embed = discord.Embed(
        colour = discord.Colour.red()
    )
    Embed.set_author(name = author, icon_url=IMAGE)
    return Embed


# bot account setup
client = commands.Bot(command_prefix = BOTPREFIX)
client.remove_command("help")

# on ready events
@client.event
async def on_ready():
    ListeningTo = discord.Activity(type=discord.ActivityType.listening, name="Christmas songs")
    await client.change_presence(status=discord.Status.online, activity=ListeningTo)
    print(f"We have logged in as {client.user}")


# get a random christmas joke
@client.command()
async def joke(ctx):
    joke = christmasfunctions.GetChrismasJoke()
    await ctx.send(joke[0])
    sleep(1)
    await ctx.send(joke[1])


# get a random christmas film
@client.command()
async def film(ctx):
    await ctx.send(embed = SimpleEmbed("Your Christmas film: " + christmasfunctions.GetChrismasFilm()))


# play a random christmas song
@client.command()
async def song(ctx):
    
    # gets the channel that the user is in and connects to it
    channel = ctx.author.voice.channel
    if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
    await channel.connect()
    
    # gets the a random song file
    songs = ["FrostyTheSnowman.wav", "HereComesSantaClaus.wav", "JingleBells.wav", "LetItSnow.wav", "RudolphTheRedNosedReindeer.wav", "TwelveDaysOfChristmas.wav", "WhiteChristmas.wav"]
    query = f"./songs/{songs[randint(0, len(songs) - 1)]}"
    
    # plays the chosen song
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
    ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
    
    # sends a confirm message
    await ctx.send(embed = SimpleEmbed("Now playing! Use '.stop' to stop playing"))


# command to stop music playback
@client.command()
async def stop(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()
    await ctx.send(embed = SimpleEmbed("Disconnected from voice channel"))


# providing info about the various commands
@client.command()
async def help(ctx):
    HelpEmbed = discord.Embed(
        colour = discord.Colour.red()
    )
    HelpEmbed.set_author(name = "ChristmasBot", icon_url=IMAGE)
    HelpEmbed.add_field(name = ".song", value = "Plays a random Chrismas song", inline=False)
    HelpEmbed.add_field(name = ".stop", value = "Stops any music that the bot is playing", inline=False)
    HelpEmbed.add_field(name = ".film", value = "Gets a random Christmas film, great inspiration for what to watch next!", inline=False)
    HelpEmbed.add_field(name = ".joke", value = "Sends a cheesy christmas joke, perfect!", inline=False)
    await ctx.send(embed = HelpEmbed)


# running the bot using the bot token
client.run(BOTTOKEN)