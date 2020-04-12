'''Program to make Rock Paper Scissor Game 

Developer:Aakash
Date:02.04.2020
--------------------------------'''

# Print the Game Instruction to the User/Player 
print("Winning Rules of the Rock Paper Scissor Game as follows: \n"
                                +"\tRock  vs paper   -> paper wins \n"
                                +"\tRock  vs scissor -> Rock wins \n"
                                +"\tpaper vs scissor -> scissor wins \n") 
u=0;c=0;d=0
while True:

    # Tell User to enter either Rock, Paper, Scissor    
    print("Enter choice \n 1. rock \n 2. paper \n 3. scissor \n") 
    
    while True:
        # Get the response from the User 
        user_choice = input("User turn: > ") 
        user_choice = user_choice.lower()
        
        if user_choice not in ['rock','paper','scissor']:
            print ("Wrong input, please input again: ")
        else:
            break
 
    # Print the response from the User 
    print("User has choosen : " + user_choice + "\n") 
    

    
    # Computer chooses randomly between Rock, Paper and Scissor
    import random
    comp_choice = random.choice(['rock','paper','scissor']) 

    # Print computers choice
    print("Computer choice is: " + comp_choice + "\n") 
  
    # Print User Choice and Computer Choice
    print("\t" + user_choice + "\n V/s \n" + "\t"+ comp_choice) 
    

    # Decide the condition of wining according to the Game Instructions
    result = None
    
    if((user_choice == "rock" and comp_choice == "paper") or
      (user_choice == "paper" and comp_choice == "rock" )): 
        result = "paper"
    elif((user_choice == "rock" and comp_choice == "scissor") or
        (user_choice == "scissor" and comp_choice == "rock")): 
        result = "rock"
    else: 
        result = "scissor"
    

    # Compare the result with user and computer 
    # Printing either user or computer wins  
    if (user_choice == comp_choice):#additional
        d=d+1
        print("<== Draw ==>")
        print("<==",d,"times ==>")
    elif (result == user_choice):
        u+=1
        print("<== User wins ==>")
        print("  <==",u,"times ==>")
    else:
        c=c+1
        print("<== Computer wins ==>")
        print("  <==",c,"times ==>")


    # Get the response from User to Play Again    
    ans = input("Do you want to play again ? (Y/N) > ")
  
    # Check the response from User and continue the loop
    # Otherwise break the loop to close the game
    if(ans == 'n' or ans == 'N') :
        print("\nFinal Score:\n")
        print("Computer Score:",c)
        print("Draw Score:",d)
        print("User Score:",u)
        break
    
        
# Print a Thanks Message to the user
print("\nThanks for playing Rock Paper Scissor Game \n") 
