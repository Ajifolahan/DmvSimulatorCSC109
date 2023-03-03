from random import randint
from time import sleep

def main():
    print("Welcome to the DMV")
    random = randint(1,200)
    print("Your DMV number is" , random, ". Please wait till your number is called")
    print("Please listen to your numbers everyone")

    for i in range(random + 1, 201 + random):
        sleep(0.5)
        if(i > 200):
            print("Number", i - 200)
        else :
            print("Number", i)
    
    random2 = randint(1,100)
    if random2 == 1: 
        print("Goodjob, You have all the required paperwork")
    else :
        print("You do not have the required paperwork, should've thought to check that before you came here, stupid")

if __name__ == '__main__':
    main()