from ultralytics import YOLO 
import cv2 
import cvzone
import math

cam=cv2.VideoCapture(0)
model=YOLO('yolov8n.pt')

while True:
    value,clips=cam.read()
    results=model(clips,stream=True)
    for result in results:
        boxes=result.boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2) 
            w,h=x2-x1,y2-y1 
            cvzone.cornerRect(clips,(x1,y1,w,h))
            conf=math.ceil((boxes.conf[0]*100))/100

            #cv2.rectangle(clips,(x1,y1),(x2,y2),(255,0,255),3) 
            
            class_id=int(boxes.cls[0])
            component_name=result.names[class_id]
            cv2.putText(clips,f'{component_name} {conf}',(x1,y1-20), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),3)
            print(x1,y1,x2,y2)


    cv2.imshow('window',clips)
    cv2.waitKey(1)





