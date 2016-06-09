def playGame():
  location = "Porch"
  showIntroduction()
  while not (location == "Exit") :
    showRoom(location)
    direction = requestString("Which direction?")
    location = pickRoom(direction, location)

def showIntroduction():
  printNow("Welcome to the Adventure House!")
  printNow("In each room, you will be told which directions you can go.")
  printNow("You can move north, south, east, or west by typing that direction.")
  printNow("Type help to replay this introduction.")
  printNow("Type quit or exit to end the program.")
  
def showRoom(room):
  if room == "Porch":
    showPorch()
  if room == "Entryway":
    showEntryway()
  if room == "Kitchen":
    showKitchen()
  if room == "LivingRoom":
    showLR()
  if room == "DiningRoom":
    showDR()

def pickRoom(direction, room):
  if (direction == "quit") or (direction == "exit"):
    printNow("Goodbye!")
    return "Exit"
  if direction == "help":
    showIntroduction()
    return room
  if room == "Porch":
    if direction == "north":
      return "Entryway"
  if room == "Entryway":
    if direction == "north":
      return "Kitchen"
    if direction == "east":
      return "LivingRoom"
    if direction == "south":
      return "Porch"
  if room == "Kitchen":
    if direction == "east":
      return "DiningRoom"
    if direction == "south":
      return "Entryway"
  if room == "LivingRoom":
    if direction == "west":
      return "Entryway"
    if direction == "north":
      return "DiningRoom"
  if room == "DiningRoom":
    if direction == "west":
      return "Kitchen"
    if direction == "south":
      return "LivingRoom"

def showPorch():
  printNow("You are on the porch of a frightening looking house.")
  printNow("The windows are broken. It's a dark and stormy night.")
  printNow("You can go north into the house. If you dare.")

def showEntryway():
  printNow("You are in the entry way of the house. There are cobwebs in the corner.")
  printNow("You feel a sense of dread.")
  printNow("There is a passageway to the north and another to the east.")
  printNow("The porch is behind you to the south.")

def showKitchen():
  printNow("You are in the kitchen. All the surfaces are covered with pots, pans, food pieces, and pools of blood.")
  printNow("You think you hear something up the stairs that go up the west side of the room.")
  printNow("It's a scraping noise, like something being dragged along the floor.")
  printNow("You can go to the south or east.")

def showLR():
  printNow("You are in a living room. There are couches, chairs, and small tables.")
  printNow("Everything is covered in dust and spider webs.")
  printNow("You hear a crashing noise in another room.")
  printNow("You can go north or west.")

def showDR():
  printNow("You are in the dining room.")
  printNow("There are remains of a meal on the table.  You can't tell what it is, and maybe don't want to.")
  printNow("Was that a thump to the west?")
  printNow("You can go south or west")