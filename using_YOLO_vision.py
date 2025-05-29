from ultralytics import YOLO#type:ignore
import cv2 #type:ignore

model = YOLO("yolov8s.pt")

results=model('fam.jpg',save=True)

for result in results:
    image =result.plot()
    

    w,h=image.shape[:2]
    cv2.namedWindow('fam',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('fam',w,h)

cv2.imshow('fam',image)
cv2.waitKey(0)




