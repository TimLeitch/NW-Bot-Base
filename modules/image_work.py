import time
import cv2
import mss
import numpy as np
from win32api import GetSystemMetrics


class Image_Processing:
    def get_image(x, y, w, h):  # screen grab function

        monitor = {
            "top": x,
            "left": y,
            "width": w,
            "height": h,
        }  # area of primary monitor to scan

        with mss.mss() as sct:
            image_rgb = np.array(sct.grab(monitor))  # get screen grab of selected area
            return image_rgb

    def show_image(
        x, y, w, h, loc
    ):  # debug function. used to show the area captured and to display fps

        while True:
            last_time = time.time()

            image = Image_Processing.get_image(x, y, w, h)
            cv2.imshow("", image)
            
            print("fps: {}".format(1 / (time.time() - last_time)))
            

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

    def full_template_match(
        template, threshold, debug=False
    ):  # template matching with debug function
        xTop, yTop, width, height = (
            0,
            0,
            GetSystemMetrics(0),
            GetSystemMetrics(1)
        )

        img_rgb = Image_Processing.get_image(
            xTop, yTop, width, height
        )  # get the source image

        img_gray = cv2.cvtColor(
            img_rgb, cv2.COLOR_RGB2GRAY
        )  # convert image to grayscale
        temp = cv2.imread(template, 0)  # read in the template image as grayscale

        w, h = temp.shape[::-1]  # get the size of the template image

        res = cv2.matchTemplate(
            img_gray, temp, cv2.TM_CCOEFF_NORMED
        )  # perform the template match

        loc = np.where(
            res >= threshold
        )  # get the x,y coords of matches that are higher then the threshold
        _, max_val, _, max_loc = cv2.minMaxLoc(
            res
        )  # get the max match value, and the location of the max matched value

        while debug:
              # show the image with the drawn rectangles
            for pt in zip(*loc[::-1]):
                cv2.rectangle(
                    img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2
                )  # draw rectangles around image   
            cv2.imshow("", img_rgb)     
                
            if cv2.waitKey(25) & 0xFF == ord("q"):  # wait for keypress to quit debug viewing
                cv2.destroyAllWindows()
                break

        if max_val >= threshold:
            return max_loc

    def template_match(
            template, threshold, debug=False
        ):  # template matching with debug function
            xTop, yTop, width, height = (
                0,
                GetSystemMetrics(0)//4,
                GetSystemMetrics(0)//2,
                GetSystemMetrics(1)
            )

            img_rgb = Image_Processing.get_image(
                xTop, yTop, width, height
            )  # get the source image

            img_gray = cv2.cvtColor(
                img_rgb, cv2.COLOR_RGB2GRAY
            )  # convert image to grayscale
            temp = cv2.imread(template, 0)  # read in the template image as grayscale

            w, h = temp.shape[::-1]  # get the size of the template image

            res = cv2.matchTemplate(
                img_gray, temp, cv2.TM_CCOEFF_NORMED
            )  # perform the template match

            loc = np.where(
                res >= threshold
            )  # get the x,y coords of matches that are higher then the threshold
            _, max_val, _, max_loc = cv2.minMaxLoc(
                res
            )  # get the max match value, and the location of the max matched value

            while debug:
                # show the image with the drawn rectangles
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(
                        img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2
                    )  # draw rectangles around image   
                cv2.imshow("", img_rgb)     
                    
                if cv2.waitKey(25) & 0xFF == ord("q"):  # wait for keypress to quit debug viewing
                    cv2.destroyAllWindows()
                    break

            if max_val >= threshold:
                return max_loc