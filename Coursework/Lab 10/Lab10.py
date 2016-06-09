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
#       LAB 10
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#-------------------------------------------------------------
#  loadSnd
#  inputs:  (none)
#  output:  sndReturn - Sound file loaded from disk
#-------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --load pics for other routines 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def loadSnd():
  filename = pickAFile()
  print filename
  sndReturn = makeSound(filename)
  print sndReturn
  return sndReturn

#-------------------------------------------------------------
#  saveSound()
#    saves an sound from JES memory to disk location
#  inputs:   source     - Input sound 
#  output:              - Sound file written to disk
#-------------------------------------------------------------
def saveSound(source):
  writeSoundTo(source, pickAFile())
  print "Your file was successfully saved!"
#
#
#-------------------------------------------------------------------------------
#  warmUpPartA - 
#    
#------------------------------------------------------------------------------
def warmUpPartA():
#
#  -- make new sound that range of start to end
#
   name = requestString("What is your name?")
   showInformation("Hello " + name)
#
#
#-------------------------------------------------------------------------------
#  warmUpPartB - 
#    
#------------------------------------------------------------------------------
#
def warmUpPartB():
  userWord = ""
  while (userWord != "stop"):
    userWord = requestString("Looking for a word...Give me one?")


def getWord():
   listOfWords = ("hangman", "chairs", "backpack", "bodywash", "clothing", "computer", "python", "program", "glasses", "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives", "ninjas", "shampoo")
   rtnWord =  listOfWords[1]
   return rtnWord
   
def findAndReplace(searchLetter, searchWord, outputWord):
  numberReplaced = 0
  startingPos = 0
  letterPos = searchWord.find(searchLetter)
  while letterPos != -1:
    outputWord[letterPos] = searchLetter
    startingPos = letterPos + 1
    letterPos = searchWord.find(searchLetter, startingPos)
    numberReplaced += 1
  return numberReplaced
    
   
#
#-------------------------------------------------------------------------------
# hangman - 
#------------------------------------------------------------------------------
#
def hangman():
#
  guessWord = getWord()
  numGuessess = 6
  guessWordLen = len(guessWord)
  available_letters = "abcdefghijklmnopqrstuvwxyz"
  outputWord = ["_"] * guessWordLen
  lettersGuessed = ""
  guessesTried = 0
  letters_correct = 0
#
  instrucText = "Welcome to the game Hangman!"
  instrucText += "\nI am thinking of a word that is "
  instrucText += str(guessWordLen)
  instrucText += " letters long."
  instrucText += "\nAvailable letters: "
  instrucText += available_letters
  instrucText += "\nYou have "
  instrucText += str(numGuessess)
  instrucText += " guesses."
  showInformation(instrucText)
#
  userGuess = ""
#    
  while (letters_correct != guessWordLen) and  (userGuess != "stop") and (guessesTried < numGuessess):
    userGuess = requestString("enter your guess:")
    if (userGuess == None):
      showInformation("You have clicked cancel.  If you would like to exit please enter the word stop.")
     
    elif (userGuess == "stop"):
       showInformation("Thank you for playing!")
      
    elif len(userGuess)> 1:
       showinformation("Too many letters, please only enter 1 letter!")
        
    elif len(userGuess) < 1:
       showInformation("Please only enter 1 letter! or the word stop ")
        
    elif  not(userGuess.isalpha()): 
       showinformation("Please only enter lowercase alpha letters.  No numbers or special characters")
        
    elif lettersGuessed.find(userGuess) != -1:
       showInformation("You already guess that letter.")
         
    else:
      lettersGuessed += userGuess
      numReplaced = findAndReplace(userGuess, guessWord, outputWord)
      if (numReplaced == 0):
        guessesTried += 1
        outputString = "Incorrect guess.\nYou have used " + str(guessesTried) + " of " + str(numGuessess) + " guessess "
      else:
        outputString = "Correct!!"
        letters_correct += numReplaced
      showInformation(outputString + "\nWord so far \n" + ' '.join(outputWord))
 #
  if not(userGuess == "stop"):
    if (guessesTried >= numGuessess):
      showInformation("Sorry you lost.\nThe word was " + guessWord)
    else:
      showInformation("Congratulations\nYou got in " + str(guessesTried + letters_correct) + " tries")
          
#
#
#==============================================================================
#  
#  ---- Main Driver
#    
#==============================================================================
#  
def mainDriver():
#
# warmup A
#
#  warmUpPartA()
#  warmUpPartB()
  hangman() 