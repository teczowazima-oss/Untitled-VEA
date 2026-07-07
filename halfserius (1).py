purple = 0
green = 0
yellow = 0
hunger = 0
health = 100
day = 1
# purple is insane, green is normal, yellow is dumb
def day3():
    print("Placeholder")

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
            exit()
        elif stealing1 == "neighbour":
            print("The neighbour caught you. You went to prison.")
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
        purple += 2
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