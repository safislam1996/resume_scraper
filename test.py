   img_page=cv2.imread(pdf_page)
    print(pdf_page)
    # cv2.imshow('img_page',img_page)
    # cv2.waitKey(2000)
    #this scrape the texts from the images using easyocr library
    # img_text=reader.readtext(IMAGE_PATH,decoder='beamsearch',beamWidth=10,detail=0)
    # cv2.putText(img_page,'CGPA')


      for (text,bbox,prob) in img_text:

        print("[INFO] {:.4f}: {}".format(prob,text))
        # (tl, tr, br, bl)= bbox
        # tl = (int(tl[0]), int(tl[1]))
        # tr = (int(tr[0]), int(tr[1]))
        # br = (int(br[0]), int(br[1]))
        # bl = (int(bl[0]), int(bl[1]))
        # cv2.rectangle(img_page,tl,br,(0,255,0),0)
        # cv2.putText(img_page,text,(tl[0], tl[1] - 10),
		# cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("image",img_page)
    cv2.waitKey(0)