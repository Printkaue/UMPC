import io
import qrcode

#função que gera o QRCODE

def generate_qr_code(url: str):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(url)
    qr.make(fit=True)

    image = qr.make_image(fill_color = "black", back_color = "white")
    buffer = io.BytesIO()

    image.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer