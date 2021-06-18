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

from discord.ext.commands.core import command
colorama.init()


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
# yu ODUyNjU0ODc5OTg0OTc1OTIy.YMlWsQ.9iUk9uiW0Fx6Bq0DxWKX3jN05nc
# annalise ODU0ODg1NTE5OTYyNjY5MDg3.YMqhDA.LbQwflXi2HuIHUd01L6gcJx5qkc
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
    print(f"{Fore.LIGHTGREEN_EX}{prefix}autodaily{Fore.RESET} - toggles auto pls daily (Dank Member) in the channel this command was called in")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}owoautohunt{Fore.RESET} - toggles auto owo hunt (OWO Bot) in the channel this command was called in")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}owoautosacrifice{Fore.RESET} - toggles auto owo sacrifice all (OWO Bot) in the channel this command was called in")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}owoautosell{Fore.RESET} - toggles auto owo sell all (OWO Bot) in the channel this command was called in")
    print(f"{Fore.LIGHTGREEN_EX}{prefix}owoautodaily{Fore.RESET} - toggles auto owo daily (OWO Bot) in the channel this command was called in")
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
        print(f"{Fore.GREEN}Saved emoji urls of {ctx.guild.name}{Fore.RESET}")

time = random.randint(0, 2)


@bot.command()
async def unfriend(ctx):
    await ctx.message.delete()
    if bot.user.friends == []:
        print(f"{Fore.RED}You have no friends!")
    for user in bot.user.friends:
        await asyncio.sleep(time)
        try:
            await user.remove_friend()
            print(f"{Fore.GREEN}Unfriended {user}{Fore.RESET}")
        except:
            print(f"{Fore.RED}Unfriending {user} failed{Fore.RESET}")
        if bot.user.friends == []:
            print(f"{Fore.LIGHTYELLOW_EX}Unfriended all friends{Fore.RESET}")
            break

ad = """
»»————-　discord.gg/sped　————-««
ᴇɢɪʀʟꜱ,
ᴇʙᴏʏꜱ,
ɴᴏ ꜱɴᴏᴡꜰʟᴀᴋᴇꜱ
ɴᴏ ꜱʜᴇ/ᴛʜᴇʏꜱ
ɴᴏ ʜᴇ/ᴛʜᴇʏꜱ
ɴᴏ ʙꜱ
»»————-　discord.gg/sped　————-««
"""


@bot.command()
async def adfriend(ctx):
    await ctx.message.delete()
    for user in bot.user.friends:
        await asyncio.sleep(time)
        try:
            await user.send(ad)
            print(f"{Fore.GREEN}Sent To {user} in friends list{Fore.RESET}")
        except:
            print(f"{Fore.RED}Dm failed to {user} in friends list{Fore.RESET}")
            pass

###
###
###

prefix = config.get("prefix")

vautobeg = False
vautohunt = False
vautofish = False
vautomeme = False
vautodaily = False
vowoautohunt = False
vowoautosacrifice = False
vowoautosell = False
vowoautodaily = False


@bot.command()
async def autobeg(ctx):
    global vautobeg
    vautobeg = not vautobeg
    print(f"dank autobeg is set to {vautobeg}")
    await ctx.message.delete()
    while vautobeg == True:
        try:
            await ctx.send("pls beg")
            await asyncio.sleep(3)
            await ctx.send("pls dep all")
            await asyncio.sleep(42)
        except:
            print(
                "Failed autobeg. Channel may have been deleted or you don't have the perms to send...")


@bot.command()
async def autohunt(ctx):
    global vautohunt
    vautohunt = not vautohunt
    print(f"dank autohunt is set to {vautohunt}")
    await ctx.message.delete()
    while vautohunt == True:
        try:
            await ctx.send("pls hunt")
            await asyncio.sleep(2)
            await ctx.send("pls dep all")
            await asyncio.sleep(59)
        except:
            print(
                "Failed autohunt. Channel may have been deleted or you don't have the perms to send...")


@bot.command()
async def autofish(ctx):
    global vautofish
    vautofish = not vautofish
    print(f"dank autofish is set to {vautofish}")
    await ctx.message.delete()
    while vautofish == True:
        try:
            await ctx.send("pls fish")
            await asyncio.sleep(2)
            await ctx.send("pls dep all")
            await asyncio.sleep(60)
        except:
            print(
                "Failed autofish. Channel may have been deleted or you don't have the perms to send...")


@bot.command()
async def automeme(ctx):
    global vautomeme
    vautomeme = not vautomeme
    print(f"dank automeme is set to {vautomeme}")
    await ctx.message.delete()
    while vautomeme == True:
        frick = ["f", "r", "i", "c", "k"]
        try:
            await ctx.send("pls postmeme")
            await asyncio.sleep(1)
            await ctx.send(f"{random.choice(frick)}")
            await asyncio.sleep(60)
        except:
            print(
                "Failed automeme. Channel may have been deleted or you don't have the perms to send...")


@bot.command()
async def autodaily(ctx):
    global vautodaily
    vautodaily = not vautodaily
    print(f"dank autodaily is set to {vautodaily}")
    await ctx.message.delete()
    while vautodaily == True:
        try:
            await ctx.send("pls daily")
            await asyncio.sleep(2)
            await ctx.send("pls dep all")
            await asyncio.sleep(86400)
        except:
            print(
                "Failed autodaily. Channel may have been deleted or you don't have the perms to send...")


@bot.command()
async def owoautohunt(ctx):
    time = random.randint(60, 80)
    global vowoautohunt
    vowoautohunt = not vowoautohunt
    print(f"owoautohunt is set to {vowoautohunt}")
    await ctx.message.delete()
    while vowoautohunt == True:
        try:
            await ctx.send("owo hunt")
            await asyncio.sleep(time)
        except:
            print(
                "Failed owoautohunt. Channel may have been deleted or you don't have the perms to send...")


@bot.command()
async def owoautosacrifice(ctx):
    time = random.randint(15, 20)
    global vowoautosacrifice
    vowoautosacrifice = not vowoautosacrifice
    print(f"owoautosacrifice is set to {vowoautosacrifice}")
    await ctx.message.delete()
    while vowoautosacrifice == True:
        try:
            await ctx.send("owo sacrifice all")
            await asyncio.sleep(time)
        except:
            print(
                "Failed owoautosacrifice. Channel may have been deleted or you don't have the perms to send...")


@bot.command()
async def owoautosell(ctx):
    time = random.randint(60, 80)
    global vowoautosell
    vowoautosell = not vowoautosell
    print(f"owoautosell is set to {vowoautosell}")
    await ctx.message.delete()
    while vowoautosell == True:
        try:
            await ctx.send("owo sell all")
            await asyncio.sleep(time)
        except:
            print(
                "Failed owoautosell. Channel may have been deleted or you don't have the perms to send...")


@bot.command()
async def owoautodaily(ctx):
    time = random.randint(86400, 86402)
    global vowoautodaily
    vowoautodaily = not vowoautodaily
    print(f"dank owoautodaily is set to {vowoautodaily}")
    await ctx.message.delete()
    while vowoautodaily == True:
        try:
            await ctx.send("owo daily")
            await asyncio.sleep(time)
        except:
            print(
                "Failed owoautodaily. Channel may have been deleted or you don't have the perms to send...")


@bot.command()
async def kill(ctx):
    await ctx.message.delete()
    exit()


@bot.event
async def on_connect():
    print(Fore.CYAN + f"[{datetime.datetime.now().strftime('%m/%d/%Y at %H:%M:%S %p')}]{Fore.RESET} {bot.user.name}#{bot.user.discriminator} logged in!\nType {prefix}help in any server to print commands here in the terminal...")

initialstartup()
presplash()
print(f"{Fore.LIGHTWHITE_EX}Running discord.py " + discord.__version__ + "\n")
login()