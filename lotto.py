from sys import exit
import random

running = True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
           16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
           29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
           42, 43, 44, 45, 46, 47, 48, 49]

def lotto_gen_7():
    pick = random.sample(numbers, 7)
    pick.sort()
    print(pick)

def lotto_gen_6():
    pick = random.sample(numbers, 6)
    pick.sort()
    print(pick)


while running:
    x = input('Press "1" for 7 numbers. Press "2" for 6 numbers. Any other key to quit \n')
    if x == "1":
        lotto_gen_7()
    elif x == "2":
        lotto_gen_6()
    else:
        running == False
        exit()
        