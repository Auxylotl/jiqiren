import discord
from discord.ext import commands
import colorama
from colorama import Fore
import random
import datetime
import json
import asyncio
colorama.init()

vautobeg = False
vautohunt = False
vautofish = False
vautomeme = False
vautodig = False
vautodaily = False

currenttime = f"{Fore.CYAN}[{datetime.datetime.now().strftime('%H:%M:%S %p')}] {Fore.RESET}"
with open("config.json") as f:
    config = json.load(f)


class Dank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    global vautobeg
    global vautohunt
    global vautofish
    global vautomeme
    global vautodig
    global vautodaily
    global currenttime
    global config
    timex = random.uniform(40.1, 44.9)
    timex2 = random.uniform(2.4, 4.8)

    @commands.command()
    async def autobeg(self, ctx):
        global vautobeg
        vautobeg = not vautobeg
        print(f"{currenttime}{Fore.LIGHTMAGENTA_EX}dank autobeg is set to {Fore.LIGHTYELLOW_EX}{vautobeg}{Fore.RESET}")
        try:
            await ctx.message.delete()
        except:
            pass
        while vautobeg == True:
            try:
                await ctx.send("pls beg")
                await asyncio.sleep(timex2)
                await ctx.send("pls dep all")
                await asyncio.sleep(timex)
            except:
                print(
                    "Failed autobeg. Channel may have been deleted or you don't have the perms to send...")

    @commands.command()
    async def autohunt(self, ctx):
        global vautohunt
        vautohunt = not vautohunt
        print(f"{currenttime}{Fore.LIGHTMAGENTA_EX}dank autohunt is set to {Fore.LIGHTYELLOW_EX}{vautohunt}{Fore.RESET}")
        try:
            await ctx.message.delete()
        except:
            pass
        while vautohunt == True:
            try:
                await ctx.send("pls hunt")
                await asyncio.sleep(timex)
            except:
                print(
                    "Failed autohunt. Channel may have been deleted or you don't have the perms to send...")

    @commands.Cog.listener()
    async def buyrifle(self, message):
        global vautohunt
        if vautohunt == True:
            if message.author.id == 270904126974590976:
                if message.content.startswith(f"You don't have a hunting rifle"):
                    await message.channel.send("pls buy hunting")
                else:
                    pass
            else:
                pass
        else:
            pass

    @commands.command()
    async def autofish(self, ctx):
        global vautofish
        vautofish = not vautofish
        print(f"{currenttime}{Fore.LIGHTMAGENTA_EX}dank autofish is set to {Fore.LIGHTYELLOW_EX}{vautofish}{Fore.RESET}")
        try:
            await ctx.message.delete()
        except:
            pass
        while vautofish == True:
            try:
                await ctx.send("pls fish")
                await asyncio.sleep(timex)
            except:
                print(
                    "Failed autofish. Channel may have been deleted or you don't have the perms to send...")

    @commands.Cog.listener()
    async def buyfishingpole(self, message):
        global vautofish
        if vautofish == True:
            if message.author.id == 270904126974590976:
                if message.content.startswith(f"You don't have a fishing pole"):
                    await message.channel.send("pls buy fishingpole")
                else:
                    pass
            else:
                pass
        else:
            pass

    @commands.command()
    async def automeme(self, ctx):
        global vautomeme
        vautomeme = not vautomeme
        print(f"{currenttime}{Fore.LIGHTMAGENTA_EX}dank automeme is set to {Fore.LIGHTYELLOW_EX}{vautomeme}{Fore.RESET}")
        try:
            await ctx.message.delete()
        except:
            pass
        while vautomeme == True:
            frick = ["f", "r", "i", "c", "k"]
            try:
                await ctx.send("pls postmeme")
                await asyncio.sleep(0.5)
                await ctx.send(f"{random.choice(frick)}")
                await asyncio.sleep(timex2)
                await ctx.send("pls dep all")
                await asyncio.sleep(timex)
            except:
                print(
                    "Failed automeme. Channel may have been deleted or you don't have the perms to send...")

    @commands.Cog.listener()
    async def buylaptop(self, message):
        global vautomeme
        if vautomeme == True:
            if message.author.id == 270904126974590976:
                if message.content.startswith(f"{self.bot.user.mention} oi you need to buy a laptop"):
                    await message.channel.send("pls buy laptop")
                else:
                    pass
            else:
                pass
        else:
            pass

    @commands.command()
    async def autodig(self, ctx):
        global vautodig
        vautodig = not vautodig
        print(f"{currenttime}{Fore.LIGHTMAGENTA_EX}dank autodig is set to {Fore.LIGHTYELLOW_EX}{vautodig}{Fore.RESET}")
        try:
            await ctx.message.delete()
        except:
            pass
        while vautodig == True:
            try:
                await ctx.send("pls dig")
                await asyncio.sleep(timex)
            except:
                print(
                    "Failed autodig. Channel may have been deleted or you don't have the perms to send...")

    @commands.Cog.listener()
    async def buyshovel(self, message):
        global vautodig
        if vautodig == True:
            if message.author.id == 270904126974590976:
                if message.content.startswith("You don't have a shovel, you need to go buy one"):
                    await message.channel.send("pls buy shovel")
                else:
                    pass
            else:
                pass
        else:
            pass

    @commands.command()
    async def autodaily(self, ctx):
        global vautodaily
        vautodaily = not vautodaily
        print(f"{currenttime}{Fore.LIGHTMAGENTA_EX}dank autodaily is set to {Fore.LIGHTYELLOW_EX}{vautodaily}{Fore.RESET}")
        try:
            await ctx.message.delete()
        except:
            pass
        while vautodaily == True:
            try:
                await ctx.send("pls daily")
                await asyncio.sleep(timex2)
                await ctx.send("pls dep all")
                await asyncio.sleep(86400)
            except:
                print(
                    "Failed autodaily. Channel may have been deleted or you don't have the perms to send...")

    @commands.command()
    async def dankautoall(self, ctx):
        tasks = [
            self.autobeg(ctx),
            self.autohunt(ctx),
            self.autofish(ctx),
            self.automeme(ctx),
            self.autodig(ctx),
            self.autodaily(ctx)
        ]
        await asyncio.gather(*tasks)


def setup(bot):
    bot.add_cog(Dank(bot))
