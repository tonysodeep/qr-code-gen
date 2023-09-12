
from segno import helpers

import qrcode

first_name = "Hy"
last_name = "Nguyen"
middle_name = "Gia"
email = "hynguyen2727@gmail.com"
phone_number = "0983100028"
phone_number_fm = '+84 ' + phone_number[1:]

# reate the vCard string
vcard_template = f'''BEGIN:VCARD
VERSION:3.0
N:Dang;Chi;;Mr.;Chi;
FN:Chi Dang
TITLE:CEO
ORG:Streamline Enterprise Co. Ltd 
URL:https://streamlinevn.com/
EMAIL;TYPE=INTERNET:chi.dang@streamlinevn.com
TEL;TYPE=voice,work,pref:{phone_number_fm}
ADR;TYPE=work:Unit G1516, The Manor II building;89;Nguyen Huu Canh, Binh Thanh District, HCM City
END:VCARD'''

# Generate the QR code
qr = qrcode.QRCode(
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=5,
    border=2,
)

qr.add_data(vcard_template)
qr.make(fit = True)

img = qr.make_image(fill_color="red", back_color="#23dda0")

# Save the QR code image
img.save('build/vcard-qrcode.png')

