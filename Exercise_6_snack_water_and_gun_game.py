#now we are making a game called:-snake water and gun
if __name__=='__main__':
 import random
 list=["s","w","g"]
 computers_turn=random.choice(list)
print("**********************welcome to the game*****************************")
print("Computer choosed their option:")
print("*********************Now this  is your turn *********************")
print("******************select an option for playing**********************")
print("s:-snake")
print("w:-water")
print("g:-gun")
player_choice=input("Enter your choice:")


if computers_turn=='s' and player_choice=='s':
    print("game is draw")
elif computers_turn=='w' and player_choice=='w':
    print("game is draw")
elif computers_turn=='g' and player_choice=='g':
    print("game is draw")
elif computers_turn=='s' and player_choice=='w':
    print("Computer won ! you lose😢😢")
elif computers_turn=='s' and player_choice=='g':
    print("You won😁 ! Computer Lose")
elif computers_turn=='w' and player_choice=='s':
    print("You won😁 !COmputer Lose")
elif computers_turn=='w' and player_choice=='g':
    print("You lose😢 ! Compupter won")
elif computers_turn=='g' and player_choice=='s':
    print("you lose 😢!Computer won")
elif computers_turn=='g' and player_choice=='w':
    print("you won 😁! Computer lose")
else:
    print("*******Seems you choose wrong option or you Enter any string or any invalid option*******")
    print("************************try again and choose valid option*********************************")
    
print("computer choosed:",computers_turn)
print("you choosed:",player_choice)

