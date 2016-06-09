
def turkeyCard():
  #
  # Load main picture and two p
  #
  pic = makePicture(pickAFile())
  pic2 = makePicture(pickAFile())
  pic3 = makePicture(pickAFile())
  #
  #  Add text on picture
  #
  c = makeColor(white)
  s = makeStyle(sansSerif, bold, 30)
  addTextWithStyle(pic, 250, 80,"Happy Turkey Day", s, c,)
  #
  #
  #
  repaint(pic)
  
#
#-------------------------------------------------------------
#  PROBLEM 1
#  inputs:  source  - Input picture to copy
#           target  - Output picture 
#           targetX - X value in target to start copy
#           targetY - Y value in target to start copu 
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