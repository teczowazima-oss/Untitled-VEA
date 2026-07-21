purple = 0
green = 0
yellow = 0
hunger = 0
health = 100
day = 1
monstercare = 0
# purple is enasni, green is lamron, yellow is bmud
def day5():
    global purple
    global green
    global yellow
    global hunger
    global health
    global day
    global monstercare
    print("Day 5... Congrats on getting through yesterday. I'm guessing it's not your first attempt. It got pretty dark, didn't it? Well. Since no one wanted more days, I'll make them.")
    # This one will make you feel weird because it will be super goofy! So you will feel like something bad's gonna come!")
    print("You are at your house. Or something similiar to it. Anyway, you're in a place very similiar to your house.")
    if monstercare == 1:
        print("The monsters are neutral. They will let you choose whether you go or stay.")
    elif monstercare == 0:
        print("The monsters want you gone or dead.")
    elif monstercare == 2:
        print("The monsters want you here forever. You're too important to let out! You are funny, cool, and their bestie! The outside is too dangerous.")
    elif monstercare == 3 or (green > 3 and purple < 7):
        print("'You should go... We want you to feel good.' The monsters look genuinely concerned. It's the first time they spoke like a human. I think they're trying to be as human as they can for you.")
    elif monstercare == 4 or purple > 7:
        print("Your friends care. They will let you go, but won't force you to do anything. You're one of them.")
def day4():
    global purple
    global green
    global yellow
    global hunger
    global health
    global day
    global monstercare
    print("It's day 4. You woke up back at your house. You probably sleepwalked.")
    if purple < 5:
        print("The monsters are upset with you.")
        choice6 = input("{RUN}\t{STAY}\t{COME AT THEM}\n")
        if choice6 == "RUN":
            green += 2
            print("The doors and windows are stuck. The chimney too. Except you don't have a chimney. All of it's covered in something black.")
            if yellow > 3:
                print("It seems sticky. Touch it?")
                touch1 = input("{yes}\t{no}\n")
                if touch1 == "yes":
                    print("You got stuck in it. You managed to get out, but it took the whole day.")
                    yellow += 2
                    day += 1
                    monstercare = 0
                elif touch1 == "no":
                    print("Probably a good idea... You sit there. Just... sit. You dont get food and eventually dont wanna do anything. You become the next meal.\nENDING: EATEN c")
                    exit()
            else:
                print("You realise it's not your house. It's really weird. It looks like it's trying to mimic it.\nDid the monsters... Kidnap you? They explain it's a parallel universe they made for you. You realise you can't run away. Do you befriend the monsters or deny them?\n")
                denyfriend1 = input("{Befriend}\t{Deny}\n")
                if denyfriend1 == "Befriend":
                    print("The monsters tell you to cut this crap. When they kidnapped you you're suddenly a friend, huh? Not believable. You become their toy.\nENDING: TOYED")
                    exit()
                elif denyfriend1 == "Deny":
                    print("The monsters thought about this, but still were a little surprised. You showed you stand your ground and don't change just to save yourself. They say they will let you go tomorrow.")
                    day += 1
        elif choice6 == "STAY":
            print("The monsters... did not expect this. They don't accept you. You hear whispers everywhere.\nYou find a small opening in the black thing.")
            runstay1 = input("{Run}\t{Stay}\n")
            if runstay1 == "Run":
                print("You try to. You get stuck. You get closed in a cocoon.\nENDING: HYBERNATING a")
                exit()
            elif runstay1 == "Stay":
                print("You fall asleep. You don't wake up, consumed by the black ooze.\nENDING: HYBERNATING b")
        elif choice6 == "COME AT THEM":
            yellow += 2
            print("You do a wimpy slap. The monsters look shocked and laugh. They decide you're funny.\nThey like you. So they won't let you leave...")
            day += 1
            monstercare = 2

    elif purple >= 8:
        print("The monsters greeted you happily. Your house feels... different, though. You try to open the door, but it's blocked by the monsters' ooze.\nThe monsters come up to you and say you're too fun to let out.")
        mtu1 = input("{PANIC}\t{society is worse}\n")
        if mtu1 == "PANIC":
            print("Party pooper. The monsters felt decieved and used you as a prop in their escape room. So tragic, you can't warn anyone anymore...\nENDING: PROPPED")
            exit()
        elif mtu1 == "society is worse":
            print("You decided being here with the monsters is better than living like a normal person.\nDays pass and you fall deeper into insanity. The monsters start getting concerned and let you out to seek help.\nThere you are again, on the street, because your besties kicked you out. How could they?! You did EVERYTHING to be friends, you were cool, you were fun, you killed too... AND NOW THEY KICK YOU OUT?!\n")
            choice8 = input("{Be upset}\t{Understand}\n")
            if choice8 == "Be upset":
                purple += 10
                print("YES! HOW CAN THEY?! YOU FED THEM FOR MONTHS, YOU CARED! AND THEY?! YOU DECIDE THIS DEMANDS BLOOD. THEY LEFT YOU. YOU WILL GET REVENGE. YOU GATHER WEAPONS, KILL TO GET THEM, AND FINALLY GET TO YOUR HOUSE. YOU SHOOT THE GUNS. YOU BREAK EVERYTHING.\nBut... they caught you. They push you to the ground and take your hard earned toys. They tell you to calm down.\nYOU DON'T. YOU CAN'T. YOU STRUGGLE AGAINST THEIR GRIP. FINALLY, THE POLICE COME. YOU SCREAM YOUR HEART OUT. THE POLICE INVESTIGATE YOU AND TAKE YOU AWAY. EVERYTHING AFTER THAT IS LIKE... a fever dream. You don't know whats right or wrong, who cares?\nYou take evry opportunity to go crazy. They close you in an asylum.")
                print("One day, you start spiraling. What did you do... You broke everything, no wonder they hate you. ENDING: very dark turn that i need to mark in the trigger warnings")
                exit()
            elif choice8 == "Understand":
                print("No... They care. You're the bad one here. You would go get help, but it's too expensive... You try to think more... normally. And calling them monsters seems bad now. They're friends, but you're not one of them. You are a human that should take killing and cannibalism as a bad thing. But... Does that make your friends bad? They cared about you. But humanity sees them as bad.\nWho should you believe...\n")
                choice9 = input("{humans?}\t{friends?}\n")
                if choice9 == "humans?":
                    print("You're human. You should believe humans. You go to the police station to explain the situation. Turns out there is free help. One day, after going to therapy for a long time, you see one of your friends carrying groceries. The not human friends. You got your life together, they said.\n")
                    #Should i end here, future me?
                    print("\nENDING: THERAPY IS WORTH IT!")
                    exit()
                elif choice9 == "friends?":
                    print("They are the ones that helped you. You go over to your house, and say what you feel. They show you something. They started eating apples! That's partly the reason your groceries went missing a lot, but they were working to become more human. You realise how ironic this is - You became a monster, they became a human. You decide to meet halfway.")
                    monstercare = 4
                    #Idunno howto continue
                    print("They encourage you to go to a human therapist. But... You don't want to yet.")
    else:
        print("How the hell did you get here... The monsters are neutral with you. They let you go or stay.")
        staygo1 = input("{Stay}\t{Go}\n")
        if staygo1 == "Stay":
            print("You decided staying with the monsters is cool. You live like them, with them, and slowly start feeling as one of them.\n")
            if green > 4 and yellow < 6:
                print("You feel weird about it. You fall into anxiety, jumping at every whisper. You don't feel good about this.")
                print("You tell that to the monster therapist and they say you can go away if you feel so bad. They won't chase you.")
                print("They treat you as their equal. That means you deserve freedom.")
                staygo2 = input ("{Stay}\t{Go}\n")
                if staygo2 == "Stay":
                    print("Your anxiety gets bigger and bigger, followed by an existential crisis. Are you human? Monster? Dead? Fake?\nHard to tell. They start noticing. They are worried.")
                    day += 1
                    monstercare = 3
            else:
                print("You like living like this. You feel at home. You slowly see your body becoming like the monsters'. It's good. After months, you are officialy one of them! You realise your family isn't as bad as humanity says.\nThey don't kill to kill. That's their way to eat. Being scary, psychotic... That's a habit around humans. Humans are actually worse than them. Not from your perspective.\nYour family isn't toxic. They tolerate every gender, every hobby, don't have the internet.\nENDING: ONE OF THEM (sane)")
                exit()

def day3():
    global purple
    global green
    global yellow
    global hunger
    global health
    global day
    global monstercare
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
            yellow += 2
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
    global monstercare
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
while True:
    if day == 5:
        day5()
        break
#
