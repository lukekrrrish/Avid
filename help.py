#help.py

from mains import *
avid.remove_command("help")


os.system('cls' if os.name == 'nt' else 'clear')
@avid.event
async def on_ready():
    print(f'''{Fore.BLUE}
                    _        _     _
                   / \__   _(_) __| |
                  / _ \ \ / / |/ _` |
                 / ___ \ V /| | (_| |
                /_/   \_\_/ |_|\__,_| 
 ------------------------------------------------------------
|   Prefix : {discords.vars.prefix}                         
|                                                           
|    User : {discords.vars.user}                                      
|                                                            
|    Token : {discords.vars.token}                           
|                                                            
|    guilds : {discords.vars.guilds}                             
|                                                            
|    version : {discords.vars.__version__}                   
|
 ------------------------------------------------------------ 
{change_log}
            ''' + Fore.RESET)

@avid.command()
async def help(catagory = None):
    cata = str(catagory).lower
    if cata == None:
        pass
    if cata == "music":
        pass




