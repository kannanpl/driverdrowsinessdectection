# Python program to illustrate
# simple thresholding type on an image

# organizing imports
import cv2
import numpy as np

# path to input image is specified and
# image is loaded with imread command
img = cv2.imread("C:\\Users\\user\\Desktop\\Facedetection\\swetha.jpg")


# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

# applying different thresholding
# techniques on the input image
# all pixels value above 120 will
# be set to 255
ret, thresh1 = cv2.threshold( img, 150, 255, cv2.WINDOW_NORMAL)
ret, thresh2 = cv2.threshold( img, 150, 255, cv2.THRESH_BINARY_INV )
ret, thresh3 = cv2.threshold( img, 120, 255, cv2.THRESH_TRUNC )
ret, thresh4 = cv2.threshold( img, 120, 255, cv2.THRESH_TOZERO )
ret, thresh5 = cv2.threshold( img, 120, 255, cv2.THRESH_TOZERO_INV )
#ret, frame = cv2.color_frame(img,120,255,cv2.frame)

# the window showing output images
# with the corresponding thresholding
# techniques applied to the input images
cv2.imshow( 'window normal', thresh1 )
cv2.imshow( 'Binary Threshold Inverted', thresh2 )
cv2.imshow( 'Truncated Threshold', thresh3 )
cv2.imshow( 'Set to 0', thresh4 )
cv2.imshow( 'Set to 0 Inverted', thresh5 )
#cv2.imshow("color frame", frame)
# De-allocate any associated memory usage
#if
cv2.waitKey(0) # & 0xff == 27:
 #cv2.destroyAllWindows()
