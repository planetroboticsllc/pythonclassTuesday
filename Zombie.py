from turtle import *
print ("hello their. it is the year 2099 and the zombie apacolipse of Boston Massachusetts has begun.\n you must find your way around the city and make it to the harbor.\n and take a boat out to saftye, but first you must find somewhere to hide")
#the players first choice
print ("you have made it out of your aparment, but you need a place to hide!\n")

choice1 = input("Will you 1. Hide at the Muesem of Fine Arts, or\n 2. Try fight your way to the harbor\n")
if choice1 == "1":
    print ("you have sucessflly snuck into the muesem of fine arts and have found a place to hide a mummy's tomb!\n")
if choice1 == "2":
    print ("you took out a couple of zombies with the weapon you chose, but their was to many of them. YOU LOSE!!!! Exit off the tab and try again.\n")
    choice2 = input("Will you 1. sneak out the back exit and climb to the top of the roof, or\n 2. or take and old artifact knife and book it\n")
    if choice2 == "1":
        print ("You managed to climb halfway up but slipped and fell into the zombies thirsty mouthes.\n You lost exit to restart\n")
    if choice2 == "2":
        print ("The ancient knife you found was acutlly vibranium and you were able to take \n out some zombies and get to a nearby police station!\n")
        print ("you are in the police station but accidentlly dropped your vibranium knife down a crack.\n You now need a vehicle to escape!\n")
        choice3 = input("Will you 1. Take the motorcycle or\n 2. Take the helicopter\n")
        if choice3 == "1":
            print ("the motorcycle is in great shape but can only get you halfway to the harbor.\n")
        if choice3 == "2":
            print ("the helicopter is out of gas, is filled with zombies and the wings are broken. \n YOU LOST exit to restart.\n")
            print ("the farthest you can get to the harbor is fenway park.\n")
            choice4 = input("Will you 1. try to go to the charles river and take a boat down the river or 2. \n take big pappies baseball bat and fight your way down to the harbor thorugh the historic streets of Boston.\n")
            print ("You got down to the river succesfelly and their were no zombies.\n")
            if choice4 == "2":
                print ("that bat was so old that is snapped the moment you hit the first zombie. \n you tried to run away but the zombies caught up to you. \nYOU DIE exit the game to restart.\n")
                print ("you are at the river and their are two boats wating for you to take you down to the harbor.\n")

                choice5 = input ("Will you 1. Swim a 30 yards to take a swan boat down or 2. Take the kayack right next too you\n.")
                if choice5 == "1":
                    print("You succsefully swam to the swan boat and are on you way to the boston harbor \n where you can escape on jeff bezos yacht worth 5 million dollars complete with a spa, gym and indoor pool.\n")
                if choice5 == "2":
                    print("their was a hole in the kayack and a fishie zombie pulled you down into \n the deep waters of the charles. YOU LOSE\n.")

                    choice6 = input ("you have made your way down to the boston harbor. \n you are about to board into jeff bezos's yacht. \n however, their is zombies gaurding the entrance.do you \n1. call up jeffy besoz to save you with his 30 million dollar robot army to save you armed with elon musks electirc zombie zappers, or\n 2. yell can i get a hoya and hope someobody saves you.\n")
                    if choice6 == "1":
                        print ("succes! JEFF BEZOS ARMY HAS ARRIVED and they killed the zombies gaurding the door.\n you are no esaping to the phillpeins and waiting for you their is joe biden.\n.")
                    if choice6 == "2":
                        print ("you have come so far only to fail. \n you screamed can i get a hoya at the top of your lungs but noboyd heard you. \n they sureounds you then they eat  your brains.\n")
              
                
