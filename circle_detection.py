import cv2 as cv
import numpy as np

# pattern_detect() function accepts path/location of the image file
# and returns a processed image and saves it in the same location
def pattern_detect(imgpath):

    img = cv.imread(imgpath)
    output = img.copy()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 0.5, 50, param1=70, param2=50, minRadius=0, maxRadius=0)
    detected_circles = np.uint16(np.around(circles))

    for (x,y,r) in detected_circles[0, :]:
        cv.circle(output, (x,y), r, (0,0,255), 2)

    cv.imwrite(filename = 'test_result_image.png', img = output)

if __name__ == "__main__":

    imgpath = input("Enter the image file name or location: ")

    pattern_detect(imgpath)

    # After executing the code, look for the desired file
    # in the same directory where the python file is located