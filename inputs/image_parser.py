from .parser import Parser
import cv2
import pytesseract
import numpy
import os


class Image_Parser(Parser):
    def opencv_preprocessing(img, cv2.BG2GRAY):
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        sharpen_kernel = numpy.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpened_image = cv2.filter2D(gray_img, -1, sharpen_kernel
        
        ret, thresh = cv2.threshold(sharpened_image, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)

        rect_kernel = cv2.getStructringElement(cv2.MORPH_RECT, (30, 30))
        smooth_img = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, rect_kernel, iterations=1)

        result_img = 255 - smooth_img
        
        return result_img

    def tesseract_extract_text(self, img, preprocessed_img):
    pytesseract.pytesseract.tesseract_cmd = r""

    contours, hierarchy = cv2.findContours(preprocessed_img, cv2.RECT_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    all_text = ""

    