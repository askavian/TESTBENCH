time_remaining = 30

abl_01 = str("""
             Name: Abdul Rahim
             Date of Birth: Dec.11th 1999
             Place of Birth: Erbil, Iraq
             
             The passport was recently issued and shows no obvious signs of damage or manipulation. 
             
             You recognize the person in front of you as the same person shown on the passport photo. 
             
             The eyes are the same; the shape of the ears is the same and you recognize a birthmark beneath the left eye.

             However, in his passport, the person has a full beard and hair. The man in front of you is bald and fully shaven.
             """)

print(abl_01)
print("You have " + str(time_remaining) + " minutes remaining.")

abl_01_des = None

abl_01_des = str(input("How do you want to proceed? 'Let him pass.' or 'Refuse Entry' or 'Perform full check'?"))
if abl_01_des == 'Let him pass.':
    time_remaining = (time_remaining - 1) 
    print("""
          Abdul Rahim passes through the border crossing uninterrupted. 
          
          You missed the 2kg of C4 Abdul was carrying. 
          
          As you hear from the News later that evening, Abdul detonated the bomb he was carrying in a bus 
          en-route to the city, killing 15 people.
          
          You are a terrible Immigration Officer.
          
          You lose!
          """)
elif abl_01_des == 'Refuse Entry':
    time_remaining = (time_remaining - 2) 
    print("""
          Abdul Rahim is shouting about racial profiling and why you refuse him. 
              
          But ultimately he leaves the border crossing and returns.
          """)
elif abl_01_des == 'Perform full check':
    time_remaining = (time_remaining - 15) 
    print("""
          You perform a full check on Abdul and his belonging. 
                  
          You find 2kg of C4 and a detailed list of a planned attack in the city.
                  
          Abdul is arrested!
                  
          You are a hero!
                  
          You win!
          """)
else:
    time_remaining = (time_remaining - 10) 
    print("Abdul gets bored and leaves after a while.")

print("You have " + str(time_remaining) + " minutes remaining.")