#===================================================
# CST205 Multimedia Design & Programming, Fall 2014 
# Professor Allie Xiong
#
# Student: Clarence Mitchell
#====================================================
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#       LAB 4
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++


# Picture load routine
# This routine is used to load pics for other routines 
def loadPic():
  filename = pickAFile()
  print filename
  picReturn = makePicture(filename)
  return picReturn
#-------------------------------------------------------------
#  savePicture()
#    saves a picture from JES memory to disk location
#  inputs:   source     - Input picture 
#  output:              - Picture file written to disk
#-------------------------------------------------------------
def savePicture(source):
  writePictureTo(picture, pickAFile())
  print "Your file was successfully saved!"

#
#
#-------------------------------------------------------------
#  WARM UP
#-------------------------------------------------------------
#
#Write function called halfBetter()....optional what it does, except must be
#done to half the pictuer. (Ex. Make picture lighter)

def halfBetter(hbPic):
  picWidth = getWidth(hbPic)
  picHeight = getHeight(hbPic)
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(picWidth, picHeight)
  #
  # -- Set begining and ending for X and Y ranges
  beginX = 0
  beginY = 0
  endX = int(float(picWidth)/2.0 +0.9)
  endY = picHeight
  stepY = 1
  stepX = 1
  # 
  # loop through half and lighten
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      pix = getPixel(hbPic, x, y)
      pixColor = getColor(pix)
      newColor = makeLighter(pixColor)
#      
      newPix = getPixel(newPic,  x, y)
      setColor(newPix, newColor)     
#
  repaint(newPic)
  return newPic
 
      
  
#
#-------------------------------------------------------------
#  PROBLEM 1
#-------------------------------------------------------------
#
# --Mirror half of a picture using a vertical mirror

def vertMirror(vmPic):
  picWidth = getWidth(vmPic)
  picHeight = getHeight(vmPic)
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(picWidth, picHeight)
  #
  # -- Set begining and ending for X and Y ranges
  beginX = 0
  beginY = 0
  endX = int(float(picWidth)/2.0 +0.9)
  endY = picHeight
  stepY = 1
  stepX = 1
  # 
  # loop through left to right side
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      oldpix = getPixel(vmPic, x, y)
      pixColor = getColor(oldpix)
      newX = ((picWidth -1) -x)
      newY = ((picHeight -1) - y)
      #
      # set left side
      newPixL = getPixel(newPic, x, y)
      setColor(newPixL, pixColor)
      #
      # set right side 
      newPixR = getPixel(newPic, newX, y)
      setColor(newPixR, pixColor)
#
  repaint(newPic)
  return newPic
#
#
#--- Mirror half of a picture horizontally from top to bottom
#
def topMirror(tmPic):
  picWidth = getWidth(tmPic)
  picHeight = getHeight(tmPic)
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(picWidth, picHeight)
  #
  # -- Set begining and ending for X and Y ranges
  beginX = 0
  beginY = 0
  endX = picWidth
  endY = int(float(picHeight)/2.0 + 0.9)
  stepY = 1
  stepX = 1
  # 
  # loop through half and copy to bottom
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      oldpix = getPixel(hbPic, x, y)
      pixColor = getColor(oldpix)
      newX = ((picWidth -1) -x)
      newY = ((picHeight -1) - y)
      #
      # set top half
      newPixL = getPixel(newPic, x, y)
      setColor(newPixL, pixColor)
      #
      # set bottom half 
      newPixR = getPixel(newPic, x, newY)
      setColor(newPixR, pixColor)
#
  repaint(newPic)
  return newPic
#
# ---- Mirror half of a picture horizontally from bottom to top
#
def bottomMirror(bmPic):
#
  picWidth = getWidth(bmPic)
  picHeight = getHeight(bmPic)
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(picWidth, picHeight)
  #
  # -- Set begining and ending for X and Y ranges
  beginX = 0
  beginY = int(float(picHeight)/2.0 + 0.9)
  endX = picWidth
  endY = picHeight-1
  stepY = 1
  stepX = 1
  # 
  # loop through bottom and copy to top
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      oldpix = getPixel(bmPic, x, y)
      pixColor = getColor(oldpix)
      newX = ((picWidth -1) -x)
      newY = ((2 * beginY) - y - 1)
      #
      # set top half
      newPixT = getPixel(newPic, x, newY)
      setColor(newPixT, pixColor)
      #
      # set bottom half 
      newPixB = getPixel(newPic, x, y)
      setColor(newPixB, pixColor)
#
  repaint(newPic)
  return newPic

#Combine one horizontal mirror with a vertical mirror for a quadruple mirror
#This should create four functions
def doubleMirror(dmPic):
  hbPic = loadPic()
  picWidth = getWidth(dmPic)
  picHeight = getHeight(dmPic)
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(picWidth, picHeight)
  #
  # -- Set begining and ending for X and Y ranges
  beginX = 0
  beginY = 0
  endX = int(float(picWidth)/2.0 +0.9)
  endY = int(float(picHeight)/2.0 + 0.9)
  stepY = 1
  stepX = 1
  # 
  # loop through quarter and copy top, bottom both sides
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      oldpix = getPixel(dmPic, x, y)
      pixColor = getColor(oldpix)
      newX = ((picWidth -1) -x)
      newY = ((picHeight -1) - y)
      #
      # set top left side
      newPixL = getPixel(newPic, x, y)
      setColor(newPixL, pixColor)
      #
      # set top right side 
      newPixR = getPixel(newPic, newX, y)
      setColor(newPixR, pixColor)
      #
      # set bottom left half
      newPixT = getPixel(newPic, x, newY)
      setColor(newPixT, pixColor)
      #
      # set bottom right half 
      newPixB = getPixel(newPic, newX, newY)
      setColor(newPixB, pixColor)
#
  repaint(newPic)
  return newPic  
#-------------------------------------------------------------
#  PROBLEM 2
#-------------------------------------------------------------
#Write a function called simpleCopy() that takes a picture as a parameter
#It creates a new blank picture and copies the picture into it, returning the new picture
#Use the width and height of existing picture to set the size

def simpleCopy(hbPic):
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
  # loop through quarter and copy top, bottom both sides
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      oldpix = getPixel(hbPic, x, y)
      pixColor = getColor(oldpix)
      newX = x
      newY = y
      #
      # copy picture pixel 
      newPixR = getPixel(newPic, newX, newY)
      setColor(newPixR, pixColor)
  show(hbPic)
  repaint(newPic)  
  return newPic
#
#-------------------------------------------------------------
#  PROBLEM 3
#-------------------------------------------------------------
#
#Write function called rotatePic()
#It will copy original picture and rotate 90 degrees to the left, returning new picture
#Again, use the width and height of existing picture to set size

def rotatePic(rbPic):
  picWidth = getWidth(rbPic)
  picHeight = getHeight(rbPic)
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(picHeight, picWidth)
  #
  # -- Set begining and ending for X and Y ranges
  beginX = 0
  beginY = 0
  endX = picWidth
  endY = picHeight
  stepY = 1
  stepX = 1
  # 
  # loop through quarter and copy top, bottom both sides
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      oldpix = getPixel(rbPic, x, y)
      pixColor = getColor(oldpix)
      newX = y
      newY = ((picWidth -1) - x)
      #
      # copy picture pixel 
      newPixR = getPixel(newPic, newX, newY)
      setColor(newPixR, pixColor)
#
  repaint(newPic)  
  return newPic
# 
#-------------------------------------------------------------
#  PROBLEM 4
#-------------------------------------------------------------
#
#Write function called shrink()
#It will copy the picture at half the original size, by sampling the original picture
#Keep every other pixel from the original image, using range(x,x,x)

def shrink(sbPic):
  picWidth = getWidth(sbPic)
  picHeight = getHeight(sbPic)
  newPicWidth = int(float(picWidth)* 0.5 + 0.9)
  newPicHeight = int(float(picHeight) * 0.5 + 0.9)
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(newPicWidth, newPicHeight)
  #
  # -- Set begining and ending for X and Y ranges
  beginX = 0
  beginY = 0
  endX = picWidth
  endY = picHeight
  stepY = 2
  stepX = 2
  # 
  # loop through quarter and copy top, bottom both sides
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      oldpix = getPixel(sbPic, x, y)
      pixColor = getColor(oldpix)
      newX = int(float(x)*0.5 + 0.5)
      newY = int(float(y)*0.5 + 0.5)
      #
      # copy picture pixel 
      newPixR = getPixel(newPic, newX, newY)
      setColor(newPixR, pixColor)
  #
  repaint(newPic)  
  return newPic
# 
#-------------------------------------------------------------
#  Main Driver
#-------------------------------------------------------------
#
def mainDriver():
  FileChooser.setMediaPath("C:/Users/LN/Documents/7. Education/Classess/Current/CST205/Labs/Lab 4/Images/Before")
  inPic = (makePicture(getMediaPath("Winery_Treliss.jpg"))) 
  show(inPic)
#
# -- transform picture
#
  picHalfBetter = halfBetter(inPic)
  picVertMirror = vertMirror(inPic)
  picTopMirror = topMirror(inPic)  
  picBottomMirror = bottomMirror(inPic)
  picDoubleMirror = doubleMirror(inPic)
  picRotate = rotatePic(inPic)
  picShrink = shrink(inPic)
#
  FileChooser.setMediaPath("C:/Users/LN/Documents/7. Education/Classess/Current/CST205/Labs/Lab 4/Images/Transformed")
  writePictureTo(picture, getMediaPath("halfBetter.jpg"))
  writePictureTo(picture, getMediaPath("VertMirror.jpg"))
  writePictureTo(picture, getMediaPath("TopMirror.jpg")
  writePictureTo(picture, getMediaPath("BottomMirror.jpg")
  writePictureTo(picture, getMediaPath("picDoubleMirror.jpg")
  writePictureTo(picture, getMediaPath("picRotat.jpg")
  writePictureTo(picture, getMediaPath("picShrink.jpg")