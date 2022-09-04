from mains import *
avid.remove_command("help")




# os.system('cls' if os.name == 'nt' else 'clear')
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
|    version : {discords.vars.__version__}                   |
|                                                            |
|   {change_log}                                             |
 ------------------------------------------------------------ 
            ''' + Fore.RESET)