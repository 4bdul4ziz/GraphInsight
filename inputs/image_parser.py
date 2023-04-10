from .parser import Parser
import cv2
import pytesseract
import numpy
import os

class Image_Parser(Parser):
    def opencv_preprocessing(self, img):
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        sharpen_kernel = numpy.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpened_img = cv2.filter2D(gray_img, -1, sharpen_kernel)

        ret, thresh = cv2.threshold(sharpened_img, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)

        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30))
        smooth_img = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, rect_kernel, iterations=1)

        result_img = 255 - smooth_img
        return result_img


    def tesseract_extract_text(self, img, preprocessed_img):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\marti\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

        contours, hierarchy = cv2.findContours(preprocessed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        all_text = ""

        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            cropped_img = img[y:y + h, x:x + w]

            extracted_text = pytesseract.image_to_string(cropped_img, lang='eng', config='--psm 6')
            all_text = extracted_text + all_text

        return all_text

    def parse(self):
        img = cv2.imread(self.input_file)
        preprocessed_img = self.opencv_preprocessing(img)
        return self.tesseract_extract_text(img, preprocessed_img)
