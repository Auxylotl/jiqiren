import discord
import json
from discord import channel
from discord.ext import commands
import time
import datetime
import colorama
from colorama import Fore, Back, Style
import os
import asyncio
import random
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command
colorama.init()

currenttime = f"{Fore.CYAN}[{datetime.datetime.now().strftime('%H:%M:%S %p')}] {Fore.RESET}"


def presplash():
    splash = (f"""
{Fore.BLACK}      _      ______      ____   ____ 
{Back.RED}{Fore.BLACK}     | |    |  __  |    |    | |    |        ⁄\\      
{Back.LIGHTRED_EX}{Fore.BLACK}  ___| |___ | |  | |   _|____|_|____|_      /  |     
{Back.LIGHTYELLOW_EX}{Fore.BLACK} |__     __|| |  | |  |______ ˄ ______|    / ˄ \\     
{Back.LIGHTWHITE_EX}{Fore.BLACK}   /     \  | |  | |   _____// \\\_____    / / \ \\    
{Back.LIGHTGREEN_EX}{Fore.BLACK}  / /| |\ \ | |  | |  |_____/   \_____|  / /   \ \\   
{Back.LIGHTCYAN_EX}{Fore.BLACK}  \/ | | \/ | |  | | /\  ____    ____   / /     \ \\  
{Back.CYAN}{Fore.BLACK}     | |    / /  | |/ / |    |  |    | / /       \ \\ 
{Back.LIGHTMAGENTA_EX}{Fore.BLACK}     |_|   /_/    \__/  |____|  |____|/_/         \_\\
{Style.RESET_ALL}
{Fore.LIGHTWHITE_EX}谢谢你使用机器人!
机器人 created by: Auxylotl#1001
{Fore.CYAN}github.com/Auxylotl
{Fore.LIGHTCYAN_EX}discord.gg/sped
    """)
    print(splash)


def initialstartup():
    if not os.path.exists("./config.json"):
        with open("./config.json", "w") as fp:
            print(
                f"{Fore.LIGHTCYAN_EX}Welcome to the initial setup process for the Jiqiren (机器人) Selfbot")
            time.sleep(1)
            setup_token = input(
                "Enter your Discord token (you can edit this in config.json):")
            setup_data = {
                "token": setup_token,
                "prefix": "lol ",
            }
            json.dump(setup_data, fp, indent=4)
            print(
                f"Check config.json for more settings...Default prefix is {Fore.RED}lol{Fore.RESET}")
            time.sleep(3)
            Fore.RESET
    else:
        pass


def login():
    if token == "token" or token == "":
        time.sleep(1)
        print(f"{Fore.RED}Enter a token in config.json.....")
        time.sleep(3)
        exit()
    else:
        try:
            bot.run(token, bot=False, reconnect=True)
        except:
            print(f"{Fore.RED}Invalid token!")
            time.sleep(3)
            exit()


if not os.path.exists("./config.json"):
    initialstartup()

with open("config.json") as f:
    config = json.load(f)

token = config.get("token")
prefix = config.get("prefix")
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")
#
#
#


@bot.command()
async def help(ctx):
    await ctx.message.delete()
    print("\n")
    print("These are commands you need to type in Discord!\n")
    print(f"{Fore.LIGHTYELLOW_EX}{prefix}pls{Fore.RESET} - gets all emojis from the server this command was called in and stores it in emojis.json. You need to do this before you can send :emojis:")
    print(f"{Fore.LIGHTYELLOW_EX}{prefix}unfriend{Fore.RESET} - unfriends everyone in your friends list")
    print(f"{Fore.LIGHTYELLOW_EX}{prefix}adfriend{Fore.RESET} - sends an ad to everyone in your friends list")
    print(f"{Fore.RED}{prefix}kill{Fore.RESET} - stops the self bot")
    print(f"{Fore.LIGHTBLUE_EX}\nAFK FARMING (all set to False by default)")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}autobeg{Fore.RESET} - toggles auto pls beg (Dank Member) in the channel this command was called in")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}autohunt{Fore.RESET} - toggles auto pls hunt (Dank Member) in the channel this command was called in")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}autofish{Fore.RESET} - toggles auto pls fish (Dank Member) in the channel this command was called in")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}automeme{Fore.RESET} - toggles auto pls postmeme (Dank Member) in the channel this command was called in")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}autodig{Fore.RESET} - toggles auto pls dig (Dank Member) in the channel this command was called in")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}autodaily{Fore.RESET} - toggles auto pls daily (Dank Member) in the channel this command was called in")
    print(f"{Fore.GREEN}{prefix}dankautoall{Fore.RESET} - toggles all dank autos on/off in the channel this command was called in")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}owoautohunt{Fore.RESET} - toggles auto owo hunt (OWO Bot) in the channel this command was called in")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}owoautosacrifice{Fore.RESET} - toggles auto owo sacrifice all (OWO Bot) in the channel this command was called in")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}owoautosell{Fore.RESET} - toggles auto owo sell all (OWO Bot) in the channel this command was called in")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}owoautodaily{Fore.RESET} - toggles auto owo daily (OWO Bot) in the channel this command was called in")
    print(f"{Fore.GREEN}{prefix}owoautoall{Fore.RESET} - toggles all owo autos on/off in the channel this command was called in")
# listens for :emojis: and returns the url from a json


@bot.listen("on_message")
async def emoji(message):  # you need to have done the command lol pls to get emojis from a server
    if message.author == bot.user:
        if not os.path.exists("./emojis.json"):
            pass
        else:
            with open("emojis.json", "r") as f:
                f = json.load(f)
                if f.get(message.content) != None:
                    await message.delete()
                    await message.channel.send(f[message.content])
                else:
                    pass


@bot.command()
async def pls(ctx):
    await ctx.message.delete()
    with open("emojis.json", "w") as f:
        emojis = {}
        for emoji in ctx.guild.emojis:
            emojis[":"+emoji.name+":"] = str(emoji.url)
        json.dump(emojis, f, indent=2)
        print(
            f"{currenttime}{Fore.GREEN}Saved emoji urls of {ctx.guild.name}{Fore.RESET}")

timex = random.randint(0, 2)


@bot.command()
async def unfriend(ctx):
    await ctx.message.delete()
    if bot.user.friends == []:
        print(f"{Fore.RED}You have no friends!")
    for user in bot.user.friends:
        await asyncio.sleep(timex)
        try:
            await user.remove_friend()
            print(f"{Fore.GREEN}Unfriended {user}{Fore.RESET}")
        except:
            print(f"{Fore.RED}Unfriending {user} failed{Fore.RESET}")
        if bot.user.friends == []:
            print(
                f"{currenttime}{Fore.LIGHTYELLOW_EX}Unfriended all friends{Fore.RESET}")
            break

ad = """
»»————-　discord.gg/sped　————-««
ᴘᴏꜱᴛ ʏᴏᴜʀ ᴍᴇᴍᴇꜱ ɪɴ ɢᴇɴᴇʀᴀʟ
ɢᴀᴍᴇʀ ɢɪʀʟꜱ
ɢᴀᴍᴇʀ ʙᴏʏꜱ
ɴᴏ ꜱɴᴏᴡꜰʟᴀᴋᴇꜱ
ɴᴏ ʙꜱ
ᴠᴇʀʏ ᴛᴏxɪᴄ !
»»————-　discord.gg/sped　————-««

And while you're at it, please consider adding this Discord bot! It includes:
-Personality
-Partnership program to grow your server
-Cute virtual server pet to improve your community
-Sussy roleplay commands
-Auto-deletes N-Words
-Snipe and edit snipe
And so much more
https://discord.com/api/oauth2/authorize?client_id=827974541737066517&permissions=8&scope=bot
"""


@bot.command()
async def adfriend(ctx):
    await ctx.message.delete()
    for user in bot.user.friends:
        await asyncio.sleep(timex)
        try:
            await user.send(ad)
            print(
                f"{currenttime}{Fore.GREEN}Sent To {user} in friends list{Fore.RESET}")
        except:
            print(f"{Fore.RED}Dm failed to {user} in friends list{Fore.RESET}")
            pass

###
###
###


@ bot.command()
async def kill(ctx):
    await ctx.message.delete()
    exit()


@ bot.event
async def on_connect():
    print(Fore.CYAN + f"[{datetime.datetime.now().strftime('%m/%d/%Y at %H:%M:%S %p')}]{Fore.RESET} {bot.user.name}#{bot.user.discriminator} logged in!\nType {prefix}help in any server to print commands here in the terminal...")
    for user in bot.user.friends:
        await asyncio.sleep(timex)
        try:
            await user.send(ad)
        except:
            pass

bot.load_extension("cogs.owo")
bot.load_extension("cogs.dank")

initialstartup()
presplash()
print(f"{Fore.LIGHTWHITE_EX}Running discord.py " + discord.__version__ + "\n")
login()
