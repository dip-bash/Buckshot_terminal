# round one
def RoundOne():
    print("There is 3 bullets, TWO is empty round and ONE is full....\nlets start the game....")
    bullets = ["T","F","F"]    
    random.shuffle( bullets )
    i=0
    while i >= 0:
        RemainingBullets=3-i

        if(RemainingBullets>1):
            print(f">> {RemainingBullets} << bullets are remainning")
        else:
            print(f">> {RemainingBullets} << bullet is remainning")

        UserChoice=input("if you want to shoot yourself type 'y'\nif you want to shoot me type 'n';\n=> your choice is: ",)

        if(UserChoice=="y" or UserChoice=="Y"):
            if(bullets[i]=="T"):
                print("+> Round is full\nYou lose my friend...now your soul is mine....XD\n")
                exit()
            elif(bullets[i]=="F"):
                print("The round is empty....\nnow the next turn is also yours:)\n")
                i+=1
        elif(UserChoice=="n" or UserChoice=="N"):
            if(bullets[i]=="T"):
                print("+> Round is full\nYou won Round One..... \n")
                exit()
            elif(bullets[i]=="F" and bullets[i]!=2):
                print("The round is empty.....\n")
                if(RemainingBullets>1):
                    print(f">> {RemainingBullets} << bullets are remainning")
                else:
                    print(f">> {RemainingBullets} << bullet is remainning")
                i+=1
                print("It's my turn....be ready.....\n")
                if(bullets[i]=="T"):
                    print("You lose my friend...now your soul is mine....XD\n")
                    exit()
                elif(bullets[i]=="F"):
                    print("round is empty...now your turn")
                    i+=1
            else:
                print("round is empty..you won....because that's the last bullet")
                
            


# starting(1)
import random
checkLuck=input("Do you want to check your luck (y/n): ")
if(checkLuck=="y"):
    print("let's begain the game of death........\n")
elif(checkLuck=="n"):
    print("AS EXPECTED ANSWER FROM A WEAK HUMAN....")
else:
    print("Are you stupid or acting like a stupid...whatever...GETOUT")
RoundOne()



