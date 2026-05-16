import cv2
import numpy as np

def read_qrcode(file_bytes=bytes):

    #Converte qrcode em bytes
    np_array = np.frombuffer(file_bytes, np.uint8)

    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
    #detecta o qrcode
    detector = cv2.QRCodeDetector()

    #retorna o conteudo
    data, verifices_array, _ = detector.detectAndDecode(image)

    if verifices_array is not None:
        return data
    
    return None