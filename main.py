# GLOBAL VARIABLES
play_game = False
time = None
player = None
score = None
grade = None
difficulty = None


# INTRODUCTION
print("""

     Welcome to: 
      
    __________                 .___             _________                            .__                
    \______   \ ___________  __| _/___________  \_   ___ \_______  ____  ______ _____|__| ____    ____  
     |    |  _//  _ \_  __ \/ __ |/ __ \_  __ \ /    \  \/\_  __ \/  _ \/  ___//  ___/  |/    \  / ___\ 
     |    |   (  <_> )  | \/ /_/ \  ___/|  | \/ \     \____|  | \(  <_> )___ \ \___ \|  |   |  \/ /_/  >
     |______  /\____/|__|  \____ |\___  >__|     \______  /|__|   \____/____  >____  >__|___|  /\___  / 
            \/                  \/    \/                \/                  \/     \/        \//_____/  

    
      INTRODUCTION: 
      
    You are a new Police Officer at the border crossing between the Republic of Arendale and the former Republic
    of Argonia. 

    Arendale and Argonia fought an asymetric war for the past few decades and the tensions are still high between 
    both people. The history is filled with Hostilities that often led to Terror Attacks and Bombings on civilians 
    and military targets alike. 
      
    Recently, Arendale occupied Argonia and overthrew the Government. 
      
    For now, the situation is stable enough so that boder crossings are possible, but there are still Religious 
    Fanatics and zealous Nationalists that are not happy with the current situation and would like to see nothing 
    more, than to end this fragile peace. 

    On top of all, there are criminals and human trafficker that try to cease the opportunity and prey on the suffering
    civilians in the Occupied Terretories of Argonia.  
      
    All kinds of people are lining up at the border crossing and it is your job to decide who may enter and who may not. 
      
  
      HOW THE GAME WORKS:
      
    You will be presented with a number of individuals that seek entry into the Occupied Terretories and you only have
    a certain amount of time to spend during your shift. 
      
    Each individual will present you his passport and you will get a readout of the description. 
      
    You can either decide to further examine the individual and his belongings by typing:
      
      "luggage" to examine his belongings, or
      "search" to search the individual, or
      "question" to inquire about the reasons for enter. 

    But beware! Each of these Actions take time and you have only a certain amount of time left until your shift ends.   

    If you came to a conclusion, you have two options. You can either: 
      
      "DENY" the request for entry and send the individual back, or 
      "APPROVE" the request for entry and let the individual enter the Occupied Terretories. 

      The Choice is yours, but beware of unforseen consequences!


      DIFFICULTY LEVEL

    You can choose between three difficulty levels. Each level grants you a different amount of time until your shift ends. 
    Easier tiers give you more time to be inquisitive about entry requests.  
      
    "hard"    30 minutes until the end of your shift.
    "medium"  45 minutes until the end of your shift.
    "easy"    60 minutes until the end of your shift.    

      
      WINNING CONDITION:

    1. If your shift ends and there are still people waiting, you lose! 
      
    2. If you work through all the cases by the end of your shift, you get a detailed perfomance evaluation resulting in 
      a performance score between 0 to 100 and a Grade. 

        95 to 100 = A Grade
         85 to 94 = B Grade
         75 to 84 = C Grade
         65 to 74 = D Grade
         55 tp 64 = E Grade
          0 tp 54 = F Grade
      
    
      RESTART
      
    You may allways "restart" your shift and reset the game!          

    """)

# preparations 
player = input("""
               
    What is your name Rookie?

    """)

difficulty = str(input("Select your difficulty level: hard, medium, easy:"))
if difficulty.lower == "hard":
    time = 30
    print("""You have """ + str(time) + """ minutes until your replacement arrives and your shift ends.""")
elif difficulty.lower == "medium":
    time = 45
    print("""You have """ + str(time) + """ minutes until your replacement arrives and your shift ends.""")
elif difficulty.lower == "easy":
    time = 60
    print("""You have """ + str(time) + """ minutes until your replacement arrives and your shift ends.""")
else:
    print("You have to chose between 'easy', 'medium' or 'hard'")

print(time)    ### BUGGY



print("""
      
    You shift has not yet started!
      
    """)

if not play_game:
    start_game = input("""

    You can start your shift whenever you are ready. 
                       
    Type "begin" to start shift. 

    """)
    if start_game.lower() == "begin":
        play_game = True
        print("""
    
    Welcome to your first shift """ + str(player) + """!
              
    It is your job to decide who may enter the Occupied Terretory of Argonia and who may not. 

    Be careful who you let into the country. There are dangerous people and criminals out there and we are 
    sitting on a bucket of shit that is about to hit the fan if something goes sideways. 
              
    But there are also good people out there that we need to help and that will better the situation in the 
    Occupied Terretories.

    Ultimately, the decision is yours.  

    You have """ + str(time) + """ minutes until your replacement arrives and your shift ends. 

    Good Luck!                   

    """)
        
        print(play_game)