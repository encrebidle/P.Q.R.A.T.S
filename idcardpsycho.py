# works on python 2.x as well as 3.x , install modules as required to run using pip in cmd
# pip install Pillow   for PIL module
from PIL import Image, ImageDraw, ImageFont
import qrcode
image = Image.new('RGB', (1000,900), (255, 245, 245))
draw = ImageDraw.Draw(image)

# Change Roboto-Bold.ttf  to any other like Calibri, Its up to you
font = ImageFont.truetype('arial.ttf', size=45)
import random
import os
import datetime
os.system("title ID CARD Generator by Kumar Atulya B.tech C.S.E ")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t Digital ID CARD \t\t\t\t\t  %I:%M:%S %p")
print ('+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*')
print (reg_format_date)
print ('+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*')
 
# starting position of the message as documentation
print('\n\nAll Fields are Mandatory') 
print('Avoid any kind of Spelling Mistakes')
print('Write Everything in as Titles ')



(x, y) = (160, 40)
name = input('\nEnter Your FULL Name: ')

color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), name, fill=color, font=font)



# adding an unique id number using random function. You can manually take it from user by input function
(x, y) = (600, 10)
idno = input ('ID no Assigned :')
message= idno
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)





(x, y) = (50, 130)
message = input('Enter Your STREAM Name: ')
stream =message
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), message, fill=color, font=font)




(x, y) = (50, 180)
message = input('Enter Your branch & year: ')
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)
(x, y) = (50, 240)
message = input('Enter Your Gender: ')
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)




(x, y) = (50, 300)
message = input('Enter Your Date Of Birth: ')
color = 'rgb(128, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)




(x, y) = (50, 360)
message = input('Enter Your Blood Group: ')
color = 'rgb(255, 255, 0)' # RED color 
draw.text((x, y), message, fill=color, font=font)




(x, y) = (50, 420)
message = input('Enter Your Mobile Number: ')
temp=message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)





(x, y) = (50, 480)
message = input('Enter Your Address: ')
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)






# save the edited image in current directory.
 
image.save(str(name)+'.png')







from PIL import Image
til = Image.open(name+'.png')       #open saved qr code and save it to final image
im = Image.open(name+'.bmp')
til.paste(im,(610,140))
im1 = Image.open('cropimage.png')
til.paste(im1,(690,520))
im2=Image.open('itmlogo.png')
til.paste(im2,(10,10))

im3=Image.open('footer.png')
til.paste(im3,(0,800))

til.save(name+'.png')

print('\n\n\nYour ID Card Successfully created in a PNG file '+name+'.png')
input('\n\nPress any key to Close program...')   #use input yo hold the screen
