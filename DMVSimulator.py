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
    
    print("You do not have the required paperwork")

if __name__ == '__main__':
    main()