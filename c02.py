# loaded_c02 = "c02 loaded successfully"  #debugging
# print(loaded_c02)  

from main import time # imports the time remaining value from main
from main import score # imports the score value
from main import people_left # people left
c02_conclusion = None # Final Conclusion State for this case
c02_conclusion_good = "c02 GOOD OUTCOME"
c02_conclusion_bad = "c02 BAD OUTCOME"
c02_conclusion_secret = "c02 SECRET OUTCOME" # unused at the moment

c02_01 = str("""
             
        Name: tbd
        Date of Birth: tbd
        Place of Birth: tbd

        c02 OVERVIEW    
        XXXDUMMYTEXTXXX
             
        """)

print(c02_01)
print("You have " + str(time) + " minutes remaining.")

while c02_conclusion == None:
    c02_01_des = str(input("""
                       
        How do you want to proceed? 

          Make A Descision:                               
        "DENY"    the request for entry and send the individual back, or 
        "APPROVE" the request for entry and let the individual enter the Occupied Terretories.

          Further Investigate:                              
        "luggage" to examine his belongings, or
        "search"  to perform a full body search on the  the individual, or
        "question" to inquire about the reasons for enter. 
                       
        """))
    if c02_01_des == 'APPROVE':
        time = (time - 1) 
        score = score + 10 # TBD
        people_left = people_left - 1
        c02_conclusion = c02_conclusion_good
        print("""
        
        c02 APPROVE      
        XXXDUMMYTEXTXXX
        
        """)
    elif c02_01_des == 'DENY':
        time = (time - 2) 
        score = score + 1
        people_left = people_left - 1
        c02_conclusion = c02_conclusion_bad
        print("""
        
        c02 DENY      
        XXXDUMMYTEXTXXX
        
        """)
    elif c02_01_des == 'search':
        time = (time - 10)
        print("""
        
        c02 search      
        XXXDUMMYTEXTXXX
                  
        """)
    elif c02_01_des == 'luggage':
        time = (time - 5) 
        print("""
        
        c02 luggage      
        XXXDUMMYTEXTXXX
                  
        """)
    elif c02_01_des == 'question':
        time = (time - 5) 
        print("""
        
        c02 question      
        XXXDUMMYTEXTXXX
                  
        """)
    else:
        time = (time - 10) 
        score = score + 5
        people_left = people_left -1
        c02_conclusion = c02_conclusion_bad
        print("""

        c02 else
        XXXDUMMYTEXTXXX
        
        """)
    
print(c02_conclusion) 
print(score) 

print("You have " + str(time) + " minutes remaining.")