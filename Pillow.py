
# installation of pillow library 
# change the image extension 
# resize image files
# resize multiple images using for loop  
# Sharpness 
# Brightess 
# Color
# Contrast 
# Image blur , GaussianBlur

#----------------------------Basic-------------------------------------

#from PIL import Image

#img1=Image.open('dog1.jpg')

#img1.show()
#img1.save('dog1.pdf')
#img1.save('dog1.png')

'''Image Resize'''

#MAX_SIZE = (250,250)
#img1.thumbnail(MAX_SIZE)
#img1.save('dog1small.jpg')


'''-----------------------------change extension of multiple images simultaneously-------------------'''

##from PIL import Image
##import os 
##
##for item in os.listdir():
##     if item.endswith('.jpg'):
##         img1 = Image.open(item)
##         filename,extension = os.path.splitext(item)
##         img1.save(f'{filename}.png')


'''--------------------------- Adjust the properties of image---------------------------------------'''
#from PIL import Image, ImageEnhance

#sharpness

##img1 = Image.open('dog1.jpg')
##enhancer = ImageEnhance.Sharpness(img1)
##enhancer.enhance(5).save('dog1edited.jpg')
'''
0 : blurry 
1: original image 
2 : image with increased sharpness
'''

# -------color ---------
##img1 = Image.open('dog1.jpg')
##enhancer = ImageEnhance.Color(img1)
##enhancer.enhance(2).save('dog1edited.jpg')

# --------brightness -----------
##img1 = Image.open('dog1.jpg')
##enhancer = ImageEnhance.Brightness(img1)
##enhancer.enhance(1.5).save('dog1edited.jpg')

#----------Contrast-----------------
##img1 = Image.open('dog1.jpg')
##enhancer = ImageEnhance.Contrast(img1)
##enhancer.enhance(1.5).save('dog1edited.jpg')



'''-----------------------------------Blurr the Image----------------------------------------------'''
##from PIL import Image,ImageFilter
##
##img1= Image.open('dog2.jpg')
##
##img1.filter(ImageFilter.GaussianBlur(radius=4)).save('dog1edited.jpg')

















