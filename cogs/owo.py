import discord
from discord.ext import commands
import colorama
from colorama import Fore
import random
import datetime
import json
import asyncio
from playsound import playsound
colorama.init()

currenttime = f"{Fore.CYAN}[{datetime.datetime.now().strftime('%H:%M:%S %p')}] {Fore.RESET}"
with open("config.json") as f:
    config = json.load(f)
vowoautohunt = False
vowoautosacrifice = False
vowoautosell = False
vowoautodaily = False


class Owo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    global currenttime
    global config
    global vowoautodaily
    global vowoautohunt
    global vowoautosacrifice
    global vowoautosell

    @commands.command()
    async def owoautohunt(self, ctx):
        time = random.randint(15, 30)
        global vowoautohunt
        vowoautohunt = not vowoautohunt
        print(f"{currenttime}{Fore.LIGHTMAGENTA_EX}owoautohunt is set to {Fore.LIGHTYELLOW_EX}{vowoautohunt}{Fore.RESET}")
        try:
            await ctx.message.delete()
        except:
            pass
        while vowoautohunt == True:
            try:
                await ctx.send("owo hunt")
                await asyncio.sleep(time)
            except:
                print(
                    "Failed owoautohunt. Channel may have been deleted or you don't have the perms to send...")

    @commands.command()
    async def owoautosacrifice(self, ctx):
        time = random.randint(60, 80)
        global vowoautosacrifice
        vowoautosacrifice = not vowoautosacrifice
        print(f"{currenttime}{Fore.LIGHTMAGENTA_EX}owoautosacrifice is set to {Fore.LIGHTYELLOW_EX}{vowoautosacrifice}{Fore.RESET}")
        try:
            await ctx.message.delete()
        except:
            pass
        while vowoautosacrifice == True:
            try:
                await asyncio.sleep(1)
                await ctx.send("owo sacrifice all")
                await asyncio.sleep(time)
            except:
                print(
                    "Failed owoautosacrifice. Channel may have been deleted or you don't have the perms to send...")

    @commands.command()
    async def owoautosell(self, ctx):
        time = random.randint(60, 80)
        global vowoautosell
        vowoautosell = not vowoautosell
        print(f"{currenttime}{Fore.LIGHTMAGENTA_EX}owoautosell is set to {Fore.LIGHTYELLOW_EX}{vowoautosell}{Fore.RESET}")
        try:
            await ctx.message.delete()
        except:
            pass
        while vowoautosell == True:
            try:
                await asyncio.sleep(2)
                await ctx.send("owo sell all")
                await asyncio.sleep(time)
            except:
                print(
                    "Failed owoautosell. Channel may have been deleted or you don't have the perms to send...")

    @commands.command()
    async def owoautodaily(self, ctx):
        time = random.randint(86400, 86402)
        global vowoautodaily
        vowoautodaily = not vowoautodaily
        print(f"{currenttime}{Fore.LIGHTMAGENTA_EX}owoautodaily is set to {Fore.LIGHTYELLOW_EX}{vowoautodaily}{Fore.RESET}")
        try:
            await ctx.message.delete()
        except:
            pass
        while vowoautodaily == True:
            try:
                await ctx.send("owo daily")
                await asyncio.sleep(time)
            except:
                print(
                    "Failed owoautodaily. Channel may have been deleted or you don't have the perms to send...")

    @commands.command()
    async def owoautoall(self, ctx):
        tasks = [
            self.owoautohunt(ctx),
            self.owoautosacrifice(ctx),
            self.owoautosell(ctx),
            self.owoautodaily(ctx)
        ]
        await asyncio.gather(*tasks)

    @commands.Cog.listener()
    async def stopowohunt(self, message):
        global vowoautohunt
        if vowoautohunt == True:
            if message.author.id == 408785106942164992:
                if f"{self.bot.user}" and "You don't have enough cowoncy!" in message.content:
                    vowoautohunt = False
                    print(
                        f"{currenttime}{Fore.RED}owoautohunt was set to {Fore.LIGHTYELLOW_EX}False{Fore.RESET} because you don't have cowoncy...")
                else:
                    pass
            else:
                pass
        else:
            pass

    @commands.Cog.listener()
    async def stopowos(self, message):
        global vowoautosacrifice
        global vowoautosell
        if vowoautosacrifice == True or vowoautosell == True:
            if message.author.id == 408785106942164992:
                if f"{self.bot.user}" and "You don't have enough animals! >:c" in message.content:
                    vowoautosell = False
                    vowoautosacrifice = False
                    print(
                        f"{currenttime}{Fore.RED}owoautosacrifice was set to {Fore.LIGHTYELLOW_EX}False{Fore.RESET} because you don't have animals...")
                    print(
                        f"{currenttime}{Fore.RED}owoautosell was set to {Fore.LIGHTYELLOW_EX}False{Fore.RESET} because you don't have animals...")
                else:
                    pass
            else:
                pass
        else:
            pass

    @commands.Cog.listener()
    async def detectedbot(self, message):
        global vowoautohunt
        global vowoautosacrifice
        global vowoautosell
        global vowoautodaily
        if vowoautohunt == True or vowoautosacrifice == True or vowoautosell == True or vowoautodaily == True:
            if message.author.id == 408785106942164992:
                if f"{self.bot.user}" and "Please complete your captcha to verify that you are human!" in message.content:
                    vowoautohunt = False
                    vowoautosacrifice = False
                    vowoautosell = False
                    vowoautodaily = False
                    playsound("reminder.mp3")
                    print(
                        f"{currenttime}{Fore.RED}All owo tasks were set to {Fore.LIGHTYELLOW_EX}False{Fore.RESET} because you need to prove you are human...")
                    print(
                        f"{Fore.LIGHTWHITE_EX}Check your owo bot dms!")
                elif f"{self.bot.user}" and "Beep Boop. Please DM me with only the following" in message.content:
                    vowoautohunt = False
                    vowoautosacrifice = False
                    vowoautosell = False
                    vowoautodaily = False
                    playsound("reminder.mp3")
                    print(
                        f"{currenttime}{Fore.RED}All owo tasks were set to {Fore.LIGHTYELLOW_EX}False{Fore.RESET} because you need to prove you are human...")
                    print(
                        f"{Fore.LIGHTWHITE_EX}owo captcha message url -> {message.jump_url}")
                else:
                    pass
            else:
                pass
        else:
            pass


def setup(bot):
    bot.add_cog(Owo(bot))
