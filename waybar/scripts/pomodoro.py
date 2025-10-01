#!/usr/bin/env python3

import os
import time
import json
import subprocess


def notify(title, message):
    subprocess.run(["notify-send", title, message])

def header():
    print("Pomodoro Timer".center(os.get_terminal_size().columns, "-"))

def footer():
    size = os.get_terminal_size()
    height = size.lines
    
    print("\n" * (height - 10), end="")
    print ("-" * os.get_terminal_size().columns)


def workCountdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print("\033[F\033[K\033[F\033[K\033[F\033[K", end="")
        print("Pomodoro Timer".center(os.get_terminal_size().columns, "-"))
        print("")
        print(timer.center(os.get_terminal_size().columns))
        time.sleep(1)
        seconds -= 1
        if seconds % 5 == 0:
            os.system("cls" if os.name == "nt" else "clear")
    print("\033[F\033[K\033[F\033[K\033[F\033[K", end="")
    print("Pomodoro Timer".center(os.get_terminal_size().columns, "-"))
    print("00:00".center(os.get_terminal_size().columns))
    print("Work's up!")
    notify(" Pomodoro Timer", "Work session finished!")
    input("Press a key to start break..." \
    "")


def breakCountdown(seconds, workMinutes, breakMinutes):
    workMinutes
    breakMinutes
    os.system("cls" if os.name == "nt" else "clear")
    header()
    print ("Work Minutes:  "+str(workMinutes))
    print ("Break Minutes: "+str(breakMinutes))

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print("\033[F\033[K\033[F\033[K\033[F\033[K", end="")
        print("Pomodoro Timer".center(os.get_terminal_size().columns, "-"))
        print ("")
        print(timer.center(os.get_terminal_size().columns))
        time.sleep(1)
        seconds -= 1
        if seconds % 5 == 0:
            os.system("cls" if os.name == "nt" else "clear")
    print("\033[F\033[K\033[F\033[K\033[F\033[K", end="")
    print("Pomodoro Timer".center(os.get_terminal_size().columns, "-"))
    print("00:00".center(os.get_terminal_size().columns))
    print("Break's up!")
    notify(" Pomodoro Timer", "Break session finished!")
    input("Press a key to return" \
    "")


def main():
    header()
    workMinutes = int(input("Work Minutes:  "))
    breakMinutes = int(input("Break Minutes: "))

    os.system("cls" if os.name == "nt" else "clear")

    workCountdown(workMinutes * 60)
    breakCountdown(breakMinutes * 60, workMinutes, breakMinutes)
    footer()



running = True
while running:
    os.system("cls" if os.name == "nt" else "clear")
    main()
