# loaded_c04 = "c #debugging04 loaded successfully"
# print(loaded_c04)

from main import time # imports the time remaining value from main
c04_conclusion = None # Final Conclusion State for this case

c04_01 = str("""
             
        Name: tbd
        Date of Birth: tbd
        Place of Birth: tbd
             
        c04 OVERVIEW
        XXXDUMMYTEXTXXX
             
        """)

print(c04_01)
print("You have " + str(time) + " minutes remaining.")

while c04_conclusion == None:
    c04_01_des = str(input("""
                       
        How do you want to proceed? 

          Make A Descision:                               
        "DENY"    the request for entry and send the individual back, or 
        "APPROVE" the request for entry and let the individual enter the Occupied Terretories.

          Further Investigate:                              
        "luggage" to examine his belongings, or
        "search"  to perform a full body search on the  the individual, or
        "question" to inquire about the reasons for enter. 
                       
        """))
    if c04_01_des == 'APPROVE':
        time = (time - 1) 
        c04_conclusion = 1
        print("""
        
        c04 APPROVE
        XXXDUMMYTEXTXXX
        
        """)
    elif c04_01_des == 'DENY':
        time = (time - 2) 
        c04_conclusion = 2
        print("""
        
        c04 DENY
        XXXDUMMYTEXTXXX
        
        """)
    elif c04_01_des == 'search':
        time = (time - 10)
        print("""
        
        c04 search
        XXXDUMMYTEXTXXX
                  
        """)
    elif c04_01_des == 'luggage':
        time = (time - 5) 
        print("""
        
        c04 luggage
        XXXDUMMYTEXTXXX
                  
        """)
    elif c04_01_des == 'question':
        time = (time - 5) 
        print("""
        
        c04 question
        XXXDUMMYTEXTXXX
                  
        """)
else:
    time = (time - 10) 
    print("""
          
        c04 else
        XXXDUMMYTEXTXXX
        
        """)
    
print(c04_conclusion)    

print("You have " + str(time) + " minutes remaining.")