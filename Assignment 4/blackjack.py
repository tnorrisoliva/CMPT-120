#if you don't know how to play blackjack, tbh not super important but look it up anyway LOL
#this script is going to require some googling: I want you to practice using your resources with this one. But of course if you get stuck, reach out :)
'''instructions: randomly generate three values between 1 and 11. in the function bust: add these three numbers together. if they add up to or less than 21, return the sum. If it's over 21, return 0. If it's over 21 BUT there's an 11 as one of the values, return the sum - 10. '''
import random

num1 = random.randrange(1,11)
num2 = random.randrange(1,11)
num3 = random.randrange(1,11)

score=num1+num2+num3
def bust():
    if score <=21 :
        print(score)
    elif score >21 and num1 or num2 or num3 == 11:
        print(10)
    else:
        print(0)
    
def main():
    bust()

main()
