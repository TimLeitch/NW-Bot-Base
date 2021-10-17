import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab
from win32api import GetSystemMetrics

pytesseract.pytesseract.tesseract_cmd = (
    "C:/Program Files/Tesseract-OCR/tesseract.exe"  # your path may be different
)
while True:

    xTop, yTop = GetSystemMetrics(0) // 2 + 900, 0  # defind the area to be captured
    width, height = xTop + 400, yTop + 75

    icap = ImageGrab.grab(bbox=(xTop, yTop, width, height))  # capture the specific area

    # For us to use cv2.imshow we need to convert the image into a numpy array
    img = np.array(icap)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[
        1
    ]

    # cv2.imwrite('thresh.png', img)
    cv2.imshow("", img)

    # for psm in range(6,13+1):
    #     # config = '--oem 3 --psm %d' % psm
    #     txt = pytesseract.image_to_string(img,  lang='eng')
    #     # config = config,
    #     print('psm ', psm, ':',txt)
    text = pytesseract.image_to_string(img)

    text = text.strip()

    # If any text was translated from the image, print it
    if len(text) > 0:
        # testList = text.split('[')
        print(text)
        # print(testList)

    # This line will break the while loop when you press Esc
    if cv2.waitKey(1) == 27:
        break

# This will make sure all windows created from cv2 is destroyed
cv2.destroyAllWindows()
