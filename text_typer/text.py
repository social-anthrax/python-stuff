#!/usr/bin/env python3
import subprocess
import time
import sys
# open the textfile

try:
    #tries to open the file which is given to it as argument 2. PS arrays dont start at 1 ik but 1st arg is the name of the program ok?
    text = open(sys.argv[2]).read().strip()
except: #if this fails it opens text.txt which should be in the same dirctory
    text = open("text.txt").read().strip()



try:
    print("getting id")
    process_id = subprocess.check_output(["xdotool", "search", "--name", sys.argv[3]]) #attempts to fetch the PID of the given program
    PID = process_id.splitlines() #splits the multiple PID's it recieves

    print("window found. Name:%s PID= %s" % (sys.argv[3:], PID[len(PID)-1])) #the last PID seems to be the window so thats what this switchs to.
    subprocess.call(["xdotool", "windowactivate", PID[len(PID)-1]])
except:
    print("Window not found/no parameters entered. Procceding with text dump.")

i = 0
for i in range(0, int(sys.argv[1])):
    for ch in text:
        # type out the text
        subprocess.call(["xdotool", "type", ch])
        # increase or decrease the time below to type slower or faster
        time.sleep(0.01)

    subprocess.call(["xdotool", "key", "KP_Enter"])
