
from ultralytics import YOLO

model = YOLO("runs/detect/runs/helmet_detection/weights/best.pt")

results = model.predict(
    source="outputs/test.jpg",
    conf=0.25,
    save=True
)

print("Prediction completed successfully.")