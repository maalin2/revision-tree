import fitz, sys, pathlib

#get pdf from flask system

#grab img
def img(path):
    doc = fitz.open(path)  
    for page in doc: 
            pix = page.get_pixmap()
            pix.save("p%i.png" % page.number)

img("assets/pse-ch10.pdf")
#grab text to return to ai
def scrape_text(img):
      return None