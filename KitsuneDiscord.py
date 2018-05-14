# ported to discord by exofeel
# orginally coded by @4201337
# ported to python3 by brensalsa

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
import urllib.request
import datetime
import os


bot = commands.Bot(command_prefix='*')


#myLock = LockPool()
#myPool = ThreadPool(myThreads)




number_of_servers = len(bot.servers)
#current_server = await bot.change_presence(game=discord.Game(name='servers: {}'.format(number_of_servers)))



social_networks = {"instagram": "https://www.instagram.com/", "twitter": "https://www.twitter.com/", "youtube": "https://www.youtube.com/", "reddit": "https://www.reddit.com/user/"}
social_network_prefix = {"instagram": "@", "twitter": "@", "youtube": " ", "reddit": "/u/"}


@bot.event
async def on_ready():
    print("Kitsune is ready.")
    number_of_servers = len(bot.servers)
    await bot.change_presence(game=discord.Game(name='Prefix: %'.format(number_of_servers)))

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Kitsune is a simple discord bot that can do social network scraping!", colour=discord.Colour(0xffb25d), description="Please read fully all commands.", timestamp=datetime.datetime.utcfromtimestamp(1526316493))

    embed.set_image()
    embed.set_thumbnail()
    embed.set_author(name="Kitsune Help Command")
    embed.set_footer(text="Kitsune")

    embed.add_field(name="Default Prefix", value="the prefix currently is %. We will add support for changing the prefix in chat. However you can change the prefix in the source code.")
    embed.add_field(name="%kitsune", value="Usage: \n```%kitsune [network] [username]``` \nThe current supported social networks are \n\n-Reddit\n-Instagram\n-Twitter\n- and YouTube.\n")
    embed.add_field(name="%batch", value="Kitsune can do batches of usernames inside a .txt file. Please. Seperate each username with a different line. Any other can break the bot and make the social network think weirdly about future requests.\n\nUsage:\n```%batch [network] [url to .txt file]```")
    embed.add_field(name="Have a suggestion?", value="Contact the developers on discord!", inline=True)
    embed.add_field(name="Donate?", value="Sure we take cypto.\n \n**VTC**:*VhYdqgeBmudv3wuDwNB4VhuQzNjK3Rw9n7* \n**ETH**:*0x6CC93E2E2D4dd0430Bab5d8Bb71a395090B84026*", inline=True)

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def batch(ctx, network, url, force="false"):
    r = requests.get(url)
    #usernames = []
    f = open('temp.txt', 'w+')
    f.write(r.text)
    with open('temp.txt','r') as f:
        usernames = [line.strip() for line in f]
        print(usernames)
        username_count = len(usernames)
        if force == "true":
            if username_count >= 999:
                await bot.say("I'm sorry but 75 usernames is the limit.\nPlease, remove some before continuing.")
            else:
                pass   
        else:
            await bot.say("Usernames detected: {}".format(username_count))
            try:
                    available_names = []
                    unavailable_names = []
                    error_names = []
                    available_names_number = len(available_names)
                    unavailable_names_number = len(available_names)
                    scraped_usernames = available_names_number + unavailable_names_number
                    embed = discord.Embed(title="Kitsune Username Scraper.", colour=discord.Colour(0xfe139e), description="Loading!", timestamp=datetime.datetime.utcfromtimestamp(1526305073))

                    embed.set_thumbnail(url="http://www.slashfilm.com/wp/wp-content/images/Zootopia-Nick-Wilde.jpg")
                    embed.set_footer(text="Kitsune username scraper")

                    embed.add_field(name="Available names ✅", value="{}".format(available_names))
                    embed.add_field(name="Unavailable names :no_entry:", value="{}".format(unavailable_names))
                    embed.add_field(name="Names that returned an error. :warning:", value="{}".format(error_names))

                    message = await bot.say(embed=embed)
                    message
                    for x in usernames:
                        print("Checking username {}".format(x))
                        social_url = social_networks[network]
                        req = requests.get(social_url + x, headers = {'User-agent': 'Kitsune username checker'})
                        username_prefix = social_network_prefix[network]
                        if req.status_code == 200:
                            unavailable_names.append(x)
                            #available_names_number = len(available_names)
                            #unavailable_names_number = len(available_names)
                        elif req.status_code == 404:
                            #await bot.say("{}{} is Available.".format(username_prefix, username))
                            available_names.append(x)
                            #available_names_number = len(available_names)
                            #unavailable_names_number = len(available_names)
                        else:
                            #x.append(error_names)
                            error_names.append(x)
                            names_list = str(available_names)
                            #available_names_number = len(available_names)
                            #unavailable_names_number = len(available_names)
                            #await bot.say(available_names)
                        embed = discord.Embed(title="Instagram Username Scraper", colour=discord.Colour(0xfe139e), description="A total number of {} were scraped.".format(len(usernames)), timestamp=datetime.datetime.utcfromtimestamp(1526305073))
                        if network == "instagram":
                            embed = discord.Embed(title="Instagram Username Scraper", colour=discord.Colour(0xfe139e), description="A total number of {} were scraped.".format(len(usernames)), timestamp=datetime.datetime.utcfromtimestamp(1526305073))
                            embed.set_thumbnail(url="https://instagram-brand.com/wp-content/uploads/2016/11/app-icon2.png")
                            pass
                        elif network == "twitter":
                            embed = discord.Embed(title="Twitter Username Scraper", colour=discord.Colour(0x20c0eb), description="A total number of {} were scraped.".format(len(usernames)), timestamp=datetime.datetime.utcfromtimestamp(1526305073))
                            embed.set_thumbnail(url="http://logos-download.com/wp-content/uploads/2016/02/Twitter_logo_bird_transparent_png-700x568.png")
                            pass
                        elif network == "reddit":
                            embed = discord.Embed(title="reddit Username Scraper", colour=discord.Colour(0xf08a0d), description="A total number of {} were scraped.".format(len(usernames)), timestamp=datetime.datetime.utcfromtimestamp(1526305073))
                            embed.set_thumbnail(url="https://is5-ssl.mzstatic.com/image/thumb/Purple125/v4/36/b8/a9/36b8a9e3-55ff-d52c-ea7e-974414f925f0/source/100x100bb.jpg")                         
                        else:
                            await bot.say("error? did you use an actual network, if so how did you get past?")
                        embed.set_footer(text="Kitsune username scraper")

                        embed.add_field(name="Available names ✅", value="{}".format(available_names))
                        embed.add_field(name="Unavailable names :no_entry:", value="{}".format(unavailable_names))
                        embed.add_field(name="Names that returned an error. :warning:", value="{}".format(error_names))
                        await bot.edit_message(message, embed=embed)
                    await bot.say("Done scraping ✅")
                    os.remove(temp.txt)
            except Exception as e:
                await bot.say(":warning: Critical Error! {}".format(e))

@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def kitsune(ctx, network, username):
    try:
        try:
            social_url = social_networks[network]
            req = requests.get(social_url + username, headers = {'User-agent': 'Kitsune username checker'})
            username_prefix = social_network_prefix[network]
            if req.status_code == 200:
                #await bot.say("{}{} is unavailable.".format(username_prefix, username))
                if network == "twitter":
                    embed = discord.Embed(title="Twitter Request", color=0x20c0eb)
                    embed.add_field(name="Username", value="{}".format(username_prefix + username))
                    embed.add_field(name="Status", value="Unavailable")
                    await bot.say(embed=embed)
                elif network == "instagram":
                    embed = discord.Embed(title="Instagram Request", color=0xfe139e)
                    embed.add_field(name="Username", value="{}".format(username_prefix + username))
                    embed.add_field(name="Status", value="Unavailable")
                    await bot.say(embed=embed)
                elif network == "reddit":
                    embed = discord.Embed(title="Reddit Request", color=0xf08a0d)
                    embed.add_field(name="Username", value="{}".format(username_prefix + username))
                    embed.add_field(name="Status", value="Unavailable")
                    await bot.say(embed=embed)
            elif req.status_code == 404:
                #await bot.say("{}{} is Available.".format(username_prefix, username))
                if network == "twitter":
                    embed = discord.Embed(title="Twitter Request", color=0x20c0eb)
                    embed.add_field(name="Username", value="{}".format(username_prefix + username))
                    embed.add_field(name="Status", value="Available")
                    await bot.say(embed=embed)
                elif network == "instagram":
                    embed = discord.Embed(title="Instagram Request", color=0xfe139e)
                    embed.add_field(name="Username", value="{}".format(username_prefix + username))
                    embed.add_field(name="Status", value="Available")
                    await bot.say(embed=embed)
                elif network == "reddit":
                    embed = discord.Embed(title="Reddit Request", color=0xf08a0d)
                    embed.add_field(name="Username", value="{}".format(username_prefix + username))
                    embed.add_field(name="Status", value="Available")
                    await bot.say(embed=embed)
             else:
                await bot.say("Error! *{}*".format(req.status_code))
        except Exception as e:
            await bot.say(":warning: **Critial error!**  \n{}".format(e))
    except CommandOnCooldown as p:
        await bot.say("{}".format(p))



@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        userID = (ctx.message.author.id)
        await bot.send_message(ctx.message.channel,"<@%s>: **Please provide a social media and/or a username.**" % (userID))
        await bot.delete_message(ctx.message)
    elif isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
        userID = (ctx.message.author.id)
        await bot.send_message(ctx.message.channel, "{} :snowflake You're on cooldown.".format(ctx.message.author.mention))

bot.run('NDQ0NzU3MzA4NDA5NjQzMDA5.DdgkDA.-8Zt4-dczbzJNbEA97MdfsMHhlg')
