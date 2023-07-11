#implement warning message 5 minutes before night time or day time 




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
                                                
        
#!decay
    @rust_socket.command(aliases=["Decay"])
    async def decay(command: Command):                                                  #will tell you decay time dependant on what you select 
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




#!test

    @rust_socket.command(aliases=["Night", "N", "m"])                                                               #working on rust time to irl (WIP)
    async def test111(command: Command):
        currentTime = (await rust_socket.get_time()).raw_time
            

        if (0 <= currentTime <= 4):
                
            print("night")
        else:
            tillNight = 20-currentTime
            minutesTillNight = tillNight*2.5
            print(minutesTillNight)

            



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

#!xy
                                                                    #creates xy diagramm and collect data on Time https://imgur.com/kcI6hV3
    

    @rust_socket.command()                                        #Gives name and location for everyone on the team 
    async def xy(command: Command):    
           
        while True:
               

            currentTime = (await rust_socket.get_time()).raw_time
            currentTime = round(currentTime, 2)
            print(currentTime)
            await asyncio.sleep(1)
                

            if  (17.60<= currentTime <= 17.70):    #intervall weg machen y= x/60 17.y*100
                await rust_socket.send_team_message("It will be Night in 5 Minutes")
                print("It will be Night in 5 Minutes")
            elif(23.86<= currentTime <= 23.96):
                await rust_socket.send_team_message("It will be Day in 5 Minutes")
                print("It will be Day in 5 Minutes")


                
            






        
       #penis
        



            






    await rust_socket.hang()

asyncio.run(Main()) 
