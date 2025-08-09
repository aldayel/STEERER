import cv2
import numpy as np
from ultralytics import YOLO

class CrowdHat:
    """Detects individual heads using a YOLO model."""
    def __init__(self, model_path='yolov8n.pt'):
        # Load a small YOLOv8 model
        self.model = YOLO(model_path)

    def detect_heads(self, frame):
        """Return centers of detected heads."""
        results = self.model(frame, verbose=False)
        centers = []
        for r in results:
            if r.boxes is None:
                continue
            for box in r.boxes.xyxy.cpu().numpy():
                x1, y1, x2, y2 = box[:4].astype(int)
                centers.append(((x1 + x2) // 2, (y1 + y2) // 2))
        return centers

class Steerer:
    """Estimates dense crowd regions via corner detection."""
    def estimate_density(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        features = cv2.goodFeaturesToTrack(gray, maxCorners=500, qualityLevel=0.01, minDistance=7)
        if features is None:
            return []
        return [tuple(pt.ravel().astype(int)) for pt in features]

def process_video(input_path, output_path=None):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise FileNotFoundError(f'Cannot open {input_path}')

    hat = CrowdHat()
    steerer = Steerer()
    writer = None

    if output_path:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        writer = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        red_points = hat.detect_heads(frame)
        green_points = steerer.estimate_density(frame)

        for x, y in red_points:
            cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)
        for x, y in green_points:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        if writer:
            writer.write(frame)

        cv2.imshow('STEERER', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    if writer:
        writer.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='STEERER dual-model crowd monitor')
    parser.add_argument('--input', default=r'C:\\Users\\user\\OneDrive\\Desktop\\6min.mp4', help='Path to input video')
    parser.add_argument('--output', default=None, help='Optional path to save annotated video')
    args = parser.parse_args()
    process_video(args.input, args.output)
