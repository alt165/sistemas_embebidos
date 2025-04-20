import cv2
import numpy as np
from ultralytics import YOLO
import time
import sys

class VehicleDetector:
    def __init__(self, model_type='yolov8n.pt', device='cpu'):
        """
        Initialize vehicle detector with YOLOv8 model (newer than YOLOv5).
        
        Args:
            model_type (str): Model type ('yolov8n.pt', 'yolov8s.pt', etc.)
            device (str): 'cpu' or 'cuda' for GPU acceleration
        """
        try:
            self.model = YOLO(model_type)
            self.model.to(device)
            self.vehicle_classes = [2, 3, 5, 7]  # COCO: car, motorcycle, bus, truck
            self.frame_count = 0
            self.fps = 0
            self.start_time = time.time()
            print(f"Loaded model {model_type} successfully")
        except Exception as e:
            print(f"Error loading model: {e}")
            sys.exit(1)
    
    def detect_vehicles(self, frame):
        """Detect vehicles in frame and return annotated frame."""
        try:
            results = self.model(frame, verbose=False)
            
            # Calculate FPS
            self.frame_count += 1
            if time.time() - self.start_time >= 1.0:
                self.fps = self.frame_count / (time.time() - self.start_time)
                self.frame_count = 0
                self.start_time = time.time()
            
            vehicle_count = 0
            
            for result in results:
                for box in result.boxes:
                    class_id = int(box.cls)
                    if class_id in self.vehicle_classes:
                        vehicle_count += 1
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        confidence = float(box.conf)
                        label = f"{self.model.names[class_id].upper()}: {confidence:.2f}"
                        
                        color = self.get_class_color(class_id)
                        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                        
                        (label_width, label_height), _ = cv2.getTextSize(
                            label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
                        cv2.rectangle(
                            frame, (x1, y1 - label_height - 10),
                            (x1 + label_width, y1 - 10), color, -1)
                        
                        cv2.putText(
                            frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            
            # Display info
            cv2.putText(frame, f"FPS: {self.fps:.1f}", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.putText(frame, f"Vehicles: {vehicle_count}", (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            return frame
        
        except Exception as e:
            print(f"Detection error: {e}")
            return frame

    def get_class_color(self, class_id):
        """Return different colors for different vehicle classes."""
        colors = {
            2: (0, 255, 0),    # Green for cars
            3: (255, 0, 0),    # Blue for motorcycles
            5: (0, 0, 255),    # Red for buses
            7: (255, 255, 0)   # Cyan for trucks
        }
        return colors.get(class_id, (0, 255, 255))

def main():
    # Check GUI backend
    print("OpenCV GUI backend:", cv2.getBuildInformation())
    
    try:
        # Initialize detector with YOLOv8 (newer than YOLOv5)
        detector = VehicleDetector(model_type='yolov8n.pt')
        
        # Video source
        video_source = 0  # Change to 0 for webcam or "video.mp4" for file
        
        cap = cv2.VideoCapture(video_source)
        if not cap.isOpened():
            print("Error: Could not open video source")
            return
        
        # Try to create window (headless fallback)
        try:
            cv2.namedWindow("Vehicle Detection", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Vehicle Detection", 800, 600)
            gui_enabled = True
        except:
            print("GUI not available - running in headless mode")
            gui_enabled = False
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("End of video stream")
                break
            
            frame = cv2.resize(frame, (800, 600))
            detected_frame = detector.detect_vehicles(frame)
            
            if gui_enabled:
                cv2.imshow("Vehicle Detection", detected_frame)
                if cv2.waitKey(1) & 0xFF in [ord('q'), 27]:
                    break
            else:
                # Headless mode - just process frames
                pass
        
    except Exception as e:
        print(f"Main error: {e}")
    finally:
        cap.release()
        if gui_enabled:
            cv2.destroyAllWindows()

if __name__ == "__main__":
    # Verify and install dependencies
    try:
        import tkinter  # Test GUI availability
    except:
        print("Installing GUI dependencies...")
        import os
        os.system("sudo apt-get install -y python3-tk")
    
    main()