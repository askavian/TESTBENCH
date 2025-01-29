# loaded_c02 = "c02 loaded successfully"  #debugging
# print(loaded_c02)  

from main import time # imports the time remaining value from main
c02_conclusion = None # Final Conclusion State for this case

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
        c02_conclusion = 1
        print("""
        
        c02 APPROVE      
        XXXDUMMYTEXTXXX
        
        """)
    elif c02_01_des == 'DENY':
        time = (time - 2) 
        c02_conclusion = 2
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
    print("""

        c02 else
        XXXDUMMYTEXTXXX
        
        """)
    
print(c02_conclusion)    

print("You have " + str(time) + " minutes remaining.")