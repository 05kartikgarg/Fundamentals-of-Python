#Installation
# pip install qrcode[pil]


#-------------- simple QRcode------------------------

import qrcode
a=qrcode.make('I love programming and Python is my favourite language.')
a.save('code1.png')
#a.save('code1.jpg')
#a.save('code1.pdf')
#a.save('code1.svg')


#------------------Resizing the QRcode------------------

##import qrcode
##q=qrcode.QRCode( version=1,
##                 box_size=15,
##                 border=5
##                 )
##data="https://www.youtube.com"
##q.add_data(data)
##q.make(fit=True)
##img=q.make_image(fill='red',back_color='white')
##img.save('code2.png')
