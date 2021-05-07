import pygame
from random import randint
from timeit import default_timer as timer

communitycards = ["Advance to Go (Collect $200)", "Bank error in your favor. Collect $200",
                  "Doctor's fees. Pay $50", "Get Out of Jail Free", "Go to Jail",
                  "Collect $50 from every player", "Holiday Funds. Recieve $100", "Income tax refund. Collect $20",
                  "It is your birthday. Collect $10 from every player", "Life Insurance Matures - Collect $100",
                  "Hospital Fees. Pay $50", "School Fees. Pay $50", "Recieve $25 consultancy fee",
                  "You are assessed for street repairs: Pay $40 per house and $115 per hotel you own",
                  "You have won second prize in a beauty contest. Collect $10", "You Inherit $100",
                  "From sale of stock you get $50"]
chancecards = ["Advance to Go (Collect $200)", "Advance to Illinois Ave. If you pass go, collect $200",
               "Advance to St. Charles Place. If you pass go, Collect $200",
               "Advance ot the nearest Utility, If unowned, you may buy it from the bank. If owned, pay owner a total 10 times the amount thrown on the dice",
               "Advance to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the bank",
               "Bank pays you dividend of $50", "Get out of Jail Free", "Go back 3 spaces",
               "Go to Jail, Do not collect $200",
               "Make general repairs to all your property: for each house pay $25, For each hotel pay $100",
               "Pay poor tax of $15", "Take a trip to Reading Railroad", "Take a walk on the Boardwalk",
               "You have been elected Chairman of the Board. Pay each player $50",
               "Your building loan matures. Recieve $150", "You have won a crossword competition. Collect $100"]
brown = ["mediterranean_avenue", "baltic_avenue"]
lightblue = ["oriental_avenue", "vermont_avenue", "connecticut_avenue"]
purple = ["st.charles_place", "states_avenue", "virginia_avenue"]
orange = ["st.james_place", "tennessee_avenue", "new_york_avenue"]
red = ["kentucky_avenue", "indiana_avenue", "illinois_avenue"]
yellow = ["atlantic_avenue", "ventnor_avenue", "marvin_gardens"]
green = ["pacific_avenue", "north_carolina_avenue", "pennsylvania_avenue"]
darkblue = ["park_place", "boardwalk"]
railroad = ["reading", "pennsylvania", "b.&o.", "short"]
chance = ["chancebottom", "chancetop", "chanceright"]
community = ["communitybottom", "communityleft", "communityright"]
utilities = ["electric_company", "water_works"]
other = ["go", "income_tax", "jail", "free_parking", "go_to_jail", "luxury_tax"]
order = [other[0], brown[0], community[0], brown[1], other[1], railroad[0], lightblue[0], chance[0], lightblue[1],
         lightblue[2], other[2], purple[0], utilities[0], purple[1], purple[2], railroad[1], orange[0], community[1],
         orange[1], orange[2], other[3], red[0], chance[1], red[1], red[2], railroad[2], yellow[0], yellow[1],
         utilities[1], yellow[2], other[4], green[0], green[1], community[2], green[2], railroad[3], chance[2],
         darkblue[0], other[5], darkblue[1]]
mortprice = [None, 30, None, 30, None, 100, 50, None, 50, 50, None, 70, 75, 70, 80, 100, 90, None, 90, 100, None, 110,
             None, 110, 120, 100, 130, 130, 75, 140, None, 150, 150, None, 160, 100, None, 175, None, 200]
mortgaged = []
rentsingle = [None, 2, None, 4, None, None, 6, None, 6, 8, None, 10, None, 10, 12, None, 14, None, 14, 16, None, 18,
              None, 18, 20, None, 22, 22, None, 24, None, 26, 26, None, 28, None, None, 35, None, 50]
rentset = [None, 4, None, 8, None, None, 12, None, 12, 16, None, 20, None, 20, 24, None, 28, None, 28, 32, None, 36,
           None, 36, 40, None, 44, 44, None, 48, None, 52, 52, None, 56, None, None, 70, None, 100]
rent1 = [None, 10, None, 20, None, None, 30, None, 30, 40, None, 50, None, 50, 60, None, 70, None, 70, 80, None, 90,
         None, 90, 100, None, 110, 110, None, 120, None, 130, 130, None, 150, None, None, 175, None, 200]
rent2 = [None, 30, None, 60, None, None, 90, None, 90, 100, None, 150, None, 150, 180, None, 200, None, 200, 220, None,
         250, None, 250, 300, None, 330, 330, None, 360, None, 390, 390, None, 450, None, None, 500, None, 600]
rent3 = [None, 90, None, 180, None, None, 270, None, 270, 300, None, 450, None, 450, 500, None, 550, None, 550, 600,
         None, 700, None, 700, 750, None, 800, 800, None, 850, None, 900, 900, None, 1000, None, None, 1100, None, 1400]
rent4 = [None, 160, None, 320, None, None, 400, None, 400, 450, None, 625, None, 625, 700, None, 750, None, 750, 800,
         None, 875, None, 875, 925, None, 975, 975, None, 1025, None, 1100, 1100, None, 1200, None, None, 1300, None,
         1700]
rent5 = [None, 250, None, 450, None, None, 550, None, 550, 600, None, 750, None, 750, 900, None, 950, None, 950, 1000,
         None, 1050, None, 1050, 1100, None, 1150, 1150, None, 1200, None, 1275, 1275, None, 1400, None, None, 1500,
         None, 2000]
propertylevel = [None, "single", None, "single", None, None, "single", None, "single", "single", None, "single", None,
                 "single", "single", None, "single", None, "single", "single", None, "single", None, "single", "single",
                 None, "single", "single", None, "single", None, "single", "single", None, "single", None, None,
                 "single", None, "single"]

pygame.init()

dog_properties = []
thimble_properties = []
menu = None
black = (0, 0, 0)
white = (255, 255, 255)
bright_red = (255, 0, 0)
redcolour = (170, 0, 0)
bright_green = (0, 255, 0)
greencolour = (0, 170, 0)
bluecolour = (0, 0, 170)
bright_blue = (0, 0, 255)
purplecolour = (165, 0, 170)
bright_purple = (250, 0, 255)
xmid = 590
ymid = 462
doublemoney = False
freeparking = False
timelimit = False
double = False
jaildog = 0
jailthimble = 0
dice = None
rolled = False
landed = None
cost = 0
turn = None
rollcounter = 0
parkingmoney = 0
starttime = None
player = "dog"
dogtile = 0
thimbletile = 0
dogmoney = 0
thimblemoney = 0
dogx = 840
dogy = 900
thimblex = 880
thimbley = 890

bgImg = pygame.image.load("menu.png")
board = pygame.image.load("Board.png")
thimbleImg = pygame.image.load("thimble.png")
dogImg = pygame.image.load("dog.png")
icon = pygame.image.load("icon.png")

gameDisplay = pygame.display.set_mode((1180, 959))
gameDisplay.fill(bluecolour)
pygame.display.set_caption("Monopoly")
pygame.display.set_icon(icon)


# ----------------------------------------------------------------------------------------------#
def printlist():
    print(propertylevel)


def settings():
    global doublemoney, freeparking, timelimit
    setting = True
    while setting:
        gameDisplay.blit(bgImg, (0, 0))
        button(("Double Money = " + str(doublemoney)), xmid - 200, ymid - 200, 400, 100, bluecolour, bright_blue, 35,
               "doublemoney")
        button(("Free Parking = " + str(freeparking)), xmid - 200, ymid - 75, 400, 100, greencolour, bright_green, 35,
               "FreeParking")
        button(("Time Limit (60 Mins)= " + str(timelimit)), xmid - 200, ymid + 50, 400, 100, purplecolour,
               bright_purple, 28, "TimeLimit")
        button("2-Player", xmid - 200, ymid + 175, 400, 100, redcolour, bright_red, 35, "Start")
        pygame.display.update()
        pygame.event.wait()


# ----------------------------------------------------------------------------------------------#

def menu():
    global menu
    menu = True
    while menu:
        gameDisplay.blit(bgImg, (0, 0))
        button("2-Player", xmid - 125, ymid - 200, 250, 100, bluecolour, bright_blue, 35, "Start")
        button("Settings", xmid - 125, ymid - 75, 250, 100, greencolour, bright_green, 35, "settings")
        button("Quit", xmid - 125, ymid + 50, 250, 100, redcolour, bright_red, 35, "quit")

        pygame.display.update()
        pygame.event.wait()


# ----------------------------------------------------------------------------------------------#

def button(msg, x1, y1, w, h, ic, ac, size, button):
    global double, rolled
    smallText = pygame.font.Font("freesansbold.ttf", size)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x1 + w > mouse[0] > x1 and y1 + h > mouse[1] > y1:
        pygame.draw.rect(gameDisplay, ac, (x1, y1, w, h))
        if click[0] == 1:
            if button == "Start":
                play("load")
            elif button == "Dice":
                play("dice")
            elif button == "Trade":
                play("trade")
            elif button == "End":
                play("end_turn")
            elif button == "Mortgage":
                play("mortgage")
            elif button == "settings":
                settings()
            elif button == "quit":
                pygame.quit()
                quit()
            elif button == "purchase":
                play("purchase")
            elif button == "houses":
                play("houses")
            elif button == "jaildice":
                if not rolled:
                    rolled = True
                    dice1 = randint(1, 6)
                    dice2 = randint(1, 6)
                    if dice1 == dice2:

                        print("You have rolled a double, Roll again to leave jail")
                        double = True
                        rolled = False
                    elif dice1 != dice2:
                        print("You didnt roll a double, you remain in jail")
                elif rolled:
                    print("You have already rolled while in Jail")
                    print("-------------------------------------------")
            elif button == "print":
                print(dog_properties)
                print(thimble_properties)
                print(str(dogmoney) + "---" + str(thimblemoney))
                print("-------------------------------------------")
                printlist()
            elif button == "sets":
                play("sets")
            elif button == "doublemoney":
                global doublemoney
                if doublemoney:
                    doublemoney = False
                elif not doublemoney:
                    doublemoney = True
                pygame.event.wait()
            elif button == "FreeParking":
                global freeparking
                if freeparking:
                    freeparking = False
                elif not freeparking:
                    freeparking = True
                pygame.event.wait()
            elif button == "TimeLimit":
                global timelimit
                if timelimit:
                    timelimit = False
                elif not timelimit:
                    timelimit = True
                pygame.event.wait()
    else:
        pygame.draw.rect(gameDisplay, ic, (x1, y1, w, h))

    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x1 + (w / 2)), (y1 + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def play(option):
    def mortgage():
        global dogmoney, thimblemoney
        if player == "dog":
            mmoney = dogmoney
        elif player == "thimble":
            mmoney = thimblemoney
        while True:
            try:
                option = int(input("Select which properties you wish to mortgage: "))
                break
            except ValueError:
                print("Select which properties you wish to mortgage (Its the number of the board): ")
        if option in mortgaged:
            mortgaged.remove(int(option))
            mmoney = mmoney - mortprice[option]
        elif option not in mortgaged:
            mortgaged.append(int(option))
            mmoney = mmoney + mortprice[option]
        if player == "dog":
            dogmoney = mmoney
        elif player == "thimble":
            thimblemoney = mmoney

    def purchase():
        global landed, cost, dogmoney, thimblemoney
        if player == "dog":
            if landed in thimble_properties:
                print("You have landed on someone else's property. Pay Rent")
                paytile = dogtile
                if propertylevel[paytile] == "single":
                    payment = rentsingle[paytile]
                elif propertylevel[paytile] == "set":
                    payment = rentset[paytile]
                elif propertylevel[paytile] == "1":
                    payment = rent1[paytile]
                elif propertylevel[paytile] == "2":
                    payment = rent2[paytile]
                elif propertylevel[paytile] == "3":
                    payment = rent3[paytile]
                elif propertylevel[paytile] == "4":
                    payment = rent4[paytile]
                elif propertylevel[paytile] == "5":
                    payment = rent5[paytile]
                dogmoney = dogmoney - payment
                thimblemoney = thimblemoney + payment

            elif landed == "chancebottom" or landed == "chancetop" or landed == "chanceright" or landed == "communitybottom" or landed == "communityleft" or landed == "communityright" or landed == "go" or landed == "income_tax" or landed == "jail" or landed == "free_parking" or landed == "go_to_jail" or landed == "luxury_tax":
                print("This tile is not purchaseable")

            elif landed not in thimble_properties:
                if dogmoney >= cost and landed not in dog_properties:
                    print("You have bought: " + str(landed))
                    dogmoney = dogmoney - cost
                    dog_properties.append(landed)
                elif dogmoney < cost:
                    print("You cannot aford this property")
                elif landed in dog_properties:
                    print("You already own this property")

        elif player == "thimble":
            if landed in dog_properties:
                print("You have landed on someone else's property. Pay Rent")
                paytile = thimbletile
                if propertylevel[paytile] == "single":
                    payment = rentsingle[paytile]
                elif propertylevel[paytile] == "set":
                    payment = rentset[paytile]
                elif propertylevel[paytile] == "1":
                    payment = rent1[paytile]
                elif propertylevel[paytile] == "2":
                    payment = rent2[paytile]
                elif propertylevel[paytile] == "3":
                    payment = rent3[paytile]
                elif propertylevel[paytile] == "4":
                    payment = rent4[paytile]
                elif propertylevel[paytile] == "5":
                    payment = rent5[paytile]
                dogmoney = dogmoney + payment
                thimblemoney = thimblemoney - payment

            elif landed == "chancebottom" or landed == "chancetop" or landed == "chanceright" or landed == "communitybottom" or landed == "communityleft" or landed == "communityright" or landed == "go" or landed == "income_tax" or landed == "jail" or landed == "free_parking" or landed == "go_to_jail" or landed == "luxury_tax":
                print("This tile is not purchaseable")

            elif landed not in dog_properties:
                if thimblemoney >= cost and landed not in thimble_properties:
                    print("You have bought: " + str(landed))
                    thimblemoney = thimblemoney - cost
                    thimble_properties.append(landed)
                elif thimblemoney < cost:
                    print("You cannot aford this property")
                elif landed in thimble_properties:
                    print("You've already own this property")
        print("-------------------------------------------")

    def fixsets():
        if brown[0] and brown[1] in dog_properties:
            propertylevel[1] = "set"
            propertylevel[3] = "set"
        elif lightblue[0] and lightblue[1] and lightblue[2] in dog_properties:
            propertylevel[6] = "set"
            propertylevel[8] = "set"
            propertylevel[9] = "set"
        elif purple[0] and purple[1] and purple[2] in dog_properties:
            propertylevel[11] = "set"
            propertylevel[13] = "set"
            propertylevel[14] = "set"
        elif orange[0] and orange[1] and orange[2] in dog_properties:
            propertylevel[16] = "set"
            propertylevel[18] = "set"
            propertylevel[19] = "set"
        elif red[0] and red[1] and red[2] in dog_properties:
            propertylevel[21] = "set"
            propertylevel[23] = "set"
            propertylevel[24] = "set"
        elif yellow[0] and yellow[1] and yellow[2] in dog_properties:
            propertylevel[26] = "set"
            propertylevel[27] = "set"
            propertylevel[29] = "set"
        elif green[0] and green[1] and green[2] in dog_properties:
            propertylevel[31] = "set"
            propertylevel[32] = "set"
            propertylevel[34] = "set"
        elif darkblue[0] and darkblue[1] in dog_properties:
            propertylevel[37] = "set"
            propertylevel[39] = "set"
        elif brown[0] and brown[1] in thimble_properties:
            propertylevel[1] = "set"
            propertylevel[3] = "set"
        elif lightblue[0] and lightblue[1] and lightblue[2] in thimble_properties:
            propertylevel[6] = "set"
            propertylevel[8] = "set"
            propertylevel[9] = "set"
        elif purple[0] and purple[1] and purple[2] in thimble_properties:
            propertylevel[11] = "set"
            propertylevel[13] = "set"
            propertylevel[14] = "set"
        elif orange[0] and orange[1] and orange[2] in thimble_properties:
            propertylevel[16] = "set"
            propertylevel[18] = "set"
            propertylevel[19] = "set"
        elif red[0] and red[1] and red[2] in thimble_properties:
            propertylevel[21] = "set"
            propertylevel[23] = "set"
            propertylevel[24] = "set"
        elif yellow[0] and yellow[1] and yellow[2] in thimble_properties:
            propertylevel[26] = "set"
            propertylevel[27] = "set"
            propertylevel[29] = "set"
        elif green[0] and green[1] and green[2] in thimble_properties:
            propertylevel[31] = "set"
            propertylevel[32] = "set"
            propertylevel[34] = "set"
        elif darkblue[0] and darkblue[1] in thimble_properties:
            propertylevel[37] = "set"
            propertylevel[39] = "set"

    def houses():
        p = 0
        if player == "dog":
            for p in range(0, len(dog_properties)):
                print(str(p) + ": " + str(dog_properties[p]))
            while True:
                try:
                    option = int(input("Select which properties you want to add houses to? "))
                    break
                except ValueError:
                    print("Select which properties you want to add houses to? (Use the Number) : ")
        if player == "thimble":
            for p in range(0, len(thimble_properties)):
                print(str(p) + ": " + str(thimble_properties[p]))
            while True:
                try:
                    option = int(input("Select which properties you want to add houses to? "))
                    break
                except ValueError:
                    print("Select which properties you want to add houses to? (Use the Number) : ")
        if propertylevel[option] == "single":  # Current=Single
            print("You need a set first")
        elif propertylevel[option] == "set":  # Currnet=Set
            print("You will add one house to: " + str(order[option]))
            propertylevel[option] = "1"
        elif propertylevel[option] == "1":  # Current=1
            print("You will add one house to: " + str(order[option]))
            propertylevel[option] = "2"
        elif propertylevel[option] == "2":  # Current=2
            print("You will add one house to: " + str(order[option]))
            propertylevel[option] = "3"
        elif propertylevel[option] == "3":  # Current=3
            print("You will add one house to: " + str(order[option]))
            propertylevel[option] = "4"
        elif propertylevel[option] == "4":  # Current=4
            print("You will add one house to: " + str(order[option]))
            propertylevel[option] = "5"
        elif propertylevel[option] == "5":  # Current=5
            print("You cannot add any more houses")

    def trade():
        global dogmoney, thimblemoney
        choice = None
        dogtrade = []
        thimbletrade = []
        p = 0
        i = 0
        k = 0
        l = 0
        x = 0
        y = 0
        DTMoney = 0
        TTMoney = 0
        while choice != 0:
            print("Confirm (0)")
            print("Dog Money: " + str(dogmoney) + " (M)")
            if not dog_properties:
                print("Does not have any properties")
            else:
                for x in range(0, (len(dog_properties))):
                    print(str(x + 1) + ": " + str(dog_properties[x]))
            while True:
                try:
                    choice = str(input("Choose what you want to trade: "))
                    break
                except ValueError:
                    print("Choose what you want to trade: (Use Numbers) ")
            if choice == "M":
                while True:
                    try:
                        DTMoney = int(input("Enter how much you want to trade, you have " + str(dogmoney) + ": "))
                        break
                    except ValueError:
                        print("Enter how much you want to trade, you have " + str(dogmoney) + ": ")
                if DTMoney > dogmoney:
                    print("You do Not have that")
            elif choice == "0":
                choice = 0
            elif choice != "M" and choice != "0":
                choice = int(choice)
                dogtrade.append(dog_properties[choice - 1])
        print("You are trading: " + str(dogtrade) + " and " + str(DTMoney))
        choice = None
        while choice != 0:
            print("Confirm (0)")
            print("Thimble Money: " + str(thimblemoney) + " (M)")
            if not thimble_properties:
                print("Does not have any properties")
            else:
                for y in range(0, (len(thimble_properties))):
                    print(str(y + 1) + ": " + str(thimble_properties[y]))
            while True:
                try:
                    choice = str(input("Choose what you want to trade: "))
                    break
                except ValueError:
                    print("Choose what you want to trade: ")
            if choice == "M":
                while True:
                    try:
                        TTMoney = int(input("Enter how much you want to trade, you have " + str(thimblemoney) + ": "))
                        break
                    except ValueError:
                        print("Enter how much you want to trade, you have " + str(thimblemoney) + ": ")
                if TTMoney > thimblemoney:
                    print("You do Not have that")
            elif choice == "0":
                choice = 0
            elif choice != "M" and choice != "0":
                choice = int(choice)
                thimbletrade.append(thimble_properties[choice - 1])
        print("You are trading: " + str(thimbletrade) + " and " + str(TTMoney))
        while True:
            try:
                confirm = str(input("Do both players agreed to this trade (Y/N): "))
                break
            except ValueError:
                print("Do both players agreed to this trade (Y/N): ")
        if confirm == "Y":
            dogmoney = dogmoney - DTMoney
            thimblemoney = thimblemoney - TTMoney
            dogmoney = dogmoney + TTMoney
            thimblemoney = thimblemoney + DTMoney
            p = 0
            i = 0
            for p in range(0, len(dogtrade)):
                dog_properties.remove(dogtrade[p])
                thimble_properties.append(dogtrade[p])
            for i in range(0, len(thimbletrade)):
                thimble_properties.remove(thimbletrade[i])
                dog_properties.append(thimbletrade[p])
        DTMoney = 0
        TTMoney = 0
        dogtrade = []
        thimbletrade = []
        choice = None
        confirm = None
        x = 0
        y = 0
        return

    def load():
        global player, dogtile, starttime, thimbletile, dogx, dogy, thimblex, thimbley, dogmoney, thimblemoney, doublemoney
        dogtile = 0
        thimbletile = 0
        if doublemoney:
            dogmoney = 3000
            thimblemoney = 3000
        elif not doublemoney:
            dogmoney = 1500
            thimblemoney = 1500
        if timelimit:
            global starttime
            starttime = timer()
        turn()

    def turn():
        global player, jaildog, jailthimble, turn

        gameDisplay.blit(board, (0, 0))
        gameDisplay.blit(dogImg, (dogx, dogy))
        gameDisplay.blit(thimbleImg, (thimblex, thimbley))
        pygame.display.update()

        if player == "dog":
            if jaildog >= 1:
                jailalgorithm()
            elif jaildog == 0:
                turn = True

        elif player == "thimble":
            if jailthimble >= 1:
                jailalgorithm()
            elif jailthimble == 0:
                turn = True

        while turn:
            gameDisplay.blit(board, (0, 0))
            gameDisplay.blit(dogImg, (dogx, dogy))
            gameDisplay.blit(thimbleImg, (thimblex, thimbley))
            button("Roll Dice", 975, 42, 175, 70, bluecolour, bright_blue, 25, "Dice")
            button("Trade", 975, 196, 175, 70, greencolour, bright_green, 25, "Trade")
            button("End Turn", 975, 350, 175, 70, redcolour, bright_red, 25, "End")
            button("Mortgage", 975, 504, 175, 70, white, black, 25, "Mortgage")
            button("Buy Property", 975, 658, 175, 70, greencolour, bright_green, 25, "purchase")
            button("Buy Houses", 975, 812, 175, 70, greencolour, bright_green, 25, "houses")
            pygame.display.update()
            pygame.event.wait()

    def end_turn():
        global player, rolled, counter, cost, landed, dogmoney, thimblemoney
        if player == "dog":
            playermoney = dogmoney
        elif player == "thimble":
            playermoney = thimblemoney
        if playermoney < 0:
            additionalfunds()
            return
        if rolled:
            winalgorithm()
            fixsets()
            if player == "dog":
                print("Dog Money: " + str(dogmoney))
                print("Dog Properties: " + str(dog_properties))
                print("Thimble Money: " + str(thimblemoney))
                print("Thimble Properties: " + str(thimble_properties))
                player = "thimble"
            elif player == "thimble":
                print("Thimble Money: " + str(thimblemoney))
                print("Thimble Properties: " + str(thimble_properties))
                print("Dog Money: " + str(dogmoney))
                print("Dog Properties: " + str(dog_properties))
                player = "dog"
            rolled = False
            counter = 0
            landed = None
            cost = 0
            print("The current player is now: " + str(player))
            print("-------------------------------------------")
            turn()
        elif not rolled:
            print("You have not rolled yet")
            print("-------------------------------------------")
            return

    def dice():
        global rolled, double, dice, dogtile, thimbletile, player, rollcounter
        global dogx, dogy, thimblex, thimbley, dogmoney, thimblemoney
        if not rolled:

            rolled = True
            double = False
            dice1 = randint(1, 6)
            dice2 = randint(1, 6)
            dice = dice1 + dice2

            if dice1 == dice2:
                double = True
                rollcounter = rollcounter + 1
                rolled = False
                if rollcounter == 3:
                    jailalgorithm()
            print("You rolled a " + str(dice))
            if double:
                print("You rolled a double")
            if player == "dog":
                dogtile = dogtile + dice
                if dogtile >= 40:
                    dogtile = dogtile - 40
                    dogmoney = dogmoney + 200
                print("You have: " + str(dogmoney))
                print("-------------------------------------------")
                move("dog", dogtile, dogImg, dogx, dogy, thimblex, thimbley, thimbleImg, dogmoney)
            elif player == "thimble":
                thimbletile = thimbletile + dice
                if thimbletile >= 40:
                    thimbletile = thimbletile - 40
                    thimblemoney = thimblemoney + 200
                print("You have: " + str(thimblemoney))
                print("-------------------------------------------")
                move("thimble", thimbletile, thimbleImg, thimblex, thimbley, dogx, dogy, dogImg, thimblemoney)

        elif rolled:
            print("You've already rolled")

    if option == "end_turn":
        end_turn()
    elif option == "turn":
        turn()
    elif option == "dice":
        dice()
    elif option == "load":
        load()
    elif option == "trade":
        trade()
    elif option == "purchase":
        purchase()
    elif option == "houses":
        houses()
    elif option == "mortgage":
        mortgage()


# ----------------------------------------------------------------------------------------------#

def jailalgorithm():
    global jaildog, jailthimble, dogmoney, thimblemoney
    turn = True
    if player == "dog":
        if jaildog == 0:
            jaildog = 1
        elif jaildog == 1:
            jaildog = 2
        elif jaildog == 2:
            jaildog = 3
        elif jaildog == 3:
            dogmoney = dogmoney - 50
            jaildog = 0
            turn = False
            play("turn")

    elif player == "thimble":
        if jailthimble == 0:
            jailthimble = 1
        elif jailthimble == 1:
            jailthimble = 2
        elif jailthimble == 2:
            jailthimble = 3
        elif jailthimble == 3:
            thimblemoney = thimblemoney - 50
            jailthimble = 0
            turn = False
            play("turn")

    while turn:
        gameDisplay.blit(board, (0, 0))
        gameDisplay.blit(dogImg, (dogx, dogy))
        gameDisplay.blit(thimbleImg, (thimblex, thimbley))
        button("Jail Throw", 975, 42, 175, 70, bluecolour, bright_blue, 25, "jaildice")
        button("Trade", 975, 196, 175, 70, greencolour, bright_green, 25, "Trade")
        button("End Turn", 975, 350, 175, 70, redcolour, bright_red, 25, "End")
        button("Mortgage", 975, 504, 175, 70, white, black, 25, "Mortgage")
        button("Print List", 975, 658, 175, 70, greencolour, bright_green, 25, "print")
        button("Buy Houses", 975, 812, 175, 70, greencolour, bright_green, 25, "houses")
        pygame.display.update()
        pygame.event.wait()


# ----------------------------------------------------------------------------------------------#

def chancecard():
    global parkingmoney, freeparking, dogmoney, thimblemoney
    randomchance = randint(0, 15)
    print(chancecards[randomchance])
    if player == "dog":
        money = dogmoney
        othermoney = thimblemoney
    elif player == "thimble":
        money = thimblemoney
        othermoney = dogmoney
    # -------------------------------#
    if randomchance == 0:  # Advance to Go
        print("Advance to Go()")
    elif randomchance == 1:  # Illiois Ave
        print("IllinoisAve()")
    elif randomchance == 2:  # St.Charles Place
        print("ST.CharlesPlace()")
    elif randomchance == 3:  # Nearest Utility
        print("NearestUtility()")
    elif randomchance == 4:  # Nearst Railroad
        print("NearestRailRoad()")
    elif randomchance == 5:  # Recieve 50
        money = money + 50
    elif randomchance == 6:  # Get out of Jail Free
        print("GetOutOfJailFree()")
    elif randomchance == 7:  # Back 3 spaces
        print("Back3Space()")
    elif randomchance == 8:  # Go TO Jail
        print("GotoJail()")
    elif randomchance == 9:  # House Repairs 25/100
        print("Houserepairs()")
    elif randomchance == 10:  # pay 15
        if freeparking:
            parkingmoney = parkingmoney + 15
        money = money - 15
    elif randomchance == 11:  # reading railroad
        print("ReadingRailroad()")
    elif randomchance == 12:  # boardwalk
        print("Boardwalk()")
    elif randomchance == 13:  # pay other player 50
        money = money - 50
        othermoney = othermoney + 50
    elif randomchance == 14:  # recieve 150
        money = money + 150
    elif randomchance == 15:  # collect 100
        money = money + 100
    print("-------------------------------------------")
    # -------------------------------#
    if player == "dog":
        dogmoney = money
        thimblemoney = othermoney
    elif player == "thimble":
        thimblemoney = money
        dogmoney = othermoney


# ----------------------------------------------------------------------------------------------#

def communitycard():
    global dogmoney, thimblemoney, player, freeparking, parkingmoney, dogtile, thimbletile
    randomchest = randint(0, 16)
    print(communitycards[randomchest])
    if player == "dog":
        money = dogmoney
        othermoney = thimblemoney
    elif player == "thimble":
        money = thimblemoney
        othermoney = dogmoney
    # -------------------------------#
    if randomchest == 0:  # Advance to Go
        print("Advance to go ()")
        if player == "dog":
            dogtile = 0
            move("dog", dogtile, dogImg, 840, 900, thimblex, thimbley, thimbleImg, dogmoney)
            pygame.display.update()
        elif player == "thimble":
            thimbletile = 0
            move("thimble", thimbletile, thimbleImg, 840, 900, dogx, dogy, dogImg, thimblemoney)

    elif randomchest == 1:  # Collect 200
        money = money + 200
    elif randomchest == 2:  # Pay 50
        if freeparking:
            parkingmoney = parkingmoney + 50
        money = money - 50
    elif randomchest == 3:  # Get out of Jail Free
        print("Get out of jail free()")
    elif randomchest == 4:  # Go to Jail
        print("Go to Jail()")
    elif randomchest == 5:  # Collect 50 from other player
        money = money + 50
        othermoney = othermoney - 50
    elif randomchest == 6 or randomchest == 9 or randomchest == 15:  # Recieve 100
        money = money + 100
    elif randomchest == 7:  # Collect 20
        money = money + 20
    elif randomchest == 8:  # collect 10 from other player
        money = money + 10
        othermoney = othermoney - 10
    elif randomchest == 10 or randomchest == 11:  # pay 50
        if freeparking:
            parkingmoney = parkingmoney + 50
        money = money - 50
    elif randomchest == 12:  # recieve 25
        money = money + 25
    elif randomchest == 13:  # House Repairs 40/115
        print("House repairs()")
    elif randomchest == 14:  # Collect 10
        money = money + 10
    elif randomchest == 16:  # Get 50
        money = money + 50
    print("-------------------------------------------")
    # -------------------------------#
    if player == "dog":
        dogmoney = money
        thimblemoney = othermoney
    elif player == "thimble":
        thimblemoney = money
        dogmoney = othermoney


# ----------------------------------------------------------------------------------------------#

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# ----------------------------------------------------------------------------------------------#

def winalgorithm():
    global starttime, turn, timelimit, dogmoney, thimblemoney
    if timelimit:
        endtime = timer()
        time = endtime - starttime
        if time >= 3600:
            print("The Game is over, It has been an hour")
            turn = False
            print("Player 1 Worth")
            print("Player 2 Worth")

    elif not timelimit:
        if dogmoney < 0:
            print("doglost")
            print("fix problem of no money condition")
        elif thimblemoney < 0:
            print("thimblelost")
            print("fix problem of no money condition")


def additionalfunds():
    if player == "dog":
        money = dogmoney
    elif player == "thimble":
        money = thimblemoney
    print("You have no money, if you end the turn you will loose. You have: " + str(money))


def othertile(tile, playermoney):
    global parkingmoney, freeparking
    if tile == "luxury":
        if freeparking:
            playermoney = playermoney - 100
            parkingmoney = parkingmoney + 100
        elif not freeparking:
            return
    elif tile == "parking":
        if freeparking:
            playermoney = playermoney + parkingmoney
            parkingmoney = 0
        elif not freeparking:
            return
    elif tile == "jail":
        jailalgorithm()
        print("-------------------------------------------")


def move(player, playerposition, image, playerx, playery, x2, y2, image2, playermoney):
    global dice, thimbley, thimblex, dogy, dogx, landed, cost, freeparking, dogmoney, thimblemoney
    align = 0
    if player == "dog":
        align = 0
    elif player == "thimble":
        align = 20

    if playerposition == 0:
        playerx, playery = 840 + align, 900
    elif playerposition == 1:
        playerx, playery = 760 + align, 900
        landed = brown[0]
        cost = 60
    elif playerposition == 2:
        playerx, playery = 680 + align, 900
        landed = community[0]
        communitycard()
    elif playerposition == 3:
        playerx, playery = 600 + align, 900
        landed = brown[1]
        cost = 60
    elif playerposition == 4:  # Income Tax
        playerx, playery = 520 + align, 900
        landed = other[1]
        if player == "dog":
            dogmoney = dogmoney - 200
        elif player == "thimble":
            thimblemoney = thimblemoney - 200
        if freeparking == True:
            parkingmoney += 200
    elif playerposition == 5:
        playerx, playery = 440 + align, 900
        landed = railroad[0]
        cost = 200
    elif playerposition == 6:
        playerx, playery = 360 + align, 900
        landed = lightblue[0]
        cost = 100
    elif playerposition == 7:
        playerx, playery = 280 + align, 900
        landed = chance[0]
        chancecard()
    elif playerposition == 8:
        playerx, playery = 200 + align, 900
        landed = lightblue[1]
        cost = 100
    elif playerposition == 9:
        playerx, playery = 120 + align, 900
        landed = lightblue[2]
        cost = 120
    elif playerposition == 10:
        playerx, playery = 15 + align, 900
        landed = other[2]
    elif playerposition == 11:
        playerx, playery = 15 + align, 790 - align
        landed = purple[0]
        cost = 140
    elif playerposition == 12:
        playerx, playery = 15 + align, 710 - align
        landed = utilities[0]  # Electric Company
        cost = 150
    elif playerposition == 13:
        playerx, playery = 15 + align, 630 - align
        landed = purple[1]
        cost = 140
    elif playerposition == 14:
        playerx, playery = 15 + align, 550 - align
        landed = purple[2]
        cost = 160
    elif playerposition == 15:
        playerx, playery = 15 + align, 470 - align
        landed = railroad[1]
        cost = 200
    elif playerposition == 16:
        playerx, playery = 15 + align, 390 - align
        landed = orange[0]
        cost = 180
    elif playerposition == 17:
        playerx, playery = 15 + align, 310 - align
        landed = community[1]
        communitycard()
    elif playerposition == 18:
        playerx, playery = 15 + align, 230 - align
        landed = orange[1]
        cost = 180
    elif playerposition == 19:
        playerx, playery = 15 + align, 150 - align
        landed = orange[2]
        cost = 200
    elif playerposition == 20:
        playerx, playery = 15 + align, 15
        landed = other[3]  # Free Parking
        othertile("parking", playermoney)
    elif playerposition == 21:
        playerx, playery = 150 - align, 15
        landed = red[0]
        cost = 220
    elif playerposition == 22:
        playerx, playery = 230 - align, 15
        landed = chance[1]
        chancecard()
    elif playerposition == 23:
        playerx, playery = 310 - align, 15
        landed = red[1]
        cost = 220
    elif playerposition == 24:
        playerx, playery = 390 - align, 15
        landed = red[2]
        cost = 240
    elif playerposition == 25:
        playerx, playery = 470 - align, 15
        landed = railroad[2]
        cost = 200
    elif playerposition == 26:
        playerx, playery = 550 - align, 15
        landed = yellow[0]
        cost = 260
    elif playerposition == 27:
        playerx, playery = 630 - align, 15
        landed = yellow[1]
        cost = 260
    elif playerposition == 28:
        playerx, playery = 710 - align, 15
        landed = utilities[1]  # Water Works
        cost = 150
    elif playerposition == 29:
        playerx, playery = 790 - align, 15
        landed = yellow[2]
        cost = 280
    elif playerposition == 30:
        playerx, playery = 900 - align, 15
        landed = other[4]
    elif playerposition == 31:
        playerx, playery = 900, 150 - align
        landed = green[0]
        cost = 300
    elif playerposition == 32:
        playerx, playery = 900, 230 - align
        landed = green[1]
        cost = 300
    elif playerposition == 33:
        playerx, playery = 900, 310 - align
        landed = community[2]
        communitycard()
    elif playerposition == 34:
        playerx, playery = 900, 390 - align
        landed = green[2]
        cost = 320
    elif playerposition == 35:
        playerx, playery = 900, 470 - align
        landed = railroad[3]
        cost = 200
    elif playerposition == 36:
        playerx, playery = 900, 550 - align
        landed = chance[2]
        chancecard()
    elif playerposition == 37:
        playerx, playery = 900, 630 - align
        landed = darkblue[0]
        cost = 350
    elif playerposition == 38:
        playerx, playery = 900, 710 - align
        landed = other[5]  # Luxury Tax
        othertile("luxury", playermoney)
    elif playerposition == 39:
        playerx, playery = 900, 790 - align
        landed = darkblue[1]
        cost = 400

    if player == "dog":
        dogx = playerx
        dogy = playery
    elif player == "thimble":
        thimblex = playerx
        thimbley = playery

    return dogx, dogy, thimblex, thimbley


# ----------------------------------------------------------------------------------------------#

menu()
