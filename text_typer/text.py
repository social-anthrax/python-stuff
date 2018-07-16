#!/usr/bin/env python3
import subprocess
import time
import sys
# open the textfile

try:
    text = open(sys.argv[2]).read().strip()
except:
    text = open("text.txt").read().strip()

PID = []

try:
    print("getting id")
    process_id = subprocess.check_output(["xdotool", "search", "--name", sys.argv[3]])
    PID = process_id.splitlines()

    print("window found. Name:%s PID= %s" % (sys.argv[3:], PID[len(PID)-1]))
    subprocess.call(["xdotool", "windowactivate", PID[len(PID)-1]])
except:
    print("Window not found/no parameters entered. Procceding with text dump.")

i = 0
for i in range(0, int(sys.argv[1])):
    for ch in text:
        # type out the text
        subprocess.call(["xdotool", "type", ch])
        # increase or decrease the time below to type slower or faster
        time.sleep(0.1)

    subprocess.call(["xdotool", "key", "KP_Enter"])
