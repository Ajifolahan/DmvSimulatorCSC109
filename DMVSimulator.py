if __name__ == '__main__':

    import random
    print("Welcome to the DMV")
    random = random.randint(1,100)

    for i in range(random, 101 + random):
        if(i > 100):
            print(i - 100)
        else :
            print(i)