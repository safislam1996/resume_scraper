# from PyPDF2 import PdfFileReader
import easyocr
import cv2
from pdf2image import convert_from_path
import os
import numpy as np

# reader=PdfFileReader("safi_CV_1(1).pdf")
# page=reader.pages[0]
file='safi_CV_1(1).pdf'
pages=convert_from_path(file,500,poppler_path=r'C:\Program Files\poppler-0.67.0\bin')
reader=easyocr.Reader(['en'])
IMAGE_PATH = 'pages/safi_CV_1(1).jpeg'

for page in pages:
    mypath='pages/'
    fname='{}.jpeg'.format(file.split('.')[0])
    pdf_page=page.save(mypath+fname,'JPEG')
    # img=cv2.imread('pages/')
    img_page=cv2.imread(pdf_page)
    img_text=reader.readtext(IMAGE_PATH,decoder='beamsearch',beamWidth=10,detail=0)
    print(img_text)