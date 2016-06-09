#===================================================
# CST205 Multimedia Design & Programming, Fall 2014 
# Professor Allie Xiong
# Team 5: <Otter Design>
# Members: 
#          Clarence Mitchell
#          Gracie Alderete-Fisher
#====================================================
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#       Lab 11
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#-------------------------------------------------------------------------------
#
#  print the Instructions 
#    
#------------------------------------------------------------------------------
def printInstructions(): 
  printNow("Welcome to the Team Otter Adventure House! ")
  printNow("\nIn each room you will be told which directions you can go")
  printNow("\n")
  printNow("\nYou can move north, south, east, or west by typing that direction.")
  printNow("\n")
  printNow("\nType help to redisplay these instructions.")
  printNow("\n")
  printNow("\nType Exit to end the program.")


#
#-------------------------------------------------------------------------------
#
#  Print information for current room!!!
#    
#------------------------------------------------------------------------------- 
#
def showRoomInfo(currentRoom, gotKnife):
  printNow("\n===========")
  if currentRoom == "Porch":
    printNow("You are on the porch oof a haunted house.")
    printNow("It is a dark and stormy night")
    printNow("You can go north into the house. If you dare.")
#  
  elif currentRoom == "Foyer":
    printNow("You are in the foyer of the house. Discarded computer parts are everywhere")
    printNow("You feel a sense of dread.")
    printNow("There is a passageway to the north and another to the east.")
    printNow("The porch is behind you to the south.")
#  
  elif currentRoom == "Kitchen":
    printNow("You are in the kitchen. There is a big bloody mess here.")
    if (gotKnife):
      printNow("Looks like there used to be bloody knife in the counter")
    else:
      printNow("A bloody knife is stuck in the counter")
    printNow("You can go to the south or east.")
#
  elif currentRoom == "LivingRoom":
    printNow("You are in a living room. It is dimmly lite here.")
    printNow("There is sofa and chair that are dusty.")
    printNow("You can go north or west.")
#
  elif currentRoom == "DiningRoom":
    printNow("You are in the dining room.")
    printNow("No one is here but there is food on the table.")
    printNow("You can go south or west")
#
#  Should never be at lines below
  else:
    printNow("You are lost somewhere")
    printNow("please exit the game.")
#
#-------------------------------------------------------------------------------
#
#  Checks if direction is valid and moves player to new (if valid)
#    
#------------------------------------------------------------------------------- 
#
    
def checkAndGetDirection(checkDirection, currentRoom, gotKnife):
  nextRoom = ""
  if (currentRoom == "Porch") and (checkDirection == "north"):
      nextRoom = "Foyer"
#
  elif currentRoom == "Foyer":
    if checkDirection == "north":
      nextRoom = "Kitchen"
    elif checkDirection == "east":
      nextRoom = "LivingRoom"
    elif checkDirection == "south":
      nextRoom = "Porch"
    else:
      nextRoom = currentRoom
#
  elif currentRoom == "Kitchen":
    if checkDirection == "east":
      nextRoom = "DiningRoom"
    elif checkDirection == "south":
      nextRoom = "Foyer"
    else:
      nextRoom = currentRoom
#
  elif currentRoom == "LivingRoom":
    if checkDirection == "west":
      nextRoom = "Foyer"
    elif checkDirection == "north":
      nextRoom = "DiningRoom"
    else:
      nextRoom = currentRoom
#
  elif currentRoom == "DiningRoom":
    if checkDirection == "west":
      nextRoom = "Kitchen"
    if checkDirection == "south":
      nextRoom = "LivingRoom"
    else:
      nextRoom = currentRoom
#      
  else: 
    nextRoom = currentRoom
    printNow("You can't (or don't want to) go in that direction.")
    
  return nextRoom

def adventureGame():
  location = "Porch"
  printInstructions()
  userDirection = ""
  holdingKnife = false
  
  while not ((userDirection == "Exit") or (userDirection == "exit")) :
    showRoomInfo(location, holdingKnife)
    userDirection = requestString("What direction do you want to go?")
    printNow("You typed: " + userDirection)
#    
    if (userDirection == "Exit") or (userDirection == "exit"):
        printNow("Thanks for playing...Goodbye!")
#    
    elif userDirection  == "help":
        printInstructions()
#  
    elif userDirection == "get knife":
      if (holdingKnife):
        printNow("You already have the knife...")
      else:
        printNow("You are now holding a possible murder weapon...")
        holdingKnife = true

    else:
        location = checkAndGetDirection(userDirection, location, holdingKnife)
        printNow( holdingKnife)
