import qrcode


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', backcolor='white')
    img.save('qrimg.png')


if __name__ == '__main__':
    url = input('enter your url: ')
    generate_qrcode(url)
