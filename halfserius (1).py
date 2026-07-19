purple = 0
green = 0
yellow = 0
hunger = 0
health = 100
day = 1
# purple is enasni, green is lamron, yellow is bmud 
def day4():
    global purple
    global green
    global yellow
    global hunger
    global health
    global day
    print("It's day 4. You woke up back at your house. You probably sleepwalked.")
    if purple < 6:
        print("The monsters are upset with you.")
        choice6 = input("{RUN}\t{STAY}\t{COME AT THEM}\n")
        if choice6 == "RUN":
            print("The doors and windows are stuck. The chimney too. Except you don't have a chimney. All of it's covered in something black.")
            if yellow > 3:
                print("It seems sticky. Touch it?")
                touch1 = input("{yes}\t{no}\n")
                if touch1 == "yes":
                    print("You got stuck in it. You managed to get out, but it took the whole day.")
                    yellow += 2
                    day += 1
                elif touch1 == "no":
                    print("Probably a good idea...")
                    green += 3
    elif purple > 6:
        print("The monsters greeted you happily. Your house feels... different, though. You try to open the door, but it's blocked by the monsters' ooze.\nThe monsters come up to you and say you're too fun to let out.")
        mtu1 = input("{PANIC}\t{society is worse}\n")
        if mtu1 == "PANIC":
            print("Party pooper. The monsters felt decieved and used you as a prop in their escape room. So tragic, you can't warn anyone anymore...\nENDING: PROPPED")
            exit()
        elif mtu1 == "society is worse":
            print("You decided being here with the monsters is better than living like a normal person.\nDays pass and you fall deeper into insanity. The monsters start getting concerned and let you out to seek help.")
            
    else:
        print("How the hell did you get here... The monsters are neutral with you. They let you go or stay.")

def day3():
    global purple
    global green
    global yellow
    global hunger
    global health
    global day
    print("You had a dream today. You don't remember it though.\nYour room stinks of blood. You decide to check...")
    choice4 = input("{the wardrobe}\t{under the bed}\t{HELL NAH}\n")
    if choice4 == "the wardrobe":
        print("You opened the wardrobe and an anime girl knocked you out. You didn't wake up.")
        print("ENDING: WAIFU'D")
        exit()
    elif choice4 == "under the bed":
        print("Ah. You forgot to feed the monsters, and they took a snack themselves. You deducted the person is dead. You may be next.")
        print("Will you feed the monsters?")
        purple += 2
        feedmonsters1 = input("{yes}\t{no}\n")
        purple += 1
        if feedmonsters1 == "yes":
            print("With what?")
            feedingmon1 = input("{normal food}\t{a human}\n")
            if feedingmon1 == "normal food":
                print("The monsters didn't like it and they ate you.")
                print("ENDING: EATEN BY MONSTERS b")
                exit()
            elif feedingmon1 == "a human":
                print("You fed them someone and they're happy.")
                day += 1
                if purple > 4:
                    print("You ate a little of that person too. The aftertaste was interesting. You talked with the monsters for a while and then went to their party. It lasted the whole night.")
                else:
                    print("You hid under the blanket for a long time.")
        elif feedmonsters1 == "no":
            print("They ate you.")
            print("ENDING: MONSTER EATEN a")
            exit()
    elif choice4 == "HELL NAH":
        print("You ran away from home. You went...")
        green += 2
        runaway1 = input("{to the police station}\t{to a friend's house}\t{to grandma}\t{screw it.}\n")
        if runaway1 == "to grandma":
            print("Grandma welcomed you with opened arms to stay the night. She fed you too many cookies though.")
            hunger -= 20
            health -= 15
            day += 1
        elif runaway1 == "to the police station":
            print("You told the cops you smelled blood in your room. They reluctantly went to check it and they found nothing.\nThe monsters will probably be upset...")
            day += 1
            green += 4
        elif runaway1 == "to a friend's house":
            print("Very funny. Maybe the imaginary one. You lay on the street.")
            day += 1
            hunger += 10
            if yellow > 2:
                print("You could always sleep in a store like in those cool videos...")
                choice5 = input("{yes}\t{no}\n")
                if choice5 == "yes":
                    print("You managed to hide in an IKEA. The employees saw you but decided your life is sad enough.")
                elif choice5 == "no":
                    print("You sleep on the street. For 2 minutes. You go there anyway.")
                    print("You managed to hide in an IKEA. The employees saw you but decided your life is sad enough.")

        elif runaway1 == "screw it.":
            print("You become homeless but your begging is very ineffective. You starve.")
            print("ENDING: HOMELESS                                                                                                                                                                                                                                                                                                                                                                                ")
            exit()
        

def day2():
    global purple
    global green
    global yellow
    global hunger
    global health
    global day
    print("The first day passes.\nYou wake up to the familiar feeling of being broke.\nYou have to go shopping today.\n")
    choice2 = input("{go shopping}\t{starve}\t{steal food}\n")
    if choice2 == "go shopping":
        print("You went shopping. You bought some normal things for the money you had.")
        green += 1
        print("You bought 2 apples, some ramen and a bun.")
        day += 1
        if hunger > 10:
            print("You need to eat something. What will you eat?")
            choice3 = input("{the apples}\t{ramen}\t{the bun}\n")
            if choice3 == "the apples":
                hunger -= 4
                print("It was good, but you're still a little hungry.")
            elif choice3 == "ramen":
                hunger -= 8
                print("That hit the spot.")
            elif choice3 == "the bun":
                hunger -= 5
                print("Tasted decent.")
    elif choice2 == "starve":
        print("You are starving.\n")
        starving1 = input("{eat}\t{don't eat}\n")
        if starving1 == "eat":
            print("You ate something. You spent the whole day lying in your bed, exhausted.")
            day += 1
            purple += 1
        elif starving1 == "don't eat":
            print("You starved.")
            print("ENDING: STARVED")
            hunger += 100
            exit()
        else:
            print("stop trolling/being a dumbass")
            exit()
    elif choice2 == "steal food":
        print("From where?")
        yellow += 1
        stealing1 = input("{neighbour}\t{grandma}\t{cat}\n")
        if stealing1 == "cat":
            print("You stole a cat's food bowl. It striked you with lightning. Never mess with cats.")
            print("ENDING: CAT STRIKED")
            exit()
        elif stealing1 == "neighbour":
            print("The neighbour caught you. You went to prison.")
            print("ENDING: PRISON a")
            exit()
        elif stealing1 == "grandma":
            print("You are evil. Grandma fed you anyway and insisted you stay for tea.")
            day += 1
            hunger -= 2
        else:
            print("pfft. you shouldve stolen")
            exit()
    else:
        print("no cheating today")
        exit()

def start():
    global purple
    global green
    global yellow
    global hunger
    global health
    global day
    print("You wake up to the smell of the trash next to your bed. You didn't clean your room since 1885.")
    print("As per usual, you ignore this to go downstairs and check your fridge for food.")
    print("Inside, you find a note from your mom that's been sitting there for 2 years. It's a block of ice.")
    print("The only other thing you have there is ice cream that was freezed and unfreezed 14 times already.")
    print("You decide to eat...")
    choice = input("{the ice cream}\t{the note}\t{none}\n")
    if choice == "the ice cream":
        print("You ate the ice cream.")
        print("You got diarrhoea. The first day flies by on the toilet.")
        yellow += 1
        day += 1
        hunger -= 3
    elif choice == "the note":
        print("You ate the note")
        print("It tasted like a freezer. The paper was ok though.\nYou spent the whole day trying to eat it.")
        purple += 1
        hunger -= 1
        day += 1
    elif choice == "none":
        print("You decide it's best if you don't eat.")
        print("You're hungry.")
        green += 1
        hunger += 10
        greenhunger1 = input("{eat something from the fridge}\t{wait until tomorrow}\n")
        if greenhunger1 == "eat something from the fridge":
            print("The day passed normally.")
            day += 1
            hunger -= 2
        elif greenhunger1 == "wait until tomorrow":
            print("You didn't eat anything and decided to buy food tomorrow. You lie on the couch the whole day.")
            day += 1
            hunger += 5
        else:
            print("no")
            exit()
    elif choice == "chair":
        print("yum. It took a long time to eat though.")
        day += 1
        purple += 4
        hunger -= 1
    else:
        print("either youre trolling or stupid")
        exit()

start()
while True:
    if day == 2:
        day2()
        break
while True:
    if day == 3:
        day3()
        break
while True:
    if day == 4:
        day4()
        break
#
