import qrcode
from PIL import Image
from io import BytesIO
link = "#" # Past your Google Drive link hear.
img=qrcode.make(link)
img.save("qr_code.png")
with open("qr_code.png", "rb") as image_file:
    Image = Image.open(BytesIO(image_file.read()))