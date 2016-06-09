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
#       LAB 7
#
#++++++++++++++++++++++++++++++++++++++++++++++++++++
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
  
## PRE FUNCTIONS
# This function saves an image from JES memory to
# the location of your choice using pickAFile() file browser.
# USAGE: saveFile(yourPicHere)
 
def saveFile(picture):
  writePictureTo(picture, pickAFile())
  print "Your file was successfully saved!"


#######################################################################
# --- WARM UP
#######################################################################
def desertSnow():
  #desert = '/home/avendanl/Pictures/desert.jpeg'  # variable filename hold the path
  #carrot = '/home/avendanl/Pictures/Carrot2.png'
  #pic = makePicture(desert)                      # variable pic holds the object picture from filename.
  #pic2 = makePicture(carrot)
  #
  pic = loadPic()
  pic2 = loadPic()
  #
  #
  #
  color =  makeColor(255, 255, 255)
  pic.addOvalFilled(white, 148, 110, 15, 15)
  pic.addOvalFilled(white, 145, 120, 20, 20)
  pic.addOvalFilled(white, 140, 135, 30, 30)
  pic.addOvalFilled(black, 154, 113, 5, 5)
  pic.addOvalFilled(black, 148, 113, 5, 5)
  copyInto(pic2, pic, 146, 118)
  repaint(pic)
#
#
#-------------------------------------------------------------------------------
#  chromaKeyCopy - Copies one picture into another replace chromakey background
#  inputs:  source  - Input picture to copy
#           target  - Output picture 
#           targetX - X value in target to start copy
#           targetY - Y value in target to start copy
#           tolaranceFactor - number for color differnce with chromakey 
#------------------------------------------------------------------------------
#
def chromaKeyCopy(source, target, targetX, targetY, tolaranceFactor):
  srcPicWidth = getWidth(source)
  srcPicHeight = getHeight(source)
  tarPicWidth =  getWidth(target)
  tarPicHeight = getHeight(target)
  #
  #  make green screen color to check with
  #
  gsColor = makeColor(60, 255, 54)
  #
  # -- Check targets for boundaries 
  #     and wrap if out of range, such as
  #       negative or past target picture boundaries
  #
  #
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
      #srcPixGrn = getGreen(srcPix)
      #srcPixBlu = getBlue(srcPix)
      #srcPixRed = getRed(srcPix)
      #
      # - Calculate target x & y
      newX = x + newTargetX
      newY = y + newTargetY
      #
      #  - Get Target Pixel
      tarPix = getPixel(target, newX, newY)
      #
      # - Check for Chroma-key background
      #
      #if getGreen(srcPix) > getBlue(srcPix) and getGreen(srcPix) > getRed(srcPix):
      if distance(srcPixColor, gsColor) < tolaranceFactor:
        srcPixColor = getColor(tarPix)
      else:
        srcPixColor = getColor(srcPix)
      #
      # copy color to target 
      #  
      setColor(tarPix, srcPixColor)
  #show(source)
  #repaint(target)  
#
#
#
#-------------------------------------------------------------------------------
#  ======== MAIN Driver ===============================
#   turkeyCard()
#
#------------------------------------------------------------------------------
#

def turkeyCard():
  #
  # Load main picture and two p
  #
  picBackground = loadPic()
  #
  # Load Pumpkin image
  picImage1 = loadPic()
  #
  #  Load horn-of-plenty image
  picImage2 = loadPic()
  #
  #  Load group image image
  picImage3 = loadPic()
  #
  #  Add text on picture
  #
  textColor = makeColor(white)
  textStyle = makeStyle(sansSerif, bold, 30)
  addTextWithStyle(picBackground, 250, 80,"Happy Turkey Day", textStyle, textColor,)
  addTextWithStyle(picBackground, 230, 120,"From Team Otter Design", textStyle, textColor,)
  #
  # Add images
  #
  chromaKeyCopy(picImage1, picBackground, 35, 743, 150)
  chromaKeyCopy(picImage2, picBackground, 400, 691, 120 )
  chromaKeyCopy(picImage3, picBackground, 56, 309, 60)
  #
  #  Show final image
  #
  repaint(picBackground)
  
