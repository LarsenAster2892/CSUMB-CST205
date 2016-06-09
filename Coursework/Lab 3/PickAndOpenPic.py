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