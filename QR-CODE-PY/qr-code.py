import qrcode

data = "Hi I`ve created a qr-code"
img = qrcode.make(data)
img.save('C:/Users/d3sig/OneDrive/Desktop/Projects-Python/QR-CODE-PY/Img-saved/qr-code-img.png')
