from pystyle import  Colors , Colorate , Write , System
from discord.ext import commands
import discord
from time import sleep
from threading import Thread
bot = commands.Bot(command_prefix = "H:", description = "Hologram Bot ;) ")

System.Title("$$ Hologram Spammer Discord bot by matxd $$")

Hologram = """

 ██░ ██  ▒█████   ██▓     ▒█████    ▄████  ██▀███   ▄▄▄       ███▄ ▄███▓
▓██░ ██▒▒██▒  ██▒▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒
▒██▀▀██░▒██░  ██▒▒██░    ▒██░  ██▒▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░
░▓█ ░██ ▒██   ██░▒██░    ▒██   ██░░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██ 
░▓█▒░██▓░ ████▓▒░░██████▒░ ████▓▒░░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒
 ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░
 ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░ ▒  ░  ░ ▒ ▒░   ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░
 ░  ░░ ░░ ░ ░ ▒    ░ ░   ░ ░ ░ ▒  ░ ░   ░   ░░   ░   ░   ▒   ░      ░   
 ░  ░  ░    ░ ░      ░  ░    ░ ░        ░    ░           ░  ░       ░   
                                                                        

"""

def Spam(message1):
    
    timer = 0

    @bot.command()
    async def alawackbar(ctx):
        while timer < 10 :
            await ctx.send(message1)

def Menu():

    System.Clear()
    print(Colorate.Vertical(Colors.purple_to_blue , Hologram))
    print()
    token = Write.Input("Enter The Token of Your Bot -> " , Colors.purple_to_blue , interval=0.0025)
    print()
    message = Write.Input("what message do you want to spam -> " , Colors.purple_to_blue , interval=0.0025)
    
    System.Clear()
    print(Colorate.Vertical(Colors.purple_to_blue , Hologram))
    print(Colorate.Vertical(Colors.purple_to_blue , "[+] Starting Creation..."))
    print(Colorate.Vertical(Colors.purple_to_blue , "[+] Token -> " + token))
    print(Colorate.Vertical(Colors.purple_to_blue , "[+] Message to Sent -> " + message))
    print()
    Write.Input("Press Enter For Start The Bot !!" , Colors.purple_to_blue)
    System.Clear()
    print(Colorate.Vertical(Colors.purple_to_blue , Hologram))
    print(Colorate.Vertical(Colors.purple_to_blue , "Prefix = H:"))
    print()
    print(Colorate.Vertical(Colors.purple_to_blue , "Spam Commands = alawackbar"))
    print()

    Thread(target=Spam, args=[message]).start()

    bot.run(token)
       
Menu()
