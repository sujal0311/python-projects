import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=1,)
data=input("Enter the link to be converted : ")
save_name=input("Enter the image name  to be saved with the format: ")
font=input("Enter the colour of the code : ")
background=input("Enter the background colour of the code : ")
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill_color=font,back_color=background)
image.save(save_name)
