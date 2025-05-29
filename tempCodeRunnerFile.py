from ultralytics import YOLO  # Import YOLO
import cv2  # Import OpenCV

# Initialize webcam
cam = cv2.VideoCapture(0)

# Load YOLOv8 model (try a bigger model for better detection)
model = YOLO('yolov8s.pt')  # Try 'yolov8m.pt' for better results

# Set resolution (width=1080, height=720)
cam.set(3, 1080)
cam.set(4, 720)

while True:
    # Capture frame
    value, clips = cam.read()

    # If the frame is not read correctly, break the loop
    if not value:
        print("Error: Couldn't capture frame")
        break

    # Perform object detection with lower confidence threshold
    results = model(clips, conf=0.3)  # Adjust conf threshold to detect more objects

    # Loop through detection results
    for result in results:
        boxes = result.boxes  # Extract detected bounding boxes
        
        for box in boxes:
            # Get bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Get confidence score
            confidence = box.conf[0].item()  # Extract confidence score

            # Get class index and class name correctly
            class_id = int(box.cls[0])  # Extract class index
            component_name = result.names[class_id]  # Get class name using index
            
            # Filter detections based on confidence score
            if confidence > 0.3:  # Set a threshold to avoid false positives
                # Draw bounding box
                cv2.rectangle(clips, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # Display class name & confidence score
                label = f"{component_name} ({confidence:.2f})"
                cv2.putText(clips, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                            0.7, (0, 255, 0), 2)

                # Print detected class name and coordinates
                print(f"Detected: {component_name} ({confidence:.2f}) at ({x1}, {y1}, {x2}, {y2})")

    # Show the frame
    cv2.imshow('YOLO Detection', clips)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
