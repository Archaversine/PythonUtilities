import numpy as np
import cv2 as cv

from PIL import Image

DICTIONARIES = {
    "DICT_4X4_50": cv.aruco.DICT_4X4_50,
    "DICT_4X4_100": cv.aruco.DICT_4X4_100,
    "DICT_4X4_250": cv.aruco.DICT_4X4_50,
    "DICT_4X4_1000": cv.aruco.DICT_4X4_1000,
    "DICT_5X5_50": cv.aruco.DICT_5X5_50,
    "DICT_5X5_100": cv.aruco.DICT_5X5_100,
    "DICT_5X5_250": cv.aruco.DICT_5X5_250,
    "DICT_5X5_1000": cv.aruco.DICT_5X5_1000,
    "DICT_6X6_50": cv.aruco.DICT_6X6_50,
    "DICT_6X6_100": cv.aruco.DICT_6X6_100,
    "DICT_6X6_250": cv.aruco.DICT_6X6_250,
    "DICT_6X6_1000": cv.aruco.DICT_6X6_1000,
    "DICT_7X7_50": cv.aruco.DICT_7X7_50,
    "DICT_7X7_100": cv.aruco.DICT_7X7_100,
    "DICT_7X7_250": cv.aruco.DICT_7X7_250,
    "DICT_7X7_1000": cv.aruco.DICT_7X7_1000,
    "DICT_ARUCO_ORIGINAL": cv.aruco.DICT_ARUCO_ORIGINAL,
    "DICT_APRILTAG_16h5": cv.aruco.DICT_APRILTAG_16h5,
    "DICT_APRILTAG_25h9": cv.aruco.DICT_APRILTAG_25h9,
    "DICT_APRILTAG_36h10": cv.aruco.DICT_APRILTAG_36h10,
    "DICT_APRILTAG_36h11": cv.aruco.DICT_APRILTAG_36h11
}

def get_dictionary(dictionary_name):

    dictionary = DICTIONARIES.get(dictionary_name, None)

    if dictionary is None:
        return None
    else:
        return cv.aruco.Dictionary_get(dictionary)

class ArucoCode:

    # Defaults
    DEFAULT_SIZE = 300

    def __init__(self, a_id, a_dict, path, img_size=DEFAULT_SIZE):
        self.a_id = a_id            # ID/Number stored in ArucoCode
        self.a_dict = a_dict        # Dictionary used to create ArucoCode
        self.path = path            # Export path for ArucoCode
        self.size = img_size        # Size of ArucoCode in pixels

        if self.a_dict is not None:
            self.draw()
        else:
            print("Error: Aruco code has 'None' as dictionary")

    # Draw Aruco code image
    def draw(self):

        # Numpy Array for image
        self.img = np.zeros((self.size, self.size, 1), dtype="uint8")
        
        # Draw Aruco code to numpy array
        cv.aruco.drawMarker(self.a_dict, self.a_id, self.size, self.img, 1)

    # Save as file
    def export(self):
        if self.img is not None:
            cv.imwrite(self.path, self.img)
        else:
            print("Cannot export ungenerated code")

    # Show image to the screen
    def show(self):
        if self.img is not None:
            cv.imshow("aruco-code{}".format(self.a_id), self.img)
        else:
            print("Cannot show ungenerated code")

    # Return an image compatible with Python Pillow Library
    def get_pil_image(self):
        self.export()

        return Image.open(self.path, mode='r')

