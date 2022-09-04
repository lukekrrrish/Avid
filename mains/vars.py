from .imports import *

change_log = f'''

{Fore.LIGHTBLACK_EX}lukekrrish : added and changed some of the templates














'''


class discords():
    class vars():
        intent = discord.Intents().all()
        token = "MTAxNDYyNjY2Nzc1NjUyNzc0Ng.G3Luih.CXS3BSxlyak7ncb6C_LzOgUqbPERkxFGIuCeow"
        prefix = "\\"
        client_id = "1014626667756527746"
        secret_id = "LGXTS2ZqEzfpafAKe2dVyoK4fSwOkv56"
        __version__ = 1.5
        avid = commands.Bot( description = "This is Avid bot it's  made by many of my BFF'S", command_prefix = prefix, intents = intent)
    class defs():
        def discord_run():
            token = discords.vars.token
            client = discords.vars.avid
            try:
                client.run(token)
            except discord.errors.LoginFailure:
                print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
                os.system('pause')
        def run():
            avid = discords.vars.avid
            os.system('cls' if os.name == 'nt' else 'clear')
            @avid.event
            async def on_ready():
                print(f'''{Fore.RED}
                _        _      _
               / \__   _(_) __| |
              / _ \ \ / / |/ _` |
             / ___ \ V /| | (_| |
            /_/   \_\_/ |_|\__,_|                                                                                                        
             ------------------------------------------------------------
            |    Prefix : {discords.vars.prefix}                         |
            |                                                            |       
            |    User : {avid.user}                                      |
            |                                                            |       
            |    Token : {discords.vars.token}                           |
            |                                                            |
            |    guilds : {len(avid.guilds)}                             |
            |                                                            |
            |    version : {discords.vars.__version__}                    |
            |
            |   {change_log}    
             ------------------------------------------------------------ 
            ''' + Fore.RESET)



class RunDefOnReady():
    discords.defs.run()


class defs():
    pass




class users():
    class lukekrrish():
        pass


avid = discords.vars.avid
