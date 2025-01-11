print("welcome to the find your match \n")

name1 = input("enter your name1 ").lower()          
name2 = input("enter your name2 ").lower() 
total = name1+name2 

at=0
al=0

for y in "true":
    at += total.count(y)
    bt = total.count(y)
    print(f"{y} occurs {bt}")  
ft = at 
print(f"Total = {ft}") 

for x in "love":
     al += total.count(x)
     bl = total.count(x) 
     print(f"{x} occurs {bl}")    
fl = al
print(f"Total = {fl}")


final = str(ft)+str(fl)
score = int(final)

if score < 10 or score > 90:
    print(f"your score is {final} you go like coke and mentos ")
elif score > 40 and score < 50:
    print(f"your score is {final} you go together")
else:
    print(f"your score is {final} try again")    

    
    
            
        
    
           
           
                
    

    
    
        