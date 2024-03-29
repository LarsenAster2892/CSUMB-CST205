def halfRed():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for pix in pixels:
    r = getRed(pix)
    setRed(pix, r * 0.5)
  repaint(pic)

def noBlue():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for pix in pixels:
    setBlue(pix, 0)
  repaint(pic)

def lessRed(prc):
  filename  = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r * (prc/100))
  repaint(pic)

def moreRed(prc):
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, (r * (prc/100+1))%256)
  repaint(pic)
  
def roseColorGlasses():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    r = getBlue(p)
    setBlue(p ,r*0.7)
    r = getGreen(p)
    setGreen(p,r*0.7)
  repaint(pic)
 
def lightenUp():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
      newColor = getColor(p)
      newColor = makeLighter(newColor)
      setColor(p,newColor)
  repaint(pic)
   
def makeNegative():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
      b = getBlue(p)
      g = getGreen(p)
      r = getRed(p)
      negColor = makeColor(255-r,255-g,255-b)
      setColor(p,negColor)
  repaint(pic)
  
def BnW():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
      b = getBlue(p)
      g = getGreen(p)
      r = getRed(p)
      gS =(b+g+r)/3
      setColor(p,makeColor(gS,gS,gS))
  repaint(pic)
  
def betterBnW():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
      b = getBlue(p)
      g = getGreen(p)
      r = getRed(p)
      gS =r*0.299 + g*0.587 + b*0.114
      setColor(p,makeColor(gS,gS,gS))
  repaint(pic) 
 
