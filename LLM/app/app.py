import cv2
from camera.camera import open_camera, read_frame, release_camera
from detector.detector import ObjectDetector
from utils.utils import draw_boxes, draw_total_count

def run_app():
    # Use better accuracy model
    detector = ObjectDetector("yolov8s.pt")

    cap = open_camera(0)
    if cap is None:
        return

    while True:
        frame = read_frame(cap)
        if frame is None:
            break

        # Detect objects
        boxes = detector.detect(frame)

        # Draw detections
        total = draw_boxes(frame, boxes, detector.class_names)
        draw_total_count(frame, total)

        cv2.imshow("Show Object to Camera (Press Q to Exit)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    release_camera(cap)
