
import colorama
import time
import random
import os


col = list(vars(colorama.Fore).values())



def pr214():
    print('11111111111111         111111111111111111           11111111111111111111      1111111      11111111                  ')
    print('1111111111111111       11111111111111111111         11111111111111111111      1111111      11111111                  ')
    print('11111111111111111      111111111111111111111        11111111111111111111      1111111      11111111                  ')
    print('111111     111111      111111          11111                      111111      1111111      11111111                  ')
    print('111111     111111      111111          11111                      111111      1111111      11111111                  ')
    print('111111     111111      111111          11111                      111111      1111111      11111111         111111   ')
    print('1111111111111111       11111111111111111111         11111111111111111111      1111111      11111111         111111   ')
    print('111111111111111        1111111111111111111          11111111111111111111      1111111      11111111111111111111111   ')
    print('1111111111111          11111111111111111            11111111111111111111      1111111      11111111111111111111111   ')
    print('111111                 111111   1111111             111111                    1111111      11111111111111111111111   ')
    print('111111                 111111     111111            111111                    1111111                      1111111   ')
    print('111111                 111111       111111          111111                    1111111                      1111111   ')
    print('111111                 111111         111111        11111111111111111111      1111111                      1111111   ')
    print('111111                 111111           111111      11111111111111111111      1111111                      1111111   ')




def affichage():
    for i in range(300):   
        time.sleep(0.001)
        print(random.choice(col),"11"*65)
    time.sleep(3)    
    os.system('cls')

    for i in range(20):
        print(random.choice(col),pr214())   
        time.sleep(0.1)
        os.system('cls')

affichage()