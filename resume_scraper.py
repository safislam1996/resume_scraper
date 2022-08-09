# from PyPDF2 import PdfFileReader

import warnings
warnings.filterwarnings('ignore')
import easyocr
import cv2
from pdf2image import convert_from_path
import os
import numpy as np
from io import BytesIO
from PIL import Image

# reader=PdfFileReader("safi_CV_1(1).pdf")
# page=reader.pages[0]
file='safi_CV_1(1).pdf'
pages=convert_from_path(file,500,poppler_path=r'C:\Program Files\poppler-0.67.0\bin')
reader=easyocr.Reader(['en'])
IMAGE_PATH = 'pages/safi_CV_1(1).jpeg'

for page in pages:
    mypath='pages'
    fname='{}.jpeg'.format(file.split('.')[0])
    print(fname)
    IMG_PATH=str(mypath+'/'+fname)
    print(IMG_PATH)

    pdf_page=page.save(IMG_PATH,'JPEG')

    #creating an window to fit the image
    # cv2.namedWindow("output", cv2.WINDOW_AUTOSIZE)
    img_page=cv2.imread(IMG_PATH)
    # imS = cv2.resize(img_page, (960, 540))
    # cv2.imshow('img_page',imS)

    #extracting the image to find the specific image..
    img_text=reader.readtext(img_page,decoder='beamsearch',beamWidth=10,detail=0)
    # cv2.putText(img_page,'CGPA')

    
    print(len(img_text))
    print(img_text[0])
    i=0
    while(i<len(img_text)):

        print(img_text[i])
        i=i+1


 
    # Destroying present windows on screen
