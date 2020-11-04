import cv2
from pyzbar import pyzbar


def barcode_reader(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized Barcode:" + info)
    return frame


camera = cv2.VideoCapture(0)
ret, frame = camera.read()
while ret:
    ret, frame = camera.read()
    frame = barcode_reader(frame)
    cv2.imshow('Barcode/QR', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()