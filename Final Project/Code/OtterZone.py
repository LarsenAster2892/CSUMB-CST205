import random
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
#       Final Project
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++
# Declare globals to be used
playerName = ""
lastCommand = ""
currCommand = ""
currentLocation = "Quad"
previousLocation = ""
lastLocation = ""
gameSnds = []
gamePics = {}
gameMap = {}
compassDirecs = ["north", "east", "south", "west"]
listOfValidDirections = ""
#
#-------------------------------------------------------------
#  loadSnd
#  inputs:  (none)
#  output:  sndReturn - Sound file loaded from disk
#-------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --load sound for game 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def loadSnd(sndList):
  FileChooser.setMediaPath("C:/Users/LN/Documents/7. Education/Classess/Current/CST205/Project - Final/Code/Sounds")
  sndList.append( makeSound(getMediaPath("\Otters\otter1.wav")))
  sndList.append( makeSound(getMediaPath("\Otters\otter2.wav")))
  sndList.append( makeSound(getMediaPath("\Otters\otter3.wav")))  
#
#-------------------------------------------------------------
#  loadPic
#  inputs:  (none)
#  output:  sndReturn - Sound file loaded from disk
#-------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --load Picutres for game 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def loadPic(picList):
  FileChooser.setMediaPath("C:/Users/LN/Documents/7. Education/Classess/Current/CST205/Project - Final/Code/Pictures")
  tmpSnd = (makePicture(getMediaPath("quad.jpg"))) 
  picList["Quad"] = tmpSnd
  tmpSnd = (makePicture(getMediaPath("mediaCenter.jpg"))) 
  picList["Multi-Media Center"] = tmpSnd
  tmpSnd = (makePicture(getMediaPath("tortugaHall.jpg"))) 
  picList["Tortuga Hall"] = tmpSnd
  tmpSnd = (makePicture(getMediaPath("admin.jpg")))
  picList["Admin Building"] = tmpSnd
  tmpSnd = (makePicture(getMediaPath("dinnigCommons.jpg")))
  picList["Dinning Commons"] = tmpSnd
  tmpSnd = (makePicture(getMediaPath("otterExpress.jpg")))
  picList["Otter Express"] = tmpSnd
  tmpSnd = (makePicture(getMediaPath("mediaCenter.jpg")))
  picList["Student Activity Building"] = tmpSnd
  tmpSnd = (makePicture(getMediaPath("library.jpg")))
  picList["CSUMB Library"] = tmpSnd



#
#-------------------------------------------------------------------------------
#
#  Load Game Map 
#    
#------------------------------------------------------------------------------ 
def loadMap(theMap):
  theMap["Quad"] = ["Multi-Media Center", "CSUMB Library", "Admin Building","Tortuga Hall" ]
  theMap["Multi-Media Center"] = ["NA", "Dinning Commons", "Quad", "Tortuga Hall"]
  theMap["Tortuga Hall"] = ["Multi-Media Center", "Quad", "Admin Building","NA" ]
  theMap["Admin Building"] = ["Quad", "CSUMB Library", "NA", "Tortuga Hall"]
  theMap["Dinning Commons"] = ["NA", "Otter Express", "NA", "Multi-Media Center"]
  theMap["Otter Express"] = ["NA", "Student Activity Building", "NA","Dinning Commons" ]
  theMap["Student Activity Building"] = ["NA", "NA", "CSUMB Library", "Otter Express"]
  theMap["CSUMB Library"] = ["Student Activity Building", "NA", "Admin Building", "Quad"]

#
#
#-------------------------------------------------------------------------------
#
#  Get the name of the player
#    
#------------------------------------------------------------------------------
def getPlayerName():
#
#  -- make new sound that range of start to end
#
   playerName = requestString("What is your name?")
   showInformation("Hello " + playerName)
#
#-------------------------------------------------------------------------------
#
#  print the Instructions 
#    
#------------------------------------------------------------------------------
def printInstructions(): 
  instrucText = "Welcome to the OtterZone! "
  instrucText += "\nIn each location, you will be told which directions you can go."
  instrucText += "\n"
  instrucText += "\nYou can move north, south, east, or west by typing that direction."
  instrucText += "\n"
  instrucText += "\nType help to redisplay these introduction."
  instrucText += "\n"
  instrucText += "\nType quit or exit to end the program."
  showInformation(instrucText) 
#
#-------------------------------------------------------------------------------
#
#  get directions for the current locations
#    
#------------------------------------------------------------------------------
#
def getLocDirections(locDirecs):
  currFacing = 0
  listStr = ""
  newLine = ""
  listOfValidDirections = ""
  for currDirec in locDirecs:
    if currDirec != "NA":
      listStr += newLine + "To the " + compassDirecs[currFacing] + " is the " + currDirec
      listOfValidDirections += compassDirecs[currFacing]
    currFacing += 1
    newLine = "\n" 
  return listStr
#
#-------------------------------------------------------------------------------
#
#  show information about current location
#    
#------------------------------------------------------------------------------
#
def showLocation(location):
  locInfo = "=== You are in the " + location + "====\n\n"
#  showInformation(locInfo)
  locDirecs = gameMap[location]
  listOfDirec = getLocDirections(locDirecs)
  locInfo += listOfDirec
  showInformation(locInfo)
  return listOfDirec
#
#-------------------------------------------------------------------------------
#
#  check for valid command
#    
#------------------------------------------------------------------------------
#
def isValidCmd(currCmd):
  isValid = false
#
  if (currCmd == "exit"):
     isValid = true
  elif (currCmd == "quit"):
     isValid = true
     currCmd = "exit"
  elif (currCmd == "help"):
     isValid = true
  elif (currCmd == "look"):
     isValid = true
  elif (currCmd in compassDirecs):
     isValid = true
  else:
     isValid = false
  return isValid
#
#-------------------------------------------------------------------------------
#
#  check for valid directions
#    
#------------------------------------------------------------------------------
  
def isValidDir(currCmd, inDirecs):
  isValid = false
#
#  printNow(inDirecs)
#  printNow(currCmd)
  if inDirecs.find(currCmd)== -1:
     isValid = false
  else:
     isValid = true
  return isValid
#
#-------------------------------------------------------------------------------
#
#  play sound when entering locations (random)
#    
#------------------------------------------------------------------------------
#
def playSounds():
  sndIndex =  random.randrange(0,4)
  if (sndIndex < 3):
    snd = gameSnds[sndIndex]
    snd.play()
  
#
#-------------------------------------------------------------------------------
#
#  play the Game
#    
#------------------------------------------------------------------------------
#
def otterZone():
#
# Declare Globals
  global currCommand
  global playerName
  global lastCommand
  global currCommand
  global currentLocation
  global previousLocation
  global lastLocation
  global gameSnds
  global gamePics
  global gameMap
  global compassDirecs
  global listOfValidDirections
#
#
# Initialize the game
#
  currentLocation = "Quad"
  loadSnd(gameSnds)
  loadPic(gamePics)
  loadMap(gameMap)
#
#  Get Player Information
#
  getPlayerName()
#
#  print instructions
#
  currCommand = ""
  printInstructions()
  while not (currCommand == "exit") :
    directionsList = showLocation(currentLocation)
#
    userCmd = requestString("Enter a direction or a command:")
    currCommand = userCmd.lower()
#
    if not(isValidCmd(currCommand)):
       showInformation("Invalid Command!, please try again!")     
    elif (currCommand == "exit"):
       showInformation("Thank you for playing " + playerName)
    elif (currCommand == "help"):
       printInstructions()
    elif (currCommand == "look"):
       directionsList = showLocation(currentLocation)
    else:
      if not(isValidDir(currCommand, directionsList)):
        showInformation("Invalid direction, please try again!")
      else:
        previousLocation = currentLocation
#       showInformation(previousLocation)
#       showInformation(currentLocation)
        currLocDirecs = gameMap[currentLocation]
#       printNow(currLocDirecs)
        direcIndex = compassDirecs.index(currCommand)
#       showInformation(str(direcIndex))
        playSounds()
        currentLocation = currLocDirecs[direcIndex]
        locPic = gamePics[currentLocation]
        locPic.show()
