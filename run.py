import os
os.system("cls")
print("welcome to the terminal tests project select menu")
print("please select the project you want to run")
print("")
print("systest: when run if the system works it will print hello world")
print("")
user = input(">")

if user == "systest":
    os.system("python systest/main.py")

