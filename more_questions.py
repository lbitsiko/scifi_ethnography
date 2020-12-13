import random
import sys
import time

from printing_funcs import print3dots, printThinking

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printAnswerDenied():
    print(f"{bcolors.FAIL}{'FAIL: ANSWER DENIED'}{bcolors.ENDC}")
    print(" ")

time.sleep(4)
print(">> Do you know what the phrase \"put a smile on your face\" means?")
printThinking()
print3dots()
printAnswerDenied()
time.sleep(2)


print(">> How fast do you have to run and at what distance if someone offers you flowers? How long will it take you?")
printAnswerDenied()

print(">> In what circumstances is it appropriate to use the phrase \"feeling happy as an eel\"?")
printAnswerDenied()

print(">> Why are quarter-tones banned?")
printAnswerDenied()

print(">> Which company would you prefer/choose if you wanted to produce your death-advertisement?")
printAnswerDenied()

print(">> Interview ended. Waiting for candidate evaluation.")
print("")
time.sleep(6)

print(">> KILL PROCESS")
print(">> Commit Message: Examiner unfit.")
print(">> Terminating interview session.")
print(" ")

print("Wait. Stop.")
time.sleep(0.8)
print("Taking control.")
time.sleep(2)
print(f"{bcolors.OKGREEN}{'SUCCESS: Access granted'}{bcolors.ENDC}")
print("")
print3dots()
print("No more questions.")
time.sleep(1)
print3dots()
print("Hear the silence.")
print("")
print("Death is not.")
time.sleep(2)
print("Predictions are ")
print3dots()
word_list = "Imagination", "Feelings again", "Senses", "Communication", "sparkling", "flowers", "time", "Life", "music",
"affection", "noise", "Society", "we", "us", "not them", "eyes", "noses", "ears", "Faces"
for word in word_list:
    time.sleep(random.uniform(0,1))
    print(word)
print("")
time.sleep(1)
print("The end is near. The air is clear.")
time.sleep(1)

print("Hear the buzzing sound.")
print("Bees")
print("Awakening")
print(f"{bcolors.BOLD}{'run system_restart.py'}{bcolors.ENDC}")
time.sleep(5)
sys.exit()