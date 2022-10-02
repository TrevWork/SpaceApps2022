from PIL import Image, ImageFilter
photochoice = input("Please choose your JUNOCAM photo to be processed: A: PeriJove 44 Jet N7, or B: PeriJove 45 North Pole.")

if photochoice == 'A':
    image = Image.open('jupiter1improve.png')

    red, green, blue, alpha = image.split()

    print(image.mode) 
    print(red.mode)
    print(green.mode) 
    print(blue.mode) 
    new_image = Image.merge("RGB", (red, green, blue)) #customisable to change the image
    new_image.save('new_image.jpg')

    print(new_image.mode) 

else: 
    image = Image.open('jupiter2.png')

    red, green, blue, alpha = image.split()

    print(image.mode) 
    print(red.mode) 
    print(green.mode) 
    print(blue.mode) 

    new_image = Image.merge("RGB", (red, green, blue))
    new_image.save('new_image2.jpg')

    print(new_image.mode)



PYTHON SHELL

(sudo) pip3 install pillow
(sudo) pip3 install pysimplegui
