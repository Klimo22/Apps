import qrcode
qr = qrcode.make('https://bit.ly/3jkjUo8')
qr.save('qrcode.jpg')
qr.show()