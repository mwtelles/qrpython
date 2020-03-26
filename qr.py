import qrcode

# qr = qrcode.make('hello world')
# qr.save('Myqr.png')

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
    )
a = input('Digite o que quer no qrcode: ')

data = a
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('Qrgit.png')



