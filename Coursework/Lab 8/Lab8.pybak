#===================================================
# CST205 Multimedia Design & Programming, Fall 2014 
# Professor Allie Xiong
# Team 5: <Otter Design>
# Members: 
#          Clarence Mitchell
#          Caitlin Kuleck
#          Gracie Alderete-Fisher
#          Luciano Avendano
#====================================================
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#       LAB 8
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
#
#-------------------------------------------------------------------------------
#  increaseVolume - 
#      takes a sound object and increase the volume by double
#  inputs:  inSound     - Input sound to change volume
#    
#------------------------------------------------------------------------------
def increaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * 2)
#
#
#-------------------------------------------------------------------------------
#  changeVolume - 
#      takes a sound object and a factor that tells you how much to increase (or decrease) the volume by
#  inputs:  inSound     - Input sound to change volume
#           volFactor   - number for color differnce with chromakey 
#------------------------------------------------------------------------------
#
def changeVolume(sound, volFactor):
  #
  #  Loop through the samples and adjust by volume Factor (volFactor
  #    
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * volFactor)
#
#-------------------------------------------------------------------------------
#  decreaseVolume - 
#      takes a sound object and reduces the volume by half
#  inputs:  inSound     - Input sound to change volume
#    
#------------------------------------------------------------------------------
#  
def decreaseVolume(sound):
  changeVolume(sound, 0.5)
  
#
#-------------------------------------------------------------------------------
#  newIncreaseVolume - 
#      takes a sound object and increase the volume by double
#  inputs:  inSound     - Input sound to change volume
#    
#------------------------------------------------------------------------------
#  
def newIncreaseVolume(sound):
  changeVolume(sound, 2)
 
#
#
#-------------------------------------------------------------------------------
#  maxSample - 
#      finds the maximum sample value in a sound
#  inputs:  inSound     - Input sound to find valude in
#  output:  maxVolume   - Maxvolume located
#------------------------------------------------------------------------------
#
def maxSample(sound):
  #
  #  since lowest value is -32768 set value to 1 lower
  #   to check if sound was valid
  #
  maxVolume = -32769
  #
  #  Loop through the samples and adjust by volume Factor (volFactor
  #    
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    maxVolume = max(value, maxVolume)
#
  return maxVolume
#
#
#-------------------------------------------------------------------------------
#  maxVolume - 
#       increases the volume of each sample by the factor (factor=32767/largest) where largest is the value
#  inputs:  inSound     - Input sound 
#  output:  maxVolume   - Maxvolume located
#------------------------------------------------------------------------------
#
def maxVolume(sound):
  #
  #  First find maxVolume
  #
  maxVolume = maxSample(sound)
  print "Max volume in sound is ", maxVolume
  #
  # Next calculate volume increase factor
  #   
  incFactor = 32767/maxVolume
  print "Increase factor is ", incFactor
  #
  #  now change the volume by increment factor
  #
  changeVolume(sound, incFactor)
#
#
#-------------------------------------------------------------------------------
#  goToEleven - 
#       For each sample, 
#        if the sample value is greater than 0, 
#           it sets the sample value to the maximum possible value: 32767. 
#        If the sample value is less than 0, 
#           it sets the sample value to the minimum possible value: -32768.
#  inputs:  inSound     - Input sound 
#  output:  maxVolume   - Maxvolume located
#------------------------------------------------------------------------------
#
def goToEleven(sound):
  #
  #  Loop through the samples and adjust by volume Factor (volFactor
  #    
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, 32767)
    elif value < 0:
      setSampleValue(sample, -32768)
    else:
      setSampleValue(sample, value)
#
#
#
#==============================================================================
#  
#  ---- Main Driver
#    
#==============================================================================
#  
def mainDriver():
#  snd1 = loadSnd()
#  explore(snd1)
#  decreaseVolume(snd1)
#  explore(snd1)
#
#  snd2 = loadSnd()
#  explore(snd2)
#  newIncreaseVolume(snd2)
#  explore(snd2)
#  print snd2
  
#  snd3 = loadSnd()
#  maxVol = maxSample(snd3)
#  strPrint = "max volume is " + repr(maxVol)
#  explore(snd3)
#  showInformation(strPrint)
 
#  snd4 = loadSnd()
#  explore(snd4)
#  maxVol = maxVolume(snd4)
#  explore(snd4)
#  showInformation("Done") 
  
  snd5 = loadSnd()
  explore(snd5)
  goToEleven(snd5)
  explore(snd5)
  showInformation("Done") 