from PIL import Image 

# open the picture
pic = Image.open("puppy.jpg")

# get the width and height of the picture
width = pic.width
height = pic.height

# go through every pixel:
# go through every column
for column in range(width):
  # and also go through every row
  for row in range(height):
    # get the original color and split into Red, Green, Blue (integers from 0 to 255)
    originalColor = pic.getpixel((column,row))
    originalRed = originalColor[0]
    originalGreen = originalColor[1]
    originalBlue = originalColor[2]

    # HERE IS WHERE YOU EDIT vvvvv
    newRed = originalRed
    newGreen = originalGreen
    newBlue = originalBlue
    
    newColor = (newRed, newGreen, newBlue)
    # put the new color back in the picture
    pic.putpixel((column,row), newColor)
      
# save the image under newPic.png (look for it in the "Files" bar to the left)
pic.save("newPic.png", "png")
