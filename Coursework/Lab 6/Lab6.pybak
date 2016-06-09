#===================================================
# CST205 Multimedia Design & Programming, Fall 2014 
# Professor Allie Xiong
#
# Student: Clarence Mitchell
#====================================================
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#       LAB 6
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++
#-------------------------------------------------------------
#  loadPic
#  inputs:  (none)
#  output:  picReturn - Picture loaded from disk
#-------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --load pics for other routines 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def loadPic():
  filename = pickAFile()
  print filename
  picReturn = makePicture(filename)
  return picReturn
  
#
#
#
#-------------------------------------------------------------
#  WARM UP
#-------------------------------------------------------------
#
#-------------------------------------------------------------
#  redEyeCorrection
#  inputs:  none
#  output:  none
#-------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --corrects red-eye to selected color
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def redEyeCorrection():
  hbPic = loadPic()
  picWidth = getWidth(hbPic)
  picHeight = getHeight(hbPic)
  show(hbPic)
  #
  redEyeColor = makeColor(113, 27, 12)
  newColor = pickAColor()
  # 
  # loop through half and lighten
  # 
  for x in range(53, 144):
    for y in range(127, 155):
      if ((x >= 53 and x <= 68) and (y >= 144 and y <= 155))  or  ((x >= 125 and x <= 144)  and (y >= 127 and y <= 139)):
        px =  getPixel(hbPic, x, y)
        color = getColor(px)
        if distance(color, redEyeColor) < 58.0:
          setColor(px, newColor)
      #if distance(color, ypicBlue) < 50.0:
      #  setColor(px, ltgray)
  #show(hbPic)
  repaint(hbPic)
  
def cheezburger(pic):
  c = makeColor(0, 0, 204)
  s = makeStyle(sansSerif, bold, 30)
  addTextWithStyle(pic, 20, 80, "ARRRRRRRR", s, c)
  repaint(pic)
  
#-------------------------------------------------------------
#  betterBnW - Makes picture Black and White
#  inputs:  hbPic  - Input picture to transform
#  output:  newPic - Black and White Picture
#-------------------------------------------------------------
def betterBnW(hbPic):
  picWidth = getWidth(hbPic)
  picHeight = getHeight(hbPic)
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(picWidth, picHeight)
  #
  # -- Set begining and ending for X and Y ranges
  beginX = 0
  beginY = 0
  endX = picWidth
  endY = picHeight
  stepY = 1
  stepX = 1
  # 
  # loop through left to right side
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      #
      #  get pixel and covert to black and white
      #
      oldPix = getPixel(hbPic, x, y)
      b = getBlue(oldPix)
      g = getGreen(oldPix)
      r = getRed(oldPix)
      gS =r*0.299 + g*0.587 + b*0.114
      newPix = getPixel(newPic, x, y)
      setColor(newPix,makeColor(gS,gS,gS))
  #
  #  -- return new picture
  #
  return newPic
#-------------------------------------------------------------
#  PROBLEM 1 Sepia
#  inputs:  (none)
#  output:  (none)
#-------------------------------------------------------------
#
# --make pictures look old,
def makeSepia():
  inPic = loadPic()  
  picWidth = getWidth(inPic)
  picHeight = getHeight(inPic)
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(picWidth, picHeight)
  #
  #  Step 1 - make picture black and White
  #
  newPic = betterBnW(inPic)
  #
  # Step 2 fade/yellow the picture
  #
  #
  # -- Set begining and ending for X and Y ranges
  beginX = 0
  beginY = 0
  endX = picWidth
  endY = picHeight
  stepY = 1
  stepX = 1
  # 
  # loop through left to right side
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      #
      #  get pixel and covert to faded
      #
      picPix = getPixel(newPic, x, y)
      r = getRed(picPix)
      if (r < 63):
        redMult = 1.1
        blueMult = 0.9
      elif (r > 62 and r < 192):
        redMult = 1.15
        blueMult = 0.85
      else:
        redMult = 1.08
        blueMult = 0.93
      #
      b = getBlue(picPix)
      g = getGreen(picPix)
      newRed = min((r * redMult), 255)
      newBlue = b * blueMult
      #gS = (r * redMult) + g + (b * blueMult)
      setColor(picPix,makeColor(newRed, g, newBlue))

  show(inPic)
  show(newPic)
  
#-------------------------------------------------------------
#  adjustColor - used by Artify routine
#  inputs:  inColor     - value for color
#  output:  adjColor  - adjusted color range
#-------------------------------------------------------------
def adjustColor(inColor):
  #
  #  Check color range and set adjustment
  #
  if (inColor < 63):
    adjColor = 31
  elif (inColor > 63 and inColor < 128):
    adjColor = 95
  elif (inColor > 127 and inColor < 192):
    adjColor = 159
  elif (inColor > 191 and inColor < 256):
    adjColor = 223
  else:
    adjColor = inColor
  #
  #
  #
  return adjColor
#
#-------------------------------------------------------------
#  PROBLEM 2 Art-i-fy
#-------------------------------------------------------------
#
# --posertization image
def Artify():
  inPic = loadPic()  
  picWidth = getWidth(inPic)
  picHeight = getHeight(inPic)
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(picWidth, picHeight)
  #
  #
  # -- Set begining and ending for X and Y ranges
  beginX = 0
  beginY = 0
  endX = picWidth
  endY = picHeight
  stepY = 1
  stepX = 1
  # 
  # loop through left to right side
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      #
      #  get pixel and covert to arty
      #
      picPix = getPixel(inPic, x, y)
      r = getRed(picPix)
      b = getBlue(picPix)
      g = getGreen(picPix)
      adjRed = adjustColor(r)
      adjBlue = adjustColor(b)
      adjGreen = adjustColor(g)
      newPix = getPixel(newPic, x, y)
      setColor(newPix,makeColor(adjRed, adjGreen, adjBlue))
  #
  #
  show(inPic)
  show(newPic)

#
#-------------------------------------------------------------
#  PROBLEM 3 GREEN SCREEN!
#-------------------------------------------------------------
#
# --Chroma-key effect on picture
#
# --make pictures look old,
def chromakey():
  #
  #  First load green screen picture
  #
  gsPic = loadPic()  
  gsPicWidth = getWidth(gsPic)
  gsPicHeight = getHeight(gsPic)
  #
  #  Next load green background picture
  #
  bkPic = loadPic()  
  bkPicWidth = getWidth(bkPic)
  bkPicHeight = getHeight(bkPic)
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(gsPicWidth, gsPicHeight)
  #
  #  make green screen color to check with
  #
  gsColor = makeColor(48, 254, 21)
  #
  # 
  #
  #
  # -- Set begining and ending for X and Y ranges
  beginX = 0
  beginY = 0
  endX = gsPicWidth
  endY = gsPicHeight
  stepY = 1
  stepX = 1
  # 
  # loop through left to right side
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      #
      #  get pixel and covert to faded
      #
      gsPicPix = getPixel(gsPic, x, y)
      gsPixColor = getColor(gsPicPix)
      if distance(gsPixColor, gsColor) < 130.0:
        bkPicPix = getPixel(bkPic, x, y)
        bkPixColor = getColor(bkPicPix)
        newPix = getPixel(newPic, x, y)
        setColor(newPix,bkPixColor)
      else:
        newPix = getPixel(newPic, x, y)
        setColor(newPix, gsPixColor)
 
  show(gsPic)
  show(bkPic)
  show(newPic)
 