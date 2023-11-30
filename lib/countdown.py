# your code goes here!
import time

def countdown(num):
    while num >= 0:
        if num == 0:
            print("HAPPY NEW YEAR!")
        else:    
            print(f'{num} SECOND(S)!')
        num-=1


def countdown_with_sleep(num):
    while num >= 0:
        if num == 0:
            print("HAPPY NEW YEAR!")
        else:    
            print(f'{num} SECOND(S)!')
        num-=1
        time.sleep(1)