#implement warning message 5 minutes before night time or day time 
#Help by oli and oli 




from datetime import datetime

import asyncio
import math
from rustplus import RustSocket, CommandOptions, Command, TeamEvent, convert_xy_to_grid

options = CommandOptions(prefix="!")                                                                                    #creates prefix 
rust_socket = RustSocket("145.239.205.187",  "28089", 76561199473072288, 1509473755, command_options=options)           #connect to server 


x = 0

LoilCodes = ["OILRIG2HELI", "OILRIG2DOCK", "OILRIG2EXHAUST", "OILRIG2L1","OILRIG2L2","OILRIG2L3A","OILRIG2L3B","OILRIG2L4","OILRIG2L5","OILRIG2L6A","OILRIG2L6B","OILRIG2L6C", "OILRIG2L6D"]        #camera codes for !codes
BanditCampCodes = ["CASINOTOWN, WEAPONS"]
DomeCodes = ["DOME1,DOMETOP"]
SiloCodes = ["SILOEXIT1", "SILOEXIT2", "SILOMISSILE", "SILOSHIPPING", "SILOTOWER"]
OutpostCodes = ["COMPOUNDSTREET","COMPOUNDMUSIC","COMPOUNDCRUDE","COMPOUNDCHILL" ]
SmoilCodes = ["OILRIG1HELI","OILRIG1DOCK", "OILRIG1EXHAUST", "OILRIG1L1", "OILRIG1L2", "OILRIG1L3", "OILRIG1L4" ] 


"""     info = await rust_socket.get_team_info()
        member = info.members[0]  
        x_coordinate = member.w
        y_coordinate = member.y
        print(x_coordinate, y_coordinate)  

"""
#this is how you call for object and function






async def Main():
    await rust_socket.connect()

    







  
                        
               
        






#!help
    @rust_socket.command(aliases=["Help", "H", "h"])
    async def help(command: Command):
        await rust_socket.send_team_message("!help, !time, !queue, !pop, !seed, !team, !promote { }, !codes { }, !events, !decay, !night, !day")            #gives list of all commands

#!time
    @rust_socket.command(aliases=["Time", "T", "t"])
    async def time(command: Command):
        await rust_socket.send_team_message((await rust_socket.get_time()).time)            #gives time in rust 

#!queue
    @rust_socket.command(aliases=["Queue", "Q", "q"])
    async def queue(command: Command):
        await rust_socket.send_team_message("Currently " + str((await rust_socket.get_info()).queued_players) + " players in queue!" )              #checks for queue 

#!pop
    @rust_socket.command(aliases=["Pop", "P", "p"])
    async def pop(command: Command):

        await rust_socket.send_team_message("Currently "+ str((await rust_socket.get_info()).players)   +" players connected!"  )                   #checks for pop 

#!seed
    @rust_socket.command(aliases=["Seed", "S", "s"])
    async def seed(command: Command):

        await rust_socket.send_team_message("The seed is " + str((await rust_socket.get_info()).seed) )                             #gets seed

#!Team
    @rust_socket.command(aliases=["Team" ])
    async def team(command: Command):



        info = await rust_socket.get_team_info()                                            #get all team members name aswell as steam id 

        for member in info.members:
            steam_id = member.steam_id
            name = member.name
            await rust_socket.send_team_message(f"Steam ID: {steam_id}, Name: {name}")
            
#promote {}
    @rust_socket.command(aliases=["Promote"])
    async def promote(command: Command):
        args = command.args[0]
        
    
        if(args  == "help" ):
            await rust_socket.send_team_message("enter the steam id of the person to promote (!team)")              #promote someone to team leader with steam Id (Only for the person running the bot )
        else :

            steamID = int(command.args[0])
            await rust_socket.promote_to_team_leader(steamID)

#!codes 
    @rust_socket.command(aliases=["Codes", "Code", "code"])
    async def codes(command: Command):
        Monument = str(command.args[0].lower())                         #rust camera codes 
            


        if(Monument == "large" ) :
          
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
    async def event( command: Command):
        for marker in await rust_socket.get_current_events():                   
            size = (await rust_socket.get_info()).size                                                 #shows current events (WIP)
            grid = convert_xy_to_grid((marker.x, marker.y), size , False)
            await rust_socket.send_team_message(f"{grid[0]}{grid[1]}")
                                                
        



#!location  
    @rust_socket.command(aliases=["Locations", "locations", "Location"])                                        #Gives name and location for everyone on the team 
    async def location(command: Command):
        info = await rust_socket.get_team_info()
        size = (await rust_socket.get_info()).size

        for member in info.members:

            x_coordinate = member.x
           
            y_coordinate = member.y  
           
            grid  = convert_xy_to_grid((x_coordinate, y_coordinate  ), size, False)
            
           
            await rust_socket.send_team_message(member.name+ " Is at " + f"( {grid[0]}{ (grid[1]) })")

#!calc
    @rust_socket.command(aliases=["Calc"])
    async def calc(command: Command):
        args = [arg.lower() for arg in command.args]

        if args[0] == "craft":
            print(args[0])

        elif args[0] == "scrap":
            print(args[0])

        elif args[0] == "rec":
            print(args[0])

        elif args[0] == "raid":
            print(args[0])

        elif args[0] == "decay":
            if len(args) >= 3:  # Check if there are at least three arguments
                decay_material = args[1]
                decay_value = args[2]

                if decay_material == "wood":
                    x = int(decay_value) / 83
                    result = round(x, 2)
                    await rust_socket.send_team_message(str(math.trunc(x/1.66666666666*100 )) + " minutes till decay")

                elif decay_material == "stone":
                    x = int(decay_value) / 100
                    result = round(x, 2)
                    await rust_socket.send_team_message(str(math.trunc(x/1.66666666666*100)) + " minutes till decay")

                elif decay_material == "metal":
                    x = int(decay_value) / 125
                    result = round(x, 2)
                    await rust_socket.send_team_message(str(math.trunc(x/1.66666666666*100 )) + " minutes till decay")

                elif decay_material == "hqm":
                    x = int(decay_value) / 166
                    
                    await rust_socket.send_team_message(str(math.trunc(x/1.66666666666*100)) + " minutes till decay")

            else:
                await rust_socket.send_team_message("Command usage: !calc decay [material] [value]")
        else:
            await rust_socket.send_team_message("This is not a valid argument, try [scrap, rec, raid, craft, decay]")

                           


    async def nightDay():
        print("night/day tracked")
        isTime = True
        isTime2 = True

        day_message_sent = False  # Flag to track if the day message has been sent

        while isTime or isTime2:
            currentTime = (await rust_socket.get_time()).raw_time
            currentTime = round(currentTime, 2)

            await asyncio.sleep(1)

            if currentTime == 17.65 and isTime:
                await rust_socket.send_team_message("It will be Night in 5 Minutes")
                isTime = False

            elif 23.90 <= currentTime <= 23.91 and isTime2 and not day_message_sent:
                await rust_socket.send_team_message("It will be Day in 5 Minutes")
                day_message_sent = True

        # Other parts of the code or additional logic can set isTime or isTime2 back to True if needed.

    asyncio.create_task(nightDay())




   


                
            






        
    
        



            






    await rust_socket.hang()

asyncio.run(Main()) 
