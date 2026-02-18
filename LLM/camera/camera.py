import cv2

def open_camera(index=0):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print("❌ Camera not opening")
        return None

    # Better resolution for detection
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    return cap

def read_frame(cap):
    success, frame = cap.read()
    return frame if success else None

def release_camera(cap):
    cap.release()
    cv2.destroyAllWindows()
