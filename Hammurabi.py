import random
#Introduction
def print_intro():
    print('''
Congrats, you are the newest ruler of ancient Samaria, elected for a ten year term
of office. Your duties are to distribute food, direct farming, and buy and sell land
as needed to support your people. Watch out for rat infestations and the resultant
plague! Grain is the general currency, measured in bushels. The following will help
you in your decisions:

(a) Each person needs at least 20 bushels of grain per year to survive.
(b) Each person can farm at most 10 acres of land.
(c) It takes 2 bushels of grain to farm an acre of land.
(d) The market price for land fluctuates yearly.

Rule wisely and you will be showered with appreciation at the end of your term. Rule
poorly and you will be kicked out of office!

          ''')

#ask players how much land they want to buy
def ask_to_buy_land(bushels_in_storage, cost_per_acre):
    acres = input("How many acres will you buy?\n")
    while acres * cost_per_acre > bushels_in_storage:
        print "Oh great Hammurabi, we have but ", bushels_in_storage, " bushels of grain!"
        acres = input("How many acres will you buy?\n")
    return acres

#ask players how much land they want to sell if they didn't want to buy land
def ask_to_sell_land(acres_owned,):
    acres = input("How many acres will you sell?\n")
    while acres > acres_owned:
        print "Oh great Hammurabi, we have but ", acres_owned, "acres!"
        acres = input("How many acres will you sell?\n")
    return acres

#ask players how much bushels they want to feed the people
def ask_to_feed(bushels_in_storage):
    bushels = input("How many bushels will you use to feed your people?\n")
    while bushels > bushels_in_storage:
        print "Oh great Hammurabi, we have but ", bushels_in_storage, " bushels of grain!"
        bushels = input("How many bushels will you use to feed your people?\n")
    return bushels

#ask player how much land they want to plant seed in
def ask_to_cultivate(acres_owned, population, bushels_in_storage):
    land = input("How many acres of land will you plant seed in?\n")
    while land > acres_owned:
        print "Oh great Hammurabi, we have but ", acres_owned, "acres!"
        land = input("How many acres of land will you plant seed in?\n")
    while land > 10 * population:
        print "Oh great Hammurabi, we have but ", population, "people!"
        land = input("How many acres of land will you plant seed in?\n")
    while land > 2 * bushels_in_storage:
        print "Oh great Hammurabi, we have but ", bushels_in_storage, " bushels of grain!"
        land = input("How many acres of land will you plant seed in?\n")
    return land

#decide whether plague happens or not
def is_plague(population):
    plague = random.randint(1,101)
    if plague in range(1,16):
        plague_deaths = population / 2
    else:
        plague_deaths = 0
    return plague_deaths

#decide the number of starved according to players' decision
def num_starving(population, bushels):
    if bushels >= 20 * population:
        starved = 0
    else:
        starved = (20 * population - bushels) / 20
    return starved

#calculate the number of immigrants if nobody starved
def num_immigrants(acre_owned, bushels_in_storage, population, starved):
    if starved > 0:
        immigrants = 0
    else:
        immigrants = (20 * acre_owned + bushels_in_storage) / (100 * population + 1)
    return immigrants

#decide how many bushels each acre of land produces
def get_harvest():
    bushels_per_acre = random.randint(1,9)
    return bushels_per_acre

#decide whether rats infest happens or not this year
def do_rats_infest():
    rats = random.randint(1,101)
    if rats in range(1,41):
        infest = True
    else:
        infest = False
    return infest

#decide the percent of bushels destroied
def percent_destroyed():
    percent = 0.01 * random.randint(10,31)
    return percent

#decide the price of land for next year
def price_of_land():
    price = random.randint(16,23)
    return price


#the main part of program which integrates all other functions
def Hammurabi():
    #set initial valuables
    starved = 0
    immigrants = 5
    population = 100
    harvest = 3000          # total bushels harvested
    bushels_per_acre = 3    # amount harvested for each acre planted
    rats_ate = 200          # bushels destroyed by rats
    bushels_in_storage = 2800
    acres_owned = 1000
    cost_per_acre = 19      # each acre costs this many bushels
    plague_deaths = 0
    starved_sum = 0

    #call print_intro function
    print_intro()

    #go from the first year to the 10th year, ends at
    #the 11th year if not break before
    for year in range(1,11):
        #show players the information of what's happend this year
        print('You are in year ' + str(year) + ' of your ten year rule.')
        print('In the previous year ' + str(starved) + ' people starved to death.')
        print('In the previous year ' + str(immigrants) + ' people entered the kingdom.')
        print('The population is now ' + str(population) + ' .')
        print('We harvested ' + str(harvest) + ' bushels at '
              + str(bushels_per_acre) + ' bushels per acre.')
        print('Rats destroyed ' + str(rats_ate) + 'bushels, leaving '
              + str(bushels_in_storage) + ' bushels in storage.')
        print('The city owns ' + str(acres_owned) + ' acres of land.')
        print('Land is currenty worth ' + str(cost_per_acre) + ' bushels per acre.')
        print('There were ' + str(plague_deaths) + ' deaths from the plague.\n')

        #call ask_to_buy_land function and calculate
        #the change in owned acres and bushels in storage
        acres = ask_to_buy_land(bushels_in_storage, cost_per_acre)
        if acres == 0:
            acres = -ask_to_sell_land(acres_owned)
        acres_owned = acres_owned + acres
        bushels_in_storage = bushels_in_storage - acres * cost_per_acre

        #call ask_to_feed function and calculate the change in bushels in storage
        bushels = ask_to_feed(bushels_in_storage)
        bushels_in_storage = bushels_in_storage - bushels

        #call ask_to_cultivate function and calculate
        #the change in bushels in storage
        land = ask_to_cultivate(acres_owned, population, bushels_in_storage)
        bushels_in_storage = bushels_in_storage - land * 2

        #call is_plague function and calculate the change in population
        plague_deaths = is_plague(population)
        population = population - plague_deaths

        #call num_starving function and and sum up the total
        #starved number for final report
        starved = num_starving(population, bushels)
        starved_sum += starved

        #decide whether the game continues or not
        #according to the starved number
        if starved >= 0.45 * population:
            print "You are thrown out of the office!"
            break

        #calculate the change in population
        population = population - starved

        #call the num_immigrants function and
        #calculate the change in population
        immigrants = num_immigrants(acres_owned, bushels_in_storage,
                                    population, starved)
        population = population + immigrants

        #call the get_harvest function and calculate the harvest bushels and
        #change in bushels in storage
        bushels_per_acre = get_harvest()
        harvest = bushels_per_acre * land
        bushels_in_storage += harvest

        #call the do_rats_infest function and  calculate
        #the change in bushels in storage
        rats_infest = do_rats_infest()
        if rats_infest:
            rats_ate = bushels_in_storage * percent_destroyed()
            bushels_in_storage -= rats_ate

        #call the price_of_land function
        cost_per_acre = price_of_land()

    #when loop ends or breaks, show ending information
    #according to what kind of ending happens
    if year == 11:      #for players who complete the 10-year-term office
        print
        '''
        Congratulation! You have finished your 10-year-term safely
        without being assassinated by starved people! Well done!
        '''
        print("Total number of starved people is " + str(starved_sum) +
              ". The land city owned now is "
              + str(acres_owned) + ". Good job:)")
    else:               #for players who don't complete the 10-year term
        print("So many people want to assasinate you." +
              "It's luck for you to be still alive:( Better luck next time!")

#call the Hammurabi function so the game will start once running the program
#which is very important for players who
#have no idea how to start game by themselves!
def main():
    Hammurabi()

if __name__ == "__main__":
    main()
 
