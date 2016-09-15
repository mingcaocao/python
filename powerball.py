import random

def pull_powerballs():
    print "Winning numbers are"
    for ball in range(0, 5):
        print random.randint(1,69)
    print "Powerball:" + str(random.randint(1,26))

pull_powerballs()
