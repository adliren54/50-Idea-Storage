import os, time, random

def add():
  os.system("clear")
  idea = input("Idea > ")
  f = open("my.ideas", "a+")
  f.write(f"{idea}\n")
  f.close()
  time.sleep(2)
  os.system("clear")

def show():
  os.system("clear")
  f = open("my.ideas", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  idea = random.choice(ideas)
  print(idea)
  time.sleep(3)
  os.system("clear")

while True:
  menu = input("1. Add idea\n2. Show a random idea\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    show()
  else:
    print("That is not a valid input. Try again...")
    os.system("clear")
    continue