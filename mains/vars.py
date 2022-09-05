#vars.py

from mains.imports import *



class vars():
    blue = Fore.BLUE
    magant = Fore.MAGENTA

class discords():
    class vars():
        token = "MTAxNDYyNjY2Nzc1NjUyNzc0Ng.Gn2GQm.TLNmw5wtr4QRq54lhx3bjL64TzDq5DYPFPA9L0"
        prefix = "\\"
        client_id = "1014626667756527746"
        secret_id = ""
        __version__ = 1.5
        avid = commands.Bot( description = "This is Avid bot it's  made by many of my BFF'S", command_prefix = prefix, intents = Intents.all())
        guilds = len(avid.guilds)
        user = avid.user
        discord_color = discord.Colour.random
        help_appends = []
        help_value = []
    class defs():
        async def cata_None(ctx):
            embed = discord.Embed(color = discords.vars.discord_color, timestamp = ctx.message.created_at)
            embed.set_author(name = f" Avid's | prefix: {avid.command_prefix}, icon_url = client.user.avatar_url")
            embed.add_field(name = f"`{discords.vars.help_appends}`", value = f"{discords.vars.help_value}", inline = False)
            # embed.add_field(name = "\uD83E\uDDCA `all`", value="Shows many of the commands", inline=False)
            await ctx.send(embed = embed)
        async def cata_music(ctx):
                embed = discord.Embed(color = discords.vars.discord_color, timestamp = ctx.message.created_at)
                embed.description(f"`music songs`", value = "playes the song")
                embed.add_field(name = "play", value = "play + song", inline = False)
                await ctx.send(embed = embed)
        async def cata_lb(ctx):
            embed = discord.Embed(color = discords.vars.discord_color, timestamp = ctx.message.created_at)
            embed.description()
            await ctx.send( embed = embed)




class RunDefOnReady():
    pass
    #discords.defs.run()


class defs():
    pass




class users():
    class lukekrrish():
        pass


avid = discords.vars.avid

if discord.errors.LoginFailure:
    avid.run(discords.vars.token)
else:
    print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
    os.system('pause')

change_log = f'''
 _____________________________________________________
|{vars.magant} lukekrrish : added and changed some of the templates{vars.blue}|
|
|
|
''' + Fore.RESET