from pyfiglet import figlet_format
from termcolor import colored
from random import choice

def printfig(output):
    color = choice(["red", "green", "blue", "yellow"])
    figtext = figlet_format(output)
    print(colored(figtext, color=color))

if __name__ == "__main__":
    while True:
        text = input("Enter a word > ")
        if text == "stop":
            break
        else:
            printfig(text)