import cv2
import numpy as np
import pytesseract as pyt
from PIL import ImageGrab
from win32api import GetSystemMetrics


class Movement_Route:
    def screen_capture():

        xTop, yTop, xBottom, yBottom = (
            GetSystemMetrics(0) // 2 - 600,
            0,
            GetSystemMetrics(0),
            200,
        )  # defind the area to be captured

        cap = ImageGrab.grab(
            bbox=(xTop, yTop, xBottom, yBottom)
        )  # capture the specific area

        return cap

    def convert_image(img):
        img_arr = np.array(img)  # converts the image to an array

        return img_arr

    def show_capture(img):  # will display the area being captured real time
        cv2.imshow("", img)

    def to_text(img):  # try to get any text from the area being captured

        output = pyt.image_to_string(img)
        output = output.strip()  # removes spaces

        if len(output) > 0:  # checks to see if it actually captured a string
            return output

        else:
            return False
