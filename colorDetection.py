import cv2
import numpy as np
  
# reading the image data from desired directory

def color_analysis():
    print("12")
    img = cv2.imread("/Users/omar/Desktop/detectbottwitter/images/one.png")
    cv2.imshow('Image',img)
    
    # counting the number of pixels
    number_of_grey_pix = np.sum(img > 100)
    number_of_black_pix = np.sum(img == 0)
    number_of_total_pix = np.sum(img >= 0)

    global percent_grey

    percent_grey = np.sum((number_of_grey_pix/number_of_total_pix)*100)
    
    print('Number of Grey Pixels:', number_of_grey_pix)
    print('Number of Black Pixels:', number_of_black_pix)
    print('Number of Pixels:', number_of_total_pix)
    print('Percentage Grey:', percent_grey)

    global percentCertanity
    global emoji

    percent_difference = abs(percent_grey - 0.636)

    if (percent_difference <= 1.87):
        percentCertanity = 25
        emoji = "🧐"
    elif(percent_difference > 1.87 and percent_difference <= 2.87):
        percentCertanity = 50
        emoji = "😬"
    elif(percent_difference > 2.87 and percent_difference <= 4.87):
        percentCertanity = 75
        emoji = "😵"
    else:
        percentCertanity = 90
        emoji = "❌"



    

