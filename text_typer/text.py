#!/usr/bin/env python3
import subprocess
import time
import sys

try:
    #tries to open the file which is given to it as argument 2. PS arrays dont start at 1 ik but 1st arg is the name of the program ok?
    text = open(sys.argv[2]).read()
except: #if this fails it opens text.txt which should be in the same dirctory
    text = open("text.txt").read()


try:
    print("getting id")
    process_id = subprocess.check_output(["xdotool", "search", "--name", sys.argv[3]]) #attempts to fetch the PID of the given program by reading what would be printed to terminal
    PID = process_id.splitlines() #splits the multiple PID's it recieves
    print("window found. Name:%s PID= %s" % (sys.argv[3:], PID[len(PID)-1])) #the last PID seems to be the window so thats what this switchs to.
    subprocess.call(["xdotool", "windowactivate", PID[len(PID)-1]]) #activates the window with the last PID recieved
except:
    print("Window not found/no parameters entered. Procceding with text dump.")


arrWord = [] #initialises array


for index in range(0, int(sys.argv[1])): #Itterates for the number exemplified in the arguments passed to the program.
    for lines in text.splitlines():
        lines = lines+" [enter]"
        print(lines)
        i = 0
        for word in lines.split(" "): #splits the text into words

            if word.lower() == "[enter]": #if the word is [enter] then it presses the enter key
                subprocess.call(["xdotool", "key", "KP_Enter"]) #here
            else: #otherwise
                word = word + " "
                for ch in word:#for every lettger in a word.
                    #type out the text
                    subprocess.call(["xdotool", "type", ch])
                    # increase or decrease the time elow to type slower or faster
                    time.sleep(0.01)
        i = i+1
