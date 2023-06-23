#implement warning message 5 minutes before night time or day time 






import asyncio
from rustplus import RustSocket, CommandOptions, Command, TeamEvent

options = CommandOptions(prefix="!")
rust_socket = RustSocket("145.239.205.187",  "28089", 76561199473072288, 1509473755, command_options=options)




LoilCodes = ["OILRIG2HELI", "OILRIG2DOCK", "OILRIG2EXHAUST", "OILRIG2L1","OILRIG2L2","OILRIG2L3A","OILRIG2L3B","OILRIG2L4","OILRIG2L5","OILRIG2L6A","OILRIG2L6B","OILRIG2L6C", "OILRIG2L6D"]
BanditCampCodes = ["CASINOTOWN, WEAPONS"]
DomeCodes = ["DOME1,DOMETOP"]
SiloCodes = ["SILOEXIT1," "SILOEXIT2," "SILOMISSILE," "SILOSHIPPING," "SILOTOWER,"]
OutpostCodes = ["COMPOUNDSTREET","COMPOUNDMUSIC","COMPOUNDCRUDE","COMPOUNDCHILL", ]
SmoilCodes = ["OILRIG1HELI","OILRIG1DOCK", "OILRIG1EXHAUST", "OILRIG1L1", "OILRIG1L2", "OILRIG1L3", "OILRIG1L4" ] 

async def Main():
    await rust_socket.connect()


#!help
    @rust_socket.command(aliases=["Help", "H", "h"])
    async def help(command: Command):
        await rust_socket.send_team_message("!help, !time, !queue, !pop, !seed, !team, !promote { }, !codes { } ")

#!time
    @rust_socket.command(aliases=["Time", "T", "t"])
    async def time(command: Command):
        await rust_socket.send_team_message((await rust_socket.get_time()).time)

#!queue
    @rust_socket.command(aliases=["Queue", "Q", "q"])
    async def queue(command: Command):
        await rust_socket.send_team_message("Currently " + str((await rust_socket.get_info()).queued_players) + " players in queue!" )

#!pop
    @rust_socket.command(aliases=["Pop", "P", "p"])
    async def pop(command: Command):

        await rust_socket.send_team_message("Currently "+ str((await rust_socket.get_info()).players)   +" players connected!"  )

#!seed
    @rust_socket.command(aliases=["Seed", "S", "s"])
    async def seed(command: Command):

        await rust_socket.send_team_message("The seed is " + str((await rust_socket.get_info()).seed) )

#!Team
    @rust_socket.command(aliases=["Team" ])
    async def team(command: Command):



        info = await rust_socket.get_team_info()

        for member in info.members:
            steam_id = member.steam_id
            name = member.name
            await rust_socket.send_team_message(f"Steam ID: {steam_id}, Name: {name}")
            
#promote {}
    @rust_socket.command(aliases=["Promote"])
    async def promote(command: Command):
        args = command.args[0]
        
    
        if(args  == "help" ):
            await rust_socket.send_team_message("enter the steam id of the person to promote (!team)")
        else :

            steamID = int(command.args[0])
            await rust_socket.promote_to_team_leader(steamID)

#!codes 
    @rust_socket.command(aliases=["Codes", "Code", "code"])
    async def codes(command: Command):
        Monument = str(command.args[0].lower())
            


        if(Monument == "loil" or "large" ) :
          
            for i in LoilCodes:
                await rust_socket.send_team_message(i)

        elif(Monument  == "air" ):
            await rust_socket.send_team_message("AIRFIELDHELIPAD")

        elif(Monument  == "banditcamp" ):
            for i in BanditCampCodes:
                await rust_socket.send_team_message(i)
            
        elif(Monument  == "dome" ):
            for i in DomeCodes:
                await rust_socket.send_team_message(i)

        elif(Monument  == "silo" ):
            for i in SiloCodes:
                await rust_socket.send_team_message(i)

        elif(Monument  == "outpost" ):
            for i in OutpostCodes:
                await rust_socket.send_team_message(i)

        elif(Monument  == "smoil "  ):
            for i in SmoilCodes:
                await rust_socket.send_team_message(i)

        elif(Monument  == "help" ):
            await rust_socket.send_team_message("help, smoil, loil, outpost, silo, dome, banditcamp, air ")
            

        else:
            await rust_socket.send_team_message("This monument doesn't have camera codes or doesn't exist")
        
#!events
    @rust_socket.command(aliases=["Event", "Events","events" ])
    async def event(command: Command):
        for marker in await rust_socket.get_markers():
            print(f"{marker.name} ({marker.x},{marker.y})")   
        
#!decay
    @rust_socket.command(aliases=["Decay"])
    async def decay(command: Command):
        Bgrade = str(command.args[0].lower())#
        if(Bgrade == "wood"):
            await rust_socket.send_team_message("3 hours")
        elif(Bgrade == "stone"):
            await rust_socket.send_team_message("5 hours")
        elif(Bgrade == "metal"):
            await rust_socket.send_team_message("8 hours")
        elif(Bgrade == "hqme"):
            await rust_socket.send_team_message("12 hours")
        else:
            await rust_socket.send_team_message("12 hours")

    await rust_socket.hang()




asyncio.run(Main())





