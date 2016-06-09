def pickAndOpenPic():
  filename = pickAFile()
  mypic = makePicture(filename)
  show(mypic)
  

def showNamedPic(filename):
  mypic = makePicture(filename)
  show(mypic)
  
def halfRed():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for pix in pixels:
    r = getRed(pix)
    setRed(pix, r * 0.5)
  repaint(pic)
  
def lessRed(inpercent):
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for pix in pixels:
    r = getRed(pix)
    setRed(pix, r * (inpercent / 100))
  repaint(pic)
  
def moreRed(inpercent):
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for pix in pixels:
    r = getRed(pix)
    setRed(pix, (((r * 100)/ inpercent) % 256))
  repaint(pic)
  
def roseColoredGlasses():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for pix in pixels:
    r = (getRed(pix) * 0.93) %256
    setRed(pix, r)
    
    b = (getBlue(pix) * 0.56) % 256
    setBlue(pix, b )
    
    g = (getGreen(pix) * 0.17) % 256
    setGreen(pix, g)
    
  repaint(pic)