from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.class_names = self.model.names

    def detect(self, frame):
        results = self.model.predict(
            source=frame,
            conf=0.15,      # detect more objects
            iou=0.45,
            imgsz=640,
            verbose=False
        )
        return results[0].boxes
