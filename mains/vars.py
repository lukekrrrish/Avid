#vars.py

from mains.imports import *


change_log = f'''
{Fore.LIGHTBLACK_EX}lukekrrish : added and changed some of the templates
'''


class discords():
    class vars():
        token = "MTAxNDYyNjY2Nzc1NjUyNzc0Ng.GgiwxP.WC2TFIryi0Y-7AKly5l7b_bNEZJr_k3mJ4dBJo"
        prefix = "\\"
        client_id = "1014626667756527746"
        secret_id = ""
        __version__ = 1.5
        avid = commands.Bot( description = "This is Avid bot it's  made by many of my BFF'S", command_prefix = prefix, intents = Intents.all())
    class defs():
        def discord_run():
            token = discords.vars.token
            avid = discords.vars.avid
            if discord.errors.LoginFailure:
                avid.run(token)
            else:
                print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
                os.system('pause')




class RunDefOnReady():
    pass
    #discords.defs.run()


class defs():
    pass




class users():
    class lukekrrish():
        pass


avid = discords.vars.avid
