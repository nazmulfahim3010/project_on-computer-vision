import cv2 as cv  # type: ignore

img=cv.imread("fam.jpg")

cv.namedWindow('fam', cv.WINDOW_NORMAL)  # Allows window resizing
cv.imshow('fam', img)
cv.resizeWindow('fam', 500, 500)  # Set custom window size

cv.waitKey(0)
cv.destroyAllWindows()



