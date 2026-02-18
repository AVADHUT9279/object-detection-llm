import cv2

def draw_boxes(frame, boxes, class_names):
    total = 0

    if boxes is not None:
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            # Ignore very weak detections
            if conf < 0.15:
                continue

            label = class_names[cls_id]
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            total += 1

            # Draw box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Draw label
            text = f"{label.upper()} ({conf*100:.1f}%)"
            cv2.putText(
                frame,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

    return total

def draw_total_count(frame, total):
    cv2.putText(
        frame,
        f"Total Objects Detected: {total}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )
