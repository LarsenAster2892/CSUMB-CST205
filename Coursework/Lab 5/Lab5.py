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
#       LAB 5
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#
# --- Lab 4 routines modified for lab 5
#
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
#-------------------------------------------------------------
#  halfBetter
#  inputs:  hbPic  - Input picture to transform
#  output:  newPic - Transformed picture
#-------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --lighten half the picture
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def halfBetter(hbPic):
  picWidth = getWidth(hbPic)
  picHeight = getHeight(hbPic)
  print picWidth , picHeight
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
      #
      # Set left side using ligther pixel
      #
      print x , y 
      oldPix = getPixel(hbPic, x, y)
      pixColor = getColor(oldPix)
      newColor = makeLighter(pixColor)
      newPixL = getPixel(newPic, x, y)
      setColor(newPixL, newColor)
      #
      # Set right side using nonlighter pixel
      #
      #  Calculate new location
      # 
      newX = ((picWidth -1) - x)
      newY = ((picHeight -1) - y)
      oldPix = getPixel(hbPic, newX, y)
      pixColor = getColor(oldPix)
      newPixR = getPixel(newPic, newX, y)
      setColor(newPixR, pixColor)
  #
  #  -- return new picture
  #
  return newPic
#
#-------------------------------------------------------------
#  vertMirror
#  inputs:  hbPic  - Input picture to transform
#  output:  newPic - Transformed picture
#-------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --Mirror half of a picture using a vertical mirror
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def vertMirror(hbPic):
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
  # loop through left to right side
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      oldPix = getPixel(hbPic, x, y)
      pixColor = getColor(oldPix)
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
  #  -- return new picture
  #
  return newPic
#
#-------------------------------------------------------------
#  topMirror
#  inputs:  hbPic  - Input picture to transform
#  output:  newPic - Transformed picture
#-------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --Mirror half of a picture horizontally from top to bottom
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
def topMirror(hbPic):
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
  endY = int(float(picHeight)/2.0 + 0.9)
  stepY = 1
  stepX = 1
  # 
  # loop through half and copy to bottom
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      oldPix = getPixel(hbPic, x, y)
      pixColor = getColor(oldPix)
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
  #  -- return new picture
  #
  return newPic
#
#-------------------------------------------------------------
#  bottomMirror
#  inputs:  hbPic  - Input picture to transform
#  output:  newPic - Transformed picture
#-------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --Mirror half of a picture horizontally from bottom to top
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def bottomMirror(hbPic):
  picWidth = getWidth(hbPic)
  picHeight = getHeight(hbPic)
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
      oldPix = getPixel(hbPic, x, y)
      pixColor = getColor(oldPix)
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
  #  -- return new picture
  #
  return newPic
#
#-------------------------------------------------------------
#  doubleMirror
#  inputs:  hbPic  - Input picture to transform
#  output:  newPic - Transformed picture
#-------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --Combine horizontal and vertical mirror for a quadruple mirror
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def doubleMirror(hbPic):
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
  endY = int(float(picHeight)/2.0 + 0.9)
  stepY = 1
  stepX = 1
  # 
  # loop through quarter and copy top, bottom both sides
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      oldPix = getPixel(hbPic, x, y)
      pixColor = getColor(oldPix)
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
  #  -- return new picture
  #
  return newPic
#
#-------------------------------------------------------------
#  simpleCopy
#  inputs:  hbPic  - Input picture to copy
#  output:  newPic - Copied picture
#-------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -- Creates a new blank picture and copies the picture into it
# -- Use the width and height of existing picture to set the size
# -- returning the new picture
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
  #
  #  -- return new picture
  #
  return newPic
#
#-------------------------------------------------------------
# rotatePic
#  inputs:  hbPic  - Input picture to transform
#  output:  newPic - Transformed picture
#-------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --copy original picture and rotate 90 degrees to the left
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def rotatePic(hbPic):
  picWidth = getWidth(hbPic)
  picHeight = getHeight(hbPic)
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
      oldpix = getPixel(hbPic, x, y)
      pixColor = getColor(oldpix)
      newX = y
      newY = ((picWidth -1) - x)
      #
      # copy picture pixel 
      newPixR = getPixel(newPic, newX, newY)
      setColor(newPixR, pixColor)
  show(hbPic)
  repaint(newPic)  
  return newPic
#
#-------------------------------------------------------------
#  shrink
#  inputs:  hbPic  - Input picture to transform
#           prc    - Percentage to adjust picture size 
#                    (example 80 is 80% )
#  output:  newPic - Transformed picture
#-------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --Copy a picture at percentage of the original size 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def shrink(hbPic, prc):
  picWidth = getWidth(hbPic)
  picHeight = getHeight(hbPic)
  #
  # Check precentage for negative  
  #
  if prc < 1:
    adjPrc = 100
  else:
    adjPrc = prc
  #
  #  Calculate factor and decimal percent
  #
  factor = 100.00 / float(adjPrc)
  decPrc = float(adjPrc) / 100.00
  #
  # used in debuging
  # print factor
  # print decPrc
  #
  #  Calculate with & height for new picture
  #
  newPicWidth = int(float(picWidth)* decPrc + 0.9)
  newPicHeight = int(float(picHeight) * decPrc + 0.9)
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(newPicWidth, newPicHeight)
  # 
  # loop through quarter and copy top, bottom both sides
  # 
  oldY = 0
  newY = 0
  while oldY <= picHeight - factor:
    oldX = 0
    newX = 0
    while oldX <= picWidth - factor:
      oldPix = hbPic.getPixel(int(oldX), int(oldY))
      oldPixColor = getColor(oldPix)
      #
      # copy picture pixel 
      #
      newPix = getPixel(newPic, newX, newY)
      setColor(newPix, oldPixColor)
      #
      oldX += factor
      newX += 1
    oldY += factor
    newY += 1
  return newPic

#++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#       LAB 5  routines....
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++

#
#
#-------------------------------------------------------------
#  WARM UP (expand)
#  inputs:  hbPic  - Input picture to transform
#  output:  newPic - Exanded canvas picture
#-------------------------------------------------------------
#
def expand(hbPic):
  picWidth = getWidth(hbPic)
  picHeight = getHeight(hbPic)
  newPicWidth = int(float(picWidth)* 2)
  newPicHeight = int(float(picHeight) * 2)
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(newPicWidth, newPicHeight)
  #
  # -- Set begining and ending for X and Y ranges
  beginX = 0
  beginY = 0
  endX = picWidth
  endY = picHeight
  stepY = 1
  stepX = 1
  #
  # --- Calculate picture offset
  #
  midNewPicX = int(float(newPicWidth) / 2.0 + 0.9)
  midNewPicY = int(float(newPicHeight) / 2.0 + 0.9)
  midOldPicX = int(float(picWidth) / 2.0 + 0.9)
  midOldPicY = int(float(picWidth) / 2.0 + 0.9)  
  offSetX = midNewPicX - midOldPicX
  offSetY = midNewPicY - midOldPicY
  # 
  # loop through quarter and copy top, bottom both sides
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      oldPix = getPixel(hbPic, x, y)
      pixColor = getColor(oldPix)
      newX = x + offSetX
      newY = y + offSetY
      #
      # copy picture pixel 
      newPixR = getPixel(newPic, newX, newY)
      setColor(newPixR, pixColor)
  return newPic

#
#-------------------------------------------------------------
#  PROBLEM 1
#  inputs:  source  - Input picture to copy
#           target  - Output picture 
#           targetX - X value in target to start copy
#           targetY - Y value in target to start copy 
#-------------------------------------------------------------
#
def pyCopy(source, target, targetX, targetY):
  srcPicWidth = getWidth(source)
  srcPicHeight = getHeight(source)
  tarPicWidth =  getWidth(target)
  tarPicHeight = getHeight(target)
  #
  # -- Create empty picture for use
  #newPic = makeEmptyPicture(newPicWidth, newPicHeight)
  #
  # -- Check targets for boundaries 
  #     and wrap if out of range, such as
  #       negative or past target picture boundaries
  #
  if targetX < 0:
    newTargetX = 0
  elif targetX > tarPicWidth:
    newTargetX = max((tarPicWidth - 1) - srcPicWidth, 0)
  else:
    newTargetX = targetX
  #
  if targetY < 0:
    newTargetY = 0
  elif targetY > tarPicHeight:
    newTargetY = max((tarPicHeight - 1) - srcPicHeight, 0)
  else:
    newTargetY = targetY
  #
  #
  # -- Set begining of range to start in source
  beginX = 0
  beginY = 0
  #
  # -- Set end of range 
  #    if will go over then wrap to end of target
  #
  if (srcPicWidth + newTargetX) > tarPicWidth:
    endX = tarPicWidth - newTargetX
  else:
    endX = srcPicWidth
  #
  if (srcPicHeight + newTargetY) > tarPicHeight:
    endY = tarPicHeight - newTargetY
  else:
    endY = srcPicHeight
  #
  # --- Set step
  # 
  stepY = 1
  stepX = 1
  #
  # --- Calculate picture offset
  #
  offSetX = min(targetX, tarPicWidth)
  offSetY = min(targetY, tarPicHeight)
  # 
  # loop through quarter and copy top, bottom both sides
  # 
  for x in range(beginX, endX, stepX):
    for y in range(beginY, endY, stepY):
      srcPix = getPixel(source, x, y)
      srcPixColor = getColor(srcPix)
      newX = x + newTargetX
      newY = y + newTargetY
      #
      # copy picture pixel 
      tarPix = getPixel(target, newX, newY)
      setColor(tarPix, srcPixColor)
  #show(source)
  #repaint(target)  
#
#-------------------------------------------------------------
#  PROBLEM 2
#  inputs:  (none)
#  output:  (none)
#-------------------------------------------------------------
#
#  Transform pictures to 8.5 x 11 with 120 dpi 
#
def transformPics():
  newPicWidth = 1020
  newPicHeight = 1320
  #
  # -- Create empty picture for use
  newPic = makeEmptyPicture(newPicWidth, newPicHeight)
  #
  # --- Calculate the increment in pixels
  #
  xIncrement = int((2.83 * 120) + 0.9)
  yIncrement = int((3.66 * 120) + 0.9)
  #
  #
  #
  for picNum in range(1,10):
    inPic = loadPic()  
    picWidth = getWidth(inPic)
    picHeight = getHeight(inPic)
 
    offSetX = ((picNum -1) % 3) * xIncrement
    offSetY = ((picNum -1) / 3) * yIncrement    
    tranNum = (picNum % 6)
    if tranNum == 0:
      transPic=simpleCopy(inPic)   
    elif tranNum == 1:
      transPic=simpleCopy(inPic)
    elif tranNum == 2:
      transPic=vertMirror(inPic)  
    elif tranNum == 3:
      transPic=topMirror(inPic)   
    elif tranNum == 4:
      transPic=bottomMirror(inPic)   
    else:
      transPic=doubleMirror(inPic)
 
    pyCopy(transPic, newPic, offSetX, offSetY)  
    show(inPic)
  writePictureTo(newPic,"C://Users//LN//Pictures//CST205Output.jpg")  
  repaint(newPic)  
