# let the python to guess a number and we are trying to find out the number
import random

print("well come \nwhat is your name:")
name=input()
print(f"well hello {name}\n\n")
print("let you to guess or computer to guess\nenter you name to play\nenter 'c' to let computer play\nenter EXIT to exit\n\n")
prmchoise=input("enter hear:")
cnd=True
while (cnd):
   pass
    
def guessGame():
    if prmchoise==name:
        print("\nim going tho guess a random number in detween (1 to 10) \nand you have to find that number bay providing me the number below \nif you dont want ot play it enter 0 for play write ok\nok")
        # def RandomNum():
        #     return random.randint(1,10)
        random_number=random.randint(1,10)

        condition=True
        choise=input("enter hear:")
        if choise=='ok':
            while (condition):
                        print("\nstart guessing the number")
                        print("tho exit enter 20\n")
                        guess=int(input("enter the numbe hear:"))
                        print(f"you entered {guess}")
                        computerguess=int(random_number)
                        if guess==computerguess:
                            print("yee your guesst it correctly")
                            print(computerguess)
                            condition=False
                            exit()
                        elif guess==20:
                            print("exiting....")
                            condition=False
                            exit()
                        elif guess>computerguess:
                            print("your number is to heigh..!")
                        elif guess<computerguess: 
                            print("your number is to low..!")
        elif choise=='0':
            # condition=False
            exit()
            # break
        else:
            print("not a valid answore")
    elif prmchoise=='c':
        print("chuse a number in your mind i will try to guess the number")
        print("if you dont want ot play it enter 0 for play write ok\nok")
        choise2=input("\nenter hear:")
        if choise2=='ok':
            print("great lets start the game")
            usernum=int(input("enter your chusen number:"))
            cond=True
            def pyrandom():
                return random.randint(1,10)
            while cond:
                print("traing....")
                # print(f'i guessted{pyrandom}')
                cmpguess=pyrandom()
                if cmpguess==usernum:
                    print(f'i guessted {cmpguess}')
                    print("yes you are correct")
                    code=False
                    exit()
                    break
        elif choise2=='0':
            print('\nexiting from hear.....')
            exit()
        else:
            print("\ninvalid option you chusen....!")
    elif prmchoise=='EXIT':
        print('your now exxited...') 
        cnd=False
        exit()
    else:
        print("invalid option....")
        print("please try again...")
        exit()