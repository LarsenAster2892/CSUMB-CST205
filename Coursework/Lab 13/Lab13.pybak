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
#       Lab 13
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#  The following is information about this program
#   1) Uses an triple quotes to creat a long string for the story
#   2) Use a dictionary to store users input
#++++++++++++++++++++++++++++++++++++++++++++++++++++
                                                     
newsStory = """
{profession} {fname} {lname} was on a trip to {place} 
when an endangered {animal} grabbed the camera and started taking hundreds of pictures.  

When viewing the shots, there was an incredible selfie of the
grinning {animal} staring right into the camera lense.  
The pictures went viral in newspapers, websites and magazines 
across the globe and the {profession}'s work was thrust into 
the internet spotlight.

It was originally requested the picture be taken off Wikipedia 
in {year} and it was removed. But then it was re-posted and Wikipedia
stated that under U.S. law any picture taken by an animal cannot have copyright.
Wikipedia told the {newspaper}: The work did not originate from {lname} as by
their own admission they did not take the picture, the {animal} did. 
However {animal}s can’t and don't own copyrights.

{lname} said recently: When I saw the picture I was just {emotion}ing it. 
It was made even better when the story was picked up and it made 
thousands of people around the world happy.
I had letters of congratulations from people as far as {location} saying it had made their day.
{lname}  said: It makes me very {emotion}ing, I'm a professional {profession} - 
it costs me over {amount} dollars to do the trip. It's my livelihood.
You take {number} shots to get one image that sells, 
it was potentially a good earner for me, I've lost over {amount} dollars because of it.
                                                       
The End                                                
"""                                                   
#-------------------------------------------------------------------------------
#
#  Get the name of the player
#    
#------------------------------------------------------------------------------
def getPlayerName():
#
#  -- make new sound that range of start to end
#
  pfirstName = requestString("What is your first name?")
  plastName = requestString("What is your last name?")
  playerName = pfirstName + " " + plastName
  showInformation("Hello " + playerName)
  return playerName

#
#-------------------------------------------------------------------------------
#
#  prompts the user of replacement data and adds it to a dictionary  
#    
#------------------------------------------------------------------------------

def getUserPicks(cue, dictKey, dictionary): 
  #                         
  # Prompt the  user response using the build string,
  # and place the response a the dictionary. 
  # 
  prompt = "Enter a %s: " % cue                                              
  response = raw_input(prompt) 
  #repsonse = = requestString(prompt)                          
  dictionary[dictKey] = response                         
#
#-------------------------------------------------------------------------------
#
#  loop through each item in the dictionary and replace values in string  
#    
#------------------------------------------------------------------------------
def replaceMarkers(madlibText, userDict):
  for dItem in userDict:
    fValue = "{" + dItem + "}"
    print fValue, userDict[dItem]
    madlibText = madlibText.replace(fValue,  userDict[dItem])
  return madlibText

#
#-------------------------------------------------------------------------------
#
#  Main driver 
#    
#------------------------------------------------------------------------------
       
def tellStory(): 
    
    showInformation("This madlib games tells a story using your input")                                      
    userPicks = dict()                                 
    getUserPicks("Team Member's first name","fname", userPicks)                       
    getUserPicks("Different Team Member's last name","lname", userPicks)    
    getUserPicks("place on campus","place", userPicks)
    getUserPicks("another university","location", userPicks)
    getUserPicks("type of pet","animal", userPicks)
    getUserPicks("computer job","profession", userPicks)
    getUserPicks("past year","year", userPicks)
    getUserPicks("tabloid magazine","newspaper", userPicks)
    getUserPicks("emotion","emotion", userPicks)                         
    getUserPicks("dollar amount","amount", userPicks)
    getUserPicks("random number","number", userPicks)
    newStory = replaceMarkers(newsStory, userPicks)
    print newStory
                                                     
                                                      
